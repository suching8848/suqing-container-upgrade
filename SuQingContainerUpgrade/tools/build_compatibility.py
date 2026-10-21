"""Generate the exact audited runtime scope and human reports from registry.json.

Python 3: python tools/build_compatibility.py [--check]
Only package-generated files are written. Workshop/game/save files are not opened.
"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import hashlib
import io
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'compatibility/registry.json'
LUA = ROOT / '42/media/lua/shared/SuQingContainerUpgrade/Compatibility.lua'
RECIPES = ROOT / '42/media/scripts/SuQingContainerUpgrade.txt'
ORIGINAL = {'Base.Bag_ChestRig_083', 'Base.2dw_reapenforcebag',
            'Base.AmmoStrap_Bullets', 'TheyKnew.MysteriousSatchel'}
STATUSES = {'active', 'restoreOnly', 'deferred', 'excluded'}
LABELS = {'active': '已支持', 'restoreOnly': '仅保留旧记录还原',
          'deferred': '暂缓适配', 'excluded': '排除'}
ACTIVE_PROFILES = {'existing_v013', 'standard_light', 'heavy_native_cap',
                   'position_pair', 'restricted_webbing', 'restricted_ammo',
                   'restricted_holster', 'hybrid_container', 'mod_container',
                   'native_capacity', 'dynamic_capacity'}
NATIVE = {'Base.BagS_cat_23', 'Base.BagS_cat_24', 'Base.BagS_cat_25',
          'Base.CamoHydrationPackpack'}
DYNAMIC = {'Base.ResidentEvilBackPack', 'Base.ResidentEvilSuspenders'}
HYBRID = {'Base.Bag_HydrationBackpack', 'Base.Bag_HydrationBackpack_Camo'}
NATIVE_CHAIN = {'Base.Bag_cat_' + str(i) for i in range(1, 7)}
VANILLA_NATIVE_UPGRADE = {'Base.Bag_CrudeLeatherBag', 'Base.Bag_CrudeTarpBag'}
EXPECTED_PROVIDER_TOTALS = {'vanilla': 86, 'FantasyWorkshopVS42_4.0': 38,
    '4123567854998': 17, 'BackpackSystemB42': 25, 'SuPrimitiveEquipment': 4,
    'TheyKnewContinued': 2, 'RaccoonCityB42': 2, 'SafeWayHamlet': 1,
    'Estate 39': 1, 'LBB42': 10, 'ModernFirearmsSystem': 1}
SOURCE_KEYS = ['fullType', 'nameCN', 'provider', 'capacity', 'weightReduction',
    'weight', 'slot', 'bodyLocation', 'source', 'sourceSha256', 'restrictions',
    'tags', 'attachmentsProvided', 'fluidCapacity', 'nameSource']
RESTRICTION_KEYS = {'acceptItemFunction', 'onlyAcceptCategory', 'maxItemSize',
    'clothingItemExtra', 'clothingItemExtraOption', 'clothingExtraSubmenu',
    'fluidComponent'}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    def normalized(item):
        if isinstance(item, float) and item.is_integer():
            return int(item)
        if isinstance(item, dict):
            return {key: normalized(val) for key, val in item.items()}
        if isinstance(item, list):
            return [normalized(val) for val in item]
        return item
    return hashlib.sha256(json.dumps(normalized(value), ensure_ascii=False, sort_keys=True,
        separators=(',', ':')).encode('utf-8')).hexdigest()


def utf16_units(value):
    raw = value.encode('utf-16-le')
    return [int.from_bytes(raw[i:i + 2], 'little') for i in range(0, len(raw), 2)]


def full_extra(row):
    extra = row['restrictions']['clothingItemExtra']
    if not extra:
        return None
    return extra if '.' in extra else row['fullType'].split('.')[0] + '.' + extra


def safe_v(row):
    if row['profile'] == 'dynamic_capacity':
        return None
    limit = math.floor(50 - row['weight'])
    if row['profile'] == 'native_capacity':
        return min(row['capacity'], limit)
    return max(row['capacity'], min(49, limit))


def validate(registry):
    check(registry.get('schema') == 1, 'Unsupported registry schema')
    rows = registry['items']
    ids = [row['fullType'] for row in rows]
    check(ids == sorted(ids) and len(set(ids)) == len(ids), 'Duplicate or unsorted fullType')
    check(ids == registry.get('auditedFullTypes'), 'Whitelist differs from audited source IDs')
    check(registry.get('sourceBindingKeys') == SOURCE_KEYS, 'Source binding fields changed')
    expected = registry['expectedCounts']
    check(len(rows) == expected['registryEntries'] == 187, 'Reviewed total scope differs')
    check(Counter(row['provider'] for row in rows) == Counter(EXPECTED_PROVIDER_TOTALS),
          'Provider source inventory differs')
    for row in rows:
        name = row['fullType']
        check(re.fullmatch(r'[A-Za-z0-9_]+\.[A-Za-z0-9_]+', name), 'Invalid fullType: ' + name)
        check(row['status'] in STATUSES, 'Invalid status: ' + name)
        for key in ('nameCN', 'provider', 'batch', 'profile', 'reason', 'source',
                    'sourceSha256', 'sourceClassification', 'slot', 'nameSource'):
            check(bool(row.get(key)), 'Missing ' + key + ': ' + name)
        check(row['provider'] in registry['providers'], 'Unknown provider: ' + name)
        check(re.fullmatch('[0-9a-f]{64}', row['sourceSha256']), 'Invalid source hash: ' + name)
        check(row.get('sourceBindingSha256') == digest({key: row.get(key) for key in SOURCE_KEYS}),
              'Source defaults/limits binding differs: ' + name)
        restrictions = row.get('restrictions', {})
        check(set(restrictions) == RESTRICTION_KEYS, 'Missing special-container audit: ' + name)
        check(type(restrictions['fluidComponent']) is bool, 'Invalid fluid audit: ' + name)
        check(isinstance(row['tags'], list), 'Missing tags audit: ' + name)
        check(type(row['capacity']) is int and 0 <= row['capacity'] <= 100000,
              'Invalid source capacity: ' + name)
        check(type(row['weightReduction']) in (int, float) and 0 <= row['weightReduction'] <= 100,
              'Invalid source WR: ' + name)
        check(type(row['weight']) in (int, float) and 0 < row['weight'] < 50,
              'Invalid source self weight: ' + name)
        if row['status'] != 'active':
            continue
        profile = row['profile']
        check(profile in ACTIVE_PROFILES, 'Unknown active capacity profile: ' + name)
        check(not row['hasOwnNativeCapacityUpgradeInput'], 'Native capacity upgrade admitted: ' + name)
        check(row.get('requireEmptyFluid') is restrictions['fluidComponent'],
              'Fluid operation-empty policy differs: ' + name)
        check(row.get('targetCapacityV') == safe_v(row), 'Advertised V capacity differs: ' + name)
        check(restrictions['onlyAcceptCategory'] in (None, ''), 'Unaudited category limit: ' + name)
        accept = restrictions['acceptItemFunction']
        check(accept in (None, '', 'AcceptItemFunction.AmmoStrap_Bullets',
              'AcceptItemFunction.AmmoStrap_Shells', 'AcceptItemFunction.HolsterShoulder'),
              'Unaudited acceptance function: ' + name)
        if accept == 'AcceptItemFunction.HolsterShoulder':
            check(name == 'Base.HolsterShoulder' and profile == 'restricted_holster',
                  'Hard-count holster limit changed: ' + name)
        elif accept:
            check(profile in ('restricted_ammo', 'existing_v013')
                  or name == 'Base.RuBag', 'Unexpected restricted-mod source: ' + name)
        size = restrictions['maxItemSize']
        check(size is None or (profile == 'restricted_webbing' and size == 1.3)
              or (name == 'Base.ResidentEvilSuspenders' and size == 3),
              'Unaudited item-size limit: ' + name)
        if profile == 'native_capacity':
            check(name in NATIVE and row['capacity'] >= 50
                  and row['capacityMode'] == 'preserve_native',
                  'Native raw-capacity strategy differs: ' + name)
        elif profile == 'dynamic_capacity':
            check(name in DYNAMIC and row['capacityMode'] == 'business_overlay'
                  and row.get('dynamicCapacityOption') and row.get('dynamicWeightReductionOption'),
                  'Dynamic sandbox strategy differs: ' + name)
        elif profile == 'hybrid_container':
            check(name in HYBRID and restrictions['fluidComponent'], 'Hybrid scope differs: ' + name)
        elif profile == 'restricted_holster':
            check(name == 'Base.HolsterShoulder' and accept == 'AcceptItemFunction.HolsterShoulder',
                  'Holster profile scope differs: ' + name)
        elif profile in ('standard_light', 'heavy_native_cap'):
            check(row['provider'] == 'vanilla' and row['slot'] in ('base:back', 'base:satchel'),
                  'Ordinary vanilla slot/provider differs: ' + name)
            check(not restrictions['fluidComponent'], 'Fluid ordinary bag: ' + name)
            for key in ('acceptItemFunction', 'onlyAcceptCategory', 'maxItemSize',
                        'clothingItemExtra', 'clothingItemExtraOption'):
                check(restrictions[key] in (None, ''), 'Ordinary bag has special restriction: ' + name)
            if profile == 'standard_light':
                check(row['batch'] == 'vanilla_light_1' and row['weight'] <= 1
                      and row['sourceClassification'] == 'selected_v014', 'Light audit differs: ' + name)
            else:
                check(row['batch'] == 'vanilla_heavy_2' and row['weight'] > 1
                      and row['capacity'] <= math.floor(50 - row['weight'])
                      and row['sourceClassification'] == 'selected_v015_heavy',
                      'Heavy audit differs: ' + name)
        elif profile in ('position_pair', 'restricted_webbing', 'restricted_ammo'):
            check(row['provider'] == 'vanilla' and row['batch'] == 'vanilla_special_3'
                  and row['sourceClassification'] == 'selected_v016_special'
                  and row['weight'] <= 1 and not restrictions['fluidComponent'],
                  'Special vanilla source differs: ' + name)
            if profile == 'restricted_webbing':
                check(row['slot'] == 'base:webbing' and size == 1.3
                      and 'base:reloadfastmagazines' in row['tags'], 'Webbing size/reload audit differs: ' + name)
            elif profile == 'restricted_ammo':
                tag = {'AcceptItemFunction.AmmoStrap_Bullets': 'base:reloadfastbullets',
                       'AcceptItemFunction.AmmoStrap_Shells': 'base:reloadfastshells'}.get(accept)
                check(row['slot'] == 'base:ammostrap' and tag in row['tags'],
                      'Ammo accept/reload audit differs: ' + name)
            else:
                check(row['slot'] in ('base:fannypackfront', 'base:fannypackback')
                      and row.get('positionPair') and row.get('material') in ('standard', 'hide', 'tarp'),
                      'Vanilla position source differs: ' + name)
        elif profile == 'existing_v013':
            check(name in ORIGINAL, 'Legacy profile expanded: ' + name)
        elif profile == 'mod_container':
            check(row['provider'] != 'vanilla' and row['capacity'] < 50
                  and row['sourceClassification'] == 'audited_v020_enabled',
                  'Mod physical source profile differs: ' + name)
        if profile not in ('native_capacity', 'dynamic_capacity'):
            check(row['capacityMode'] == 'physical', 'Physical capacity mode differs: ' + name)
        if restrictions['clothingItemExtraOption']:
            check(row.get('positionPair') == full_extra(row), 'Unprotected native replacement: ' + name)

    active = sorted(row['fullType'] for row in rows if row['status'] == 'active')
    retired = sorted(row['fullType'] for row in rows if row['status'] == 'restoreOnly')
    check(ORIGINAL <= set(active), 'Previously supported types must remain active')
    check(retired == ['Base.Bag_cat_5'], 'Legacy restore-only scope differs')
    for status in STATUSES:
        check(sum(row['status'] == status for row in rows) == expected[status],
              'Reviewed status count differs: ' + status)
    check(len(active) == 168 and expected['active'] == 168, 'Active whitelist differs')
    check(sum(row['provider'] == 'vanilla' and row['status'] == 'active' for row in rows)
          == expected['activeVanilla'] == 84, 'Vanilla active count differs')
    check(sum(row['provider'] != 'vanilla' and row['status'] == 'active' for row in rows)
          == expected['activeMod'] == 84, 'Mod active count differs')
    check(sum(row['provider'] == 'vanilla' for row in rows)
          == expected['vanillaInventoryIncludingFluid'] == 86, 'Vanilla source inventory differs')
    check(sum(row['provider'] != 'vanilla' for row in rows)
          == expected['modInventory'] == 101, 'Mod source inventory differs')
    check(Counter(row['profile'] for row in rows if row['status'] == 'active')
          == Counter(expected['profiles']), 'Reviewed profile counts differ')
    check(sum(row['status'] == 'active' and row['batch'] == registry['currentBatch'] for row in rows)
          == expected['addedThisBatch'], 'Current batch active count differs')
    for provider, metadata in registry['providers'].items():
        group = [row for row in rows if row['provider'] == provider]
        check(metadata['name'] and len(group) == metadata['total']
              and Counter(row['status'] for row in group) == Counter(metadata['counts']),
              'Provider report counts differ: ' + provider)
    check(registry['providers']['SuPrimitiveEquipment']['name'] == '苏别璃原始装备',
          'Confirmed SuPrimitiveEquipment name differs')
    check({row['fullType'] for row in rows if row['profile'] == 'native_capacity'} == NATIVE,
          'Native capacity profile whitelist differs')
    check({row['fullType'] for row in rows if row['profile'] == 'dynamic_capacity'} == DYNAMIC,
          'Dynamic profile whitelist differs')
    excluded = {row['fullType'] for row in rows if row['status'] == 'excluded'}
    maximum = {row['fullType'] for row in rows if row['provider'] == 'LBB42'} | {'Base.MikuBackPack'}
    check(excluded == VANILLA_NATIVE_UPGRADE | (NATIVE_CHAIN - {'Base.Bag_cat_5'}) | maximum,
          'Excluded exact source scope differs')
    check(registry['fluidPolicy']['requireCompletelyEmptyBeforeUpgradeOrRestore'] is True
          and registry['fluidPolicy']['writeFluidComponent'] is False, 'Fluid preservation policy differs')

    positioned = {row['fullType']: row for row in rows
                  if row['status'] == 'active' and row.get('positionPair')}
    check(len(positioned) == expected['positionMappings'] == 13, 'Position mappings count differs')
    for name, row in positioned.items():
        pair = positioned.get(row['positionPair'])
        check(pair is not None and pair['positionPair'] == name
              and row['positionPair'] == full_extra(row)
              and bool(row['restrictions']['clothingItemExtraOption']),
              'Position mapping must match exact native reciprocal/self action: ' + name)
        check(all(row[key] == pair[key] for key in ('profile', 'capacity', 'weightReduction', 'weight')),
              'Position mapping changes source specs/profile: ' + name)
        if name != pair['fullType']:
            check(row['slot'] != pair['slot'], 'Opposite-position pair shares slot: ' + name)
            check(row.get('material') == pair.get('material'), 'Position material differs: ' + name)

    variants = registry['variantRecipes']
    check(registry.get('variantSourceBindingSha256') == digest(variants),
          'Variant source identity/edge binding differs')
    check(len(variants) == expected['variantRecipes'] == 8, 'Variant recipe count differs')
    check(len({v['id'] for v in variants}) == len(variants)
          and len({v['recipeFullType'] for v in variants}) == len(variants),
          'Duplicate variant identity')
    lookup = {row['fullType']: row for row in rows}
    for variant in variants:
        check(bool(variant.get('source')) and re.fullmatch('[0-9a-f]{64}', variant.get('sourceSha256', '')),
              'Variant recipe source hash missing')
        check(re.fullmatch(r'recipe_[1-8]', variant['id']) and variant['recipeFullType'].startswith('Base.')
              and variant['recipeCodepoints'] == utf16_units(variant['recipeFullType']),
              'Variant native Unicode identity differs')
        source, target = lookup.get(variant['from']), lookup.get(variant['target'])
        check(source and target and source['status'] == target['status'] == 'active'
              and source['profile'] == target['profile'] == 'mod_container'
              and source['provider'] == target['provider'] == '4123567854998',
              'Variant targets are outside the reviewed mod profile')
        check(all(source[key] == target[key] for key in ('capacity', 'weightReduction', 'weight', 'slot')),
              'Variant changes original storage specs/slot')
        check(not source['restrictions']['fluidComponent'] and not target['restrictions']['fluidComponent'],
              'Unaudited fluid size conversion')
    return rows, active, retired, positioned, variants


def restriction_text(row):
    r = row['restrictions']
    parts = []
    if r['acceptItemFunction']:
        parts.append(r['acceptItemFunction'])
    if r['maxItemSize'] is not None:
        parts.append('最大物品尺寸' + str(r['maxItemSize']))
    if row['fullType'] == 'Base.HolsterShoulder':
        parts.append('最多2个手枪弹匣')
    if r['fluidComponent']:
        parts.append('液体' + str(row.get('fluidCapacity')) + 'L；操作前排空；不改液体')
    if row.get('positionPair'):
        parts.append('精确穿戴/换位保护')
    if row['profile'] == 'dynamic_capacity':
        parts.append('原沙盒业务容量；保留原标签/挂点')
    if row['fullType'] == 'Base.cat_AutoReload':
        parts.append('原5发装填周期不变')
    return '；'.join(parts) or '原槽位、标签和挂点保持'


def display_v(row):
    return '原沙盒容量与强化下限叠加' if row['profile'] == 'dynamic_capacity' else str(row.get('targetCapacityV', ''))


def render():
    raw = REGISTRY.read_bytes()
    registry = json.loads(raw.decode('utf-8'))
    rows, active, retired, positioned, variants = validate(registry)
    lines = ['-- GENERATED by tools/build_compatibility.py; edit compatibility/registry.json.',
             '-- Unicode names stay in JSON/CSV; native recipe identity is numeric UTF-16.',
             'SuQingContainerUpgradeCompatibility = {', '    schema = 1,',
             '    registrySha256 = "' + hashlib.sha256(raw).hexdigest() + '",',
             '    supported = {']
    lines += ['        ["' + name + '"] = true,' for name in active]
    lines += ['    },', '    retired = {']
    lines += ['        ["' + name + '"] = true,' for name in retired]
    lines += ['    },', '    profiles = {']
    lines += ['        ["' + row['fullType'] + '"] = "' + row['profile'] + '",'
              for row in rows if row['status'] in ('active', 'restoreOnly')]
    lines += ['    },', '    positionPairs = {']
    lines += ['        ["' + name + '"] = "' + row['positionPair'] + '",'
              for name, row in sorted(positioned.items())]
    lines += ['    },', '    variantRecipes = {']
    for variant in variants:
        lines += ['        { id = "' + variant['id'] + '", from = "' + variant['from']
                  + '", target = "' + variant['target'] + '",',
                  '          recipeCodepoints = { ' + ', '.join(map(str, variant['recipeCodepoints'])) + ' } },']
    lines += ['    },', '}', 'return SuQingContainerUpgradeCompatibility', '']
    lua = '\n'.join(lines)

    script = RECIPES.read_text(encoding='utf-8')
    # Own the six native recipe icon bindings as well as their exact target IDs.
    # Rebuilding the audit reports must neither remove nor duplicate the icons.
    recipe_names = ['SuQingUpgrade' + str(i) for i in range(1, 6)] + ['SuQingRestore']
    header = re.compile(r'(?m)^    craftRecipe (SuQing(?:Upgrade[1-5]|Restore))\n    \{\n')
    check(header.findall(script) == recipe_names, 'Unexpected recipe headers for icon bindings')
    script = re.sub(r'(?m)^        Icon = Item_SuQing(?:Upgrade[1-5]|Restore),\n', '', script)
    script = header.sub(lambda match: match[0] + '        Icon = Item_' + match[1] + ',\n', script)
    blocks = re.findall(r'(?ms)^    craftRecipe (\w+)\n    \{\n(.*?)(?=^    craftRecipe |\Z)', script)
    check([name for name, _ in blocks] == recipe_names, 'Unexpected recipe blocks')
    for name, body in blocks:
        icons = re.findall(r'(?mi)^\s*icon\s*=\s*([^,\r\n]+)\s*,', body)
        check([value.strip() for value in icons] == ['Item_' + name],
              'Each owned recipe must have exactly its own icon: ' + name)
    pattern = re.compile(r'(?m)^(            item 1 )\[[^\]\n]+\]( mode:keep flags\[IsNotWorn;AllowFavorite;ItemCount\],)$')
    check(len(list(pattern.finditer(script))) == 6, 'Expected exactly six native recipe target lines')
    check(re.findall(r'\bcraftRecipe\s+(\w+)', script) ==
          ['SuQingUpgrade' + str(i) for i in range(1, 6)] + ['SuQingRestore'],
          'Unexpected recipe identity/order')
    counter = [0]
    def replacement(match):
        counter[0] += 1
        scope = active if counter[0] <= 5 else sorted(active + retired)
        return match[1] + '[' + ';'.join(scope) + ']' + match[2]
    script = pattern.sub(replacement, script)
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, lineterminator='\r\n')
    writer.writerow(['物品ID', '中文名称', '来源', '来源ID', '适配状态', '批次', '规格方案',
                     '源脚本容量', '源减重率', '源自重', '满级实际基础容量说明',
                     '容量处理', '原收纳/功能限制', '精确换位配对ID', '审计说明', '来源文件'])
    for row in rows:
        writer.writerow([row['fullType'], row['nameCN'], registry['providers'][row['provider']]['name'],
            row['provider'], LABELS[row['status']], row['batch'], row['profile'],
            row['capacity'], row['weightReduction'], row['weight'],
            display_v(row) if row['status'] == 'active' else '', row['capacityMode'],
            restriction_text(row), row.get('positionPair', ''), row['reason'], row['source']])
    supported = ['蘇清的容器升级 ' + registry['modVersion'] + ' 最终适配物品名单', '',
        'B42.21单人版。当前明确支持168个完整ID：原版84、已审计模组84。',
        '客户端代表项在单人档测试；168项为支持范围，不代表逐件游戏内实测。多人/联机未验证。',
        '下面只列支持强化的物品；187项完整分类（含仅还原1、排除18）见适配名单.csv。',
        '规格均为源脚本默认值，实际实例/沙盒可能不同；V不降低已有容量或减重。',
        '原物品尺寸、种类、2弹匣硬限制、槽位、挂点、装填规则及液体组件保持。',
        '液体与普通库存须在强化/还原前排空；高原生容量项只强化减重，浣熊市保留沙盒业务容量。',
        '']
    for provider, meta in registry['providers'].items():
        group = [row for row in rows if row['provider'] == provider and row['status'] == 'active']
        if not group:
            continue
        supported += [meta['name'] + '（' + str(len(group)) + '个ID）']
        for row in group:
            supported.append(row['nameCN'] + ' | ' + row['fullType'] + ' | 源'
                + str(row['capacity']) + '/' + str(row['weightReduction']) + '% | 自重'
                + str(row['weight']) + ' | V实际基础容量：' + display_v(row)
                + ' | ' + restriction_text(row))
        supported.append('')
    stats = ['蘇清的容器升级 ' + registry['modVersion'] + ' 适配统计', '',
        'B42.21单人版；168项为明确支持的ID，客户端代表项单人测试与离线回归分开记录。',
        '多人/联机未验证；本包不修改工坊原件或自动改写存档与启用名单。',
        '唯一人工维护清单：compatibility/registry.json；由build_compatibility.py确定性生成运行时和报告。',
        '全量来源：187个完整ID = 原版86 + 当前启用模组101。',
        '支持强化：168 = 原版84 + 模组84；仅旧记录还原：1（踏行千山五）；排除：18；暂缓：0。',
        '排除18 = 原版原生升级包2 + 踏行千山其它等级5 + 初音背包1 + 传奇背包10。',
        '初音/传奇原规格已达或超过目标，不收费、不新增记录；踏行千山继续走原模组一至六级扩容链。',
        '本批在此前84个支持ID基础新增84个；中文同名、材质和尺码仍按完整ID分别统计。', '',
        '支持数/来源清点数：']
    for provider, meta in registry['providers'].items():
        stats.append(meta['name'] + '：支持' + str(meta['counts'].get('active', 0))
                     + ' / 来源' + str(meta['total']))
    stats += ['', '容量与原机制：',
        '普通物理容器按名义档位与floor(50-当前实际自重)计算；不降低原有更高容量/减重，保留原100减重。',
        'native_capacity四件（背包系统23/24/25、SafeWay水袋包）绝不调用容量setter，只提高减重；脚本50/60不等于实际可用容量。',
        '浣熊市两件不写物理容量：沿用原沙盒业务容量与特性算法，用有效记录叠加强化下限。',
        '肩挂枪套原生最多2个手枪弹匣保持；胸挂最大尺寸1.3和浣熊市背带3.0、弹带过滤/装填标签保持。',
        '所有混合液体容器只强化普通储物；操作前清空物品和液体，绝不改流体容量/内容/混合物。',
        '13条精确穿戴/换位映射：原版6 + oldcat同ID5 + 苏别璃前后腰包2；仅有效自身记录启用保护。',
        '二维衣橱8条精确改码配方保留内容引用、外观与强化记录；主库存且卸下后改码，超载/异常回滚。',
        '自动装弹机构保留有效定义2/91与原5发装填周期，不安装旧自动喂弹或新的tick逻辑。',
        '原生新制作将背包当材料消耗时请先还原已有强化（例如近轨航行背包材料）；不会把所有合成泛化为属性继承。',
        '仍使用原生制作入口；不增加右键/悬浮/Halo/Say提示，不周期扫描。', '',
        '完整187项见适配名单.csv；仅支持168项详见最终适配物品名单.txt。',
        '代表项已进行单人客户端测试；离线/API验证不代表所有168项已逐件完成显示、实际换弹或保存重进验收。', '']
    outputs = {LUA: lua.encode('ascii'), RECIPES: script.encode('utf-8'),
        ROOT / '适配名单.csv': stream.getvalue().encode('utf-8-sig'),
        ROOT / '适配统计.txt': '\n'.join(stats).encode('utf-8'),
        ROOT / '最终适配物品名单.txt': '\n'.join(supported).encode('utf-8')}
    return outputs, registry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify generated files without writing')
    args = parser.parse_args()
    outputs, registry = render()
    differences = [str(path.relative_to(ROOT)) for path, data in outputs.items()
                   if not path.is_file() or path.read_bytes() != data]
    if args.check:
        check(not differences, 'Generated files differ: ' + ', '.join(differences))
    else:
        for path, data in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(json.dumps({'mode': 'check' if args.check else 'build',
        'active': registry['expectedCounts']['active'], 'restoreOnly': registry['expectedCounts']['restoreOnly'],
        'registryEntries': len(registry['items']), 'activeVanilla': registry['expectedCounts']['activeVanilla'],
        'activeMod': registry['expectedCounts']['activeMod'],
        'generated': [str(path.relative_to(ROOT)) for path in outputs]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
