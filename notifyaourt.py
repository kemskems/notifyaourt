#!/usr/bin/env python3


import os
import os.path
import json
import subprocess
import argparse


VERSION_KEY = 'Version'
URL_KEY = 'URL'


def get_info(pkgs):
    """Get the current info of a list of packages"""
    pkg_map = {}
    for pkg in pkgs:
        yaourt_proc = subprocess.Popen(['pacman', '-Qi', pkg],
                                       stdout=subprocess.PIPE)
        pattern = VERSION_KEY + '|' + URL_KEY
        grep_proc = subprocess.Popen(['grep', '-E', pattern],
                                     stdin=yaourt_proc.stdout,
                                     stdout=subprocess.PIPE)
        out, err = grep_proc.communicate()
        sout = str(out, encoding='utf-8')
        info_map = {u.split()[0]: u.split()[2]
                    for u in sout.split('\n')
                    if len(u) > 0}
        pkg_map[pkg] = info_map
    return pkg_map


def get_packages():
    """Get the user-defined important list of packages

    List of packages are stored as JSON file in $HOME/.notifyaourt.conf

    """
    home_dir = os.environ['HOME']
    config_file = os.path.join(home_dir, '.notifyaourt.conf')
    if os.path.exists(config_file):
        lines = ""
        with open(config_file) as conf:
            for line in conf:
                lines += line
        return json.loads(lines)
    else:
        return []


parser = argparse.ArgumentParser(description='Simple notifier for Arch Linux \
                                package update')
parser.add_argument('command', help='Command to update packages')
parser.add_argument('flags', nargs=argparse.REMAINDER,
                    help='Flags to be passed to command')
args = parser.parse_args()


packages = get_packages()
old_info = get_info(packages)
update_command = args.flags
update_command.insert(0, args.command)
subprocess.call(update_command)
new_info = get_info(packages)
updated_packages = []
for pkg in packages:
    if old_info[pkg][VERSION_KEY] != new_info[pkg][VERSION_KEY]:
        updated_packages.append(pkg)

print()
if len(updated_packages) == 0:
    print('No important package updates')
else:
    print('Important package updates:')
    for cnt, pkg in enumerate(updated_packages, start=1):
        old_ver = old_info[pkg][VERSION_KEY]
        new_ver = new_info[pkg][VERSION_KEY]
        url = new_info[pkg][URL_KEY]
        print(cnt, ')', pkg, old_ver, '=>', new_ver, '|', url)