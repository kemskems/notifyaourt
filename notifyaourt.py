import os
import os.path
import json
from subprocess import call, Popen, PIPE

def get_version(pkgs):
    """Get the current version from a list of packages"""
    pkg_map = {}
    for pkg in pkgs:
        yaourt_proc = Popen(['yaourt', '-Qi', pkg], stdout=PIPE)
        grep_proc = Popen(['grep', 'Version'], stdin=yaourt_proc.stdout,
            stdout=PIPE)
        out, err = grep_proc.communicate()
        ver = str(out, encoding='utf-8').split()[2]
        pkg_map[pkg] = ver
    return pkg_map

def get_packages():
    """Get the user-defined important list of packages"""
    home_dir = os.environ['HOME']
    config_file = os.path.join(home_dir, '.notifyaourt.conf')
    lines = ""
    with open(config_file) as conf:
        for line in conf:
            lines += line
    return json.loads(lines)

packages = get_packages()
curr_version = get_version(packages)
call(['yaourt', '-Syua'])
new_version = get_version(packages)
for pkg in packages:
    if curr_version[pkg] != new_version[pkg]:
        print(pkg, 'has been updated!')