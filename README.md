
pacnotif
========

**Pacnotif** helps you to keep you updated of *your* important packages. This is particularly useful when you do not upgrade your Arch for a long time and you have so many updates that it is difficult to search for your important packages update information. **Pacnotif** will notify you whether there are packages from *your* list of important packages that are upgraded, right after the upgrade process ends. You could then proceed to visit their websites to read their release notes, changelogs, etc.

How to Use
----------

 1. Make sure you have Python 3 installed.
 2. Create ``.pacnotif.conf`` file in your home directory. It is simply a [JSON][1] list of your important package. Sample can be found in `.pacnotif.conf.sample` file.
 3. Download ``pacnotif.py``.
 4. To upgrade your Arch, simply execute ``pacnotif.py`` in any way you like. See ``pacnotif.py -h`` for more details.

  [1]: http://www.json.org/
