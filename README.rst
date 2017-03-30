Confluence CLI
==============

::

    usage: confluence [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                      [-u <url>]
                      [--plugin.credentials.keyring | --plugin.credentials.volatile]
                      [--keyring-service <service>]
                      [--keyring-username <username>]
                      [--volatile-username <username>]
                      [--volatile-password <password>] [--plugin.export.pdf]
                      [--pdf-file <file>]

    Confluence Command-line Client.

    optional arguments:
      --version             show program's version number and exit
      -v, --verbose         Increase verbosity of output. Can be repeated.
      -q, --quiet           Suppress output except warnings and errors.
      --log-file LOG_FILE   Specify a file to log output. Disabled by default.
      -h, --help            Show help message and exit.
      --debug               Show tracebacks on errors.
      -u <url>, --url <url>
                            URL of the API
      --plugin.credentials.keyring
                            Enable keyring credentials plugin.
      --plugin.credentials.volatile
                            Enable volatile credentials plugin.
      --plugin.export.pdf   Enable pdf export plugin.

    Keyring credentials plugin:
      --keyring-service <service>
                            Service entry
      --keyring-username <username>
                            User name

    Volatile credentials plugin:
      --volatile-username <username>
                            User name
      --volatile-password <password>
                            User password

    Pdf export plugin:
      --pdf-file <file>     Output PDF file

    Commands:
      complete       print bash completion command
      group add
      group list
      group member add
      group member remove
      group remove
      help           print detailed help for another command
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
