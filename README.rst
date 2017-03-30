Confluence CLI
==============

A python command-line interface for Confluence.


Commands
--------

The following commands are available :

::

    Commands:
      group add
      group list
      group member add
      group member remove
      group remove
      page add
      page content
      page copy
      page info
      page label add
      page label remove
      page list
      page remove
      page render
      page update
      space add
      space list
      space remove
      user add
      user deactivate
      user info
      user list
      user reactivate
      user remove
      user update

Plugins
-------

Confluence CLI is really easy to extend and natively uses a plugin system to
add some extra features.

It comes with the following plugins:

+----------+-------------+--------------------------------------------------+
| Plugin   | Group       | Description                                      |
+==========+=============+==================================================+
| Keyring  | Credentials | Secure credentials handling using user-preferred |
|          |             | keyring to store secrets.                        |
+----------+-------------+--------------------------------------------------+
| Volatile | Credentials | Unsafe credentials handling using clear text     |
|          |             | options from the command line.                   |
+----------+-------------+--------------------------------------------------+
| PDF      | Export      | Convert rendered HTML page to a PDF file.        |
+----------+-------------+--------------------------------------------------+
