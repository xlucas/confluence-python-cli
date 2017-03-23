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

from cliff.command import Command


class UserCommand(Command):
    def get_parser(self, prog_name):
        parser = super(UserCommand, self).get_parser(prog_name)
        parser.add_argument(
            "name",
            metavar="<name>",
            help="User name",
        )
        return parser


class Add(UserCommand):
    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument(
            "--fullname",
            metavar="<fullname>",
            help="New user full name",
            required=True,
        )
        parser.add_argument(
            "--email",
            metavar="<email>",
            help="New user email address",
            required=True,
        )
        parser.add_argument(
            "--password",
            metavar="<password>",
            help="New user password",
            required=True,
        )
        return parser

    def take_action(self, parsed_args):
        pass


class Deactivate(UserCommand):
    def take_action(self, parsed_args):
        pass


class Info(UserCommand):
    def take_action(self, parsed_args):
        pass


class List(Command):
    def take_action(self, parsed_args):
        pass


class Reactivate(UserCommand):
    def take_action(self, parsed_args):
        pass


class Remove(UserCommand):
    def take_action(self, parsed_args):
        pass


class Update(UserCommand):
    def get_parser(self, prog_name):
        parser = super(Update, self).get_parser(prog_name)
        parser.add_argument(
            "--password",
            metavar="<password>",
            help="User new password",
            required=True,
        )
        return parser

    def take_action(self, parsed_args):
        pass
