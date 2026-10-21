"""Create a first-upload folder for the game's Workshop screen. Never contacts Steam."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import struct

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'SuQingContainerUpgrade'
PUBLISHING = ROOT / 'publishing'
MOD_ID = 'SuQingContainerUpgrade_4221'
NAME = 'SuQingContainerUpgrade'
DISALLOWED = {'.exe', '.dll', '.bat', '.app', '.dylib', '.sh', '.so', '.zip'}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def files(root):
    result = {}
    for path in sorted(root.rglob('*')):
        require(not path.is_symlink(), 'Linked content is not supported: ' + str(path))
        if path.is_file():
            result[path.relative_to(root).as_posix()] = sha(path)
    return result

def info(path):
    return dict(line.split('=', 1) for line in path.read_text(encoding='utf-8-sig').splitlines() if '=' in line)

def preview(path):
    raw = path.read_bytes()
    require(raw[:8] == b'\x89PNG\r\n\x1a\n' and raw[12:16] == b'IHDR', 'Preview must be a PNG')
    width, height = struct.unpack('>II', raw[16:24])
    require(width == height and width in (256, 512), 'Preview must be 256x256 or 512x512')
    require(len(raw) <= 1_024_000, 'Preview must be no larger than 1,024,000 bytes')
    return {'width': width, 'height': height, 'bytes': len(raw), 'sha256': sha(path)}

def validate(destination):
    contents = destination / 'Contents'
    require(contents.is_dir(), 'Missing Contents folder')
    require(all(path.is_dir() and path.name in {'mods', 'buildings', 'creative'} for path in contents.iterdir()),
            'Contents may contain only supported content folders')
    mods = contents / 'mods'
    require(mods.is_dir() and {path.name for path in mods.iterdir()} == {NAME}, 'Expected exactly this one mod folder')
    packaged = mods / NAME
    require((packaged / 'common').is_dir(), 'Missing common folder')
    fields = info(packaged / '42/mod.info')
    source_fields = info(SOURCE / '42/mod.info')
    require(fields.get('id') == MOD_ID and fields.get('modversion') == source_fields.get('modversion'),
            'Unexpected mod identity or version')
    for path in contents.rglob('*'):
        require(not path.is_symlink(), 'Linked content is not supported')
        require(path.suffix.lower() not in DISALLOWED, 'Disallowed Workshop file type: ' + str(path))
    require(files(packaged) == files(SOURCE), 'Staged mod differs from repository source')
    settings = (destination / 'workshop.txt').read_text(encoding='utf-8-sig')
    require('version=1\n' in settings and '\ntitle=' in settings and '\ndescription=' in settings, 'Incomplete workshop.txt')
    return {'result': 'PASS', 'folder': str(destination), 'mod_id': MOD_ID, 'version': fields['modversion'],
            'mod_files': len(files(packaged)), 'preview': preview(destination / 'preview.png'),
            'uploaded': False, 'note': 'File and structure validation only; the game performs its native validation before upload.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path.home() / 'Zomboid/Workshop' / NAME)
    parser.add_argument('--check', action='store_true', help='Only check an existing staging folder')
    args = parser.parse_args()
    destination = args.output.expanduser().resolve()
    if args.check:
        print(json.dumps(validate(destination), ensure_ascii=False, indent=2))
        return
    require(destination.parent.name == 'Workshop' and destination.name == NAME,
            'Output must end in Workshop/SuQingContainerUpgrade')
    require(not destination.exists(), 'Folder already exists. Preserve its workshop.txt and assigned ID; use --check or update deliberately.')
    require(info(SOURCE / '42/mod.info').get('id') == MOD_ID, 'Unexpected source mod ID')
    metadata = json.loads((PUBLISHING / 'workshop.json').read_text(encoding='utf-8'))
    require(metadata['visibility'] in {'public', 'friendsOnly', 'private', 'unlisted'}, 'Invalid visibility')
    description = (PUBLISHING / 'description.bbcode.txt').read_text(encoding='utf-8').strip()
    require(metadata['title'].strip() and description, 'Title and description must be nonempty')
    preview(PUBLISHING / 'preview.png')
    lines = ['version=1', 'title=' + metadata['title']]
    lines += ['description=' + line for line in description.splitlines()]
    lines += ['tags=' + ';'.join(metadata['tags']), 'visibility=' + metadata['visibility'], '']
    # No ID is invented. The game writes its Steam-assigned ID after the first upload.
    destination.mkdir(parents=True, exist_ok=False)
    shutil.copytree(SOURCE, destination / 'Contents/mods' / NAME)
    shutil.copy2(PUBLISHING / 'preview.png', destination / 'preview.png')
    shutil.copy2(PUBLISHING / 'changenote.txt', destination / 'changenote.txt')
    (destination / 'workshop.txt').write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    print(json.dumps(validate(destination), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
