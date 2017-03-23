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


class SpaceCommand(Command):
    def get_parser(self, prog_name):
        parser = super(SpaceCommand, self).get_parser(prog_name)
        parser.add_argument(
            "key",
            metavar="<key>",
            help="Space key",
        )
        return parser


class Add(SpaceCommand):
    def take_action(self, parsed_args):
        pass


class List(Command):
    def take_action(self, parsed_args):
        pass


class Remove(SpaceCommand):
    def take_action(self, parsed_args):
        pass
