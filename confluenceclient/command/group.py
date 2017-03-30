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

from confluenceclient import formatter
from cliff.command import Command
from cliff.lister import Lister


class GroupCommand(Command):
    def get_parser(self, prog_name):
        parser = super(GroupCommand, self).get_parser(prog_name)
        parser.add_argument(
            "name",
            metavar="<name>",
            help="Group name",
        )
        return parser


class GroupMemberCommand(GroupCommand):
    def get_parser(self, prog_name):
        parser = super(GroupMemberCommand, self).get_parser(prog_name)
        parser.add_argument(
            "user",
            metavar="<user>",
            help="User name",
        )
        return parser


class Add(GroupCommand):
    def take_action(self, parsed_args):
        self.app.proxy.group.create(parsed_args.name)


class List(Lister):
    def get_parser(self, prog_name):
        parser = super(Lister, self).get_parser(prog_name)
        parser.add_argument(
            "--user",
            metavar="<user>",
            help="User name",
        )
        return parser

    def take_action(self, parsed_args):
        return formatter.table(self.app.proxy.group.list_(parsed_args.user))


class Remove(GroupCommand):
    def get_parser(self, prog_name):
        parser = super(Lister, self).get_parser(prog_name)
        parser.add_argument(
            "--dest-group",
            metavar="<name>",
            default='confluence-users',
            help="Group to move users to",
        )
        return parser

    def take_action(self, parsed_args):
        self.app.proxy.group.delete(parsed_args.name, parsed_args.dest_group)


class MemberAdd(GroupMemberCommand):
    def take_action(self, parsed_args):
        self.app.proxy.group.add_member(parsed_args.name, parsed_args.user)


class MemberRemove(GroupMemberCommand):
    def take_action(self, parsed_args):
        self.app.proxy.group.remove_member(parsed_args.name, parsed_args.user)
