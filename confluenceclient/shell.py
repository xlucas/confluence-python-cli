# Copyright (C) 2017  Xavier Lucas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import confluenceclient
import sys

from confluenceclient.plugins.manager import PluginManager
from confluenceclient.api.proxy import Proxy
from cliff.app import App
from cliff.commandmanager import CommandManager


class ConfluenceClient(App):
    """Confluence Command-line Client."""

    def __init__(self):
        self.plugin_manager = PluginManager('confluence.cli.plugins')

        super(ConfluenceClient, self).__init__(
            description=self.__doc__,
            version=confluenceclient.__version__,
            command_manager=CommandManager('confluence.cli'),
            deferred_help=True,
        )

    def build_option_parser(self, description, version):
        parser = super(ConfluenceClient, self).build_option_parser(
            description,
            version,
        )
        parser.add_argument(
            "-u",
            "--url",
            metavar="<url>",
            help="URL of the API",
        )

        self.plugin_manager.build_option_parser(parser)

        return parser

    def clean_up(self, cmd, result, error):
        for plugin in self.plugin_manager.active_plugins(self.options):
            getattr(plugin, 'after_command')(self, cmd, result, error)

    def initialize_app(self, argv):
        if self.options.deferred_help:
            return

        for plugin in self.plugin_manager.active_plugins(self.options):
            getattr(plugin, 'initialize')(self)

        # Authenticate
        self.proxy = Proxy(self.options.url)
        self.proxy.token = self.proxy.auth.login(self.username, self.password)

    def prepare_to_run_command(self, cmd):
        for plugin in self.plugin_manager.active_plugins(self.options):
            getattr(plugin, 'before_command')(self, cmd)


def main(argv=sys.argv[1:]):
    result = ConfluenceClient().run(argv)
    if isinstance(result, unicode):
        result = result.encode('utf-8')
    if isinstance(result, str):
        sys.stdout.write(result)
    else:
        return result


if __name__ == '__main__':
    sys.exit(main())
