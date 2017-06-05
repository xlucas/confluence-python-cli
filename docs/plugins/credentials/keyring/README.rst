Keyring plugin
==============

Description
-----------

This plugin adds the possibility to read your user password from a local
keyring so that you don't provide such information in plain text.

Activation
----------

Provide the `--plugin.credentials.keyring` option to the CLI.

Options
-------

+--------------------+----------------------------+----------+------------------+
| Option             | Description                | Required | Default          |
+====================+============================+==========+==================+
| --keyring-service  | Service name to use when   | No       | "confluence-cli" |
|                    | looking up a keyring entry |          |                  |
+--------------------+----------------------------+----------+------------------+
| --keyring-username | User name to use when      | Yes      | `-`              |
|                    | looking up a keyring entry |          |                  |
+--------------------+----------------------------+----------+------------------+
