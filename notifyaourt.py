from subprocess import call, Popen, PIPE

def get_version(pkgs):
    """Get the current version of packages"""
    pkg_map = {}
    for pkg in pkgs:
        yaourt_proc = Popen(['yaourt', '-Qi', pkg], stdout=PIPE)
        grep_proc = Popen(['grep', 'Version'], stdin=yaourt_proc.stdout,
            stdout=PIPE)
        out, err = grep_proc.communicate()
        ver = str(out, encoding='utf-8').split()[2]
        pkg_map[pkg] = ver
    return pkg_map

packages = ['git']
curr_version = get_version(packages)
call(['yaourt', '-Syua'])
new_version = get_version(packages)
for pkg in packages:
    if curr_version[pkg] != new_version[pkg]:
        print(pkg, 'has been updated!')