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

from cliff.app import App
from cliff.commandmanager import CommandManager


class ConfluenceClient(App):
    """Confluence Command-line Client."""

    def __init__(self):
        super(ConfluenceClient, self).__init__(
            description=self.__doc__,
            version=confluenceclient.__version__,
            command_manager=CommandManager('confluence.cli'),
            deferred_help=True
        )

    def initialize_app(self, argv):
        pass

    def build_option_parser(self, description, version):
        parser = super(ConfluenceClient, self).build_option_parser(
            description,
            version,
        )
        parser.add_argument(
            "-s",
            "--server",
            metavar="<server>",
            help="Server name",
        )
        parser.add_argument(
            "-u",
            "--username",
            metavar="<username>",
            help="User name",
        )
        parser.add_argument(
            "-p",
            "--password",
            metavar="<password>",
            help="User password",
        )
        parser.add_argument(
            "-k",
            "--keyring",
            help="Use keyring",
            action='store_true',
        )
        return parser


def main(argv=sys.argv[1:]):
    return ConfluenceClient().run(argv)


if __name__ == '__main__':
    sys.exit(main())
