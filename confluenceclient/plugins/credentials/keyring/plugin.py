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

import getpass
import keyring


def build_option_parser(parser):
    parser.add_argument(
        "--keyring-service",
        metavar="<service>",
        default="confluence-cli",
        help="Service entry",
    )
    parser.add_argument(
        "--keyring-username",
        metavar="<username>",
        help="User name",
    )


def after_command(app, cmd, result, error):
    pass


def before_command(app, cmd):
    pass


def initialize(app):
    _load_credentials(app, app.options)


def _load_credentials(app, options):
    app.username = options.keyring_username
    app.password = _get_or_save(options.keyring_service, app.username)


def _get_or_save(service, entry):
    value = keyring.get_password(service, entry)

    if value is None:
        value = getpass.getpass("Password to store: ")
        keyring.set_password(service, entry, value)

    return value
