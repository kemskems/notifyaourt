
notifyaourt
===========

**Notifyaourt** helps you to find whether your important Arch Linux packages are updated. This is useful when you do not upgrade your Arch for a long time and you have so many updates that it is difficult to search for your important packages update information.

How to Use
----------

 1. Make sure you have [yaourt][1] installed.
 2. Create ``.notifyaourt.conf`` file in your home directory. It is simply a [JSON][2] list of your important package.
 3. Download ``notifyaourt.py``.
 4. To upgrade your Arch, simply execute ``notifyaourt.py`` in any way you like.

  [1]: https://aur.archlinux.org/packages/yaourt/
  [2]: http://www.json.org/
