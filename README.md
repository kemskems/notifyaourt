
notifyaourt
===========

**Notifyaourt** helps you to keep you updated of *your* important packages. This is particularly useful when you do not upgrade your Arch for a long time and you have so many updates that it is difficult to search for your important packages update information. **Notifyaourt** will notify you whether there are packages from *your* list of important packages that are upgraded, right after the upgrade process ends. You could then proceed to visit their websites to read their release notes, changelogs, etc.

How to Use
----------

 1. Make sure you have Python 3 and [yaourt][1] installed.
 2. Create ``.notifyaourt.conf`` file in your home directory. It is simply a [JSON][2] list of your important package. Sample can be found in `.notifyaourt.conf.sample` file.
 3. Download ``notifyaourt.py``.
 4. To upgrade your Arch, simply execute ``notifyaourt.py`` in any way you like.

  [1]: https://aur.archlinux.org/packages/yaourt/
  [2]: http://www.json.org/
