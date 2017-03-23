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


class PageCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageCommand, self).get_parser(prog_name)
        parser.add_argument(
            "--space",
            metavar="<key>",
            help="Space key",
            required=True,
        )
        parser.add_argument(
            "name",
            metavar="<name>",
            help="Page name",
        )
        return parser


class PageMetaCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageMetaCommand, self).get_parser(prog_name)
        parser.add_argument(
            "--label",
            metavar="<label>",
            help="Page label",
            default="created_via_api",
        )
        return parser


class PageSourceCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageSourceCommand, self).get_parser(prog_name)
        source = parser.add_mutually_exclusive_group()
        source.add_argument(
            "--file",
            metavar="<file>",
            help="File to read content from",
        )
        source.add_argument(
            "--stdin",
            help="Read content from stdin",
            action='store_true',
        )
        return parser


class PageTreeCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageTreeCommand, self).get_parser(prog_name)
        parser.add_argument(
            "parent",
            metavar="<parent>",
            help="Parent page ID",
            default="0",
        )
        return parser


class Add(PageCommand, PageMetaCommand, PageSourceCommand, PageTreeCommand):
    def take_action(self, parsed_args):
        pass


class Content(PageCommand):
    def take_action(self, parsed_args):
        pass


class Copy(PageCommand, PageMetaCommand, PageSourceCommand, PageTreeCommand):
    def get_parser(self, prog_name):
        parser = super(Copy, self).get_parser(prog_name)
        parser.add_argument(
            "--origin",
            metavar="<origin>",
            help="Origin page name",
            required=True,
        )
        return parser

    def take_action(self, parsed_args):
        pass


class Crawl(Command):
    def take_action(self, parsed_args):
        pass


class List(Command):
    def take_action(self, parsed_args):
        pass


class Remove(PageCommand):
    def take_action(self, parsed_args):
        pass


class Summary(PageCommand):
    def get_parser(self, prog_name):
        parser = super(Summary, self).get_parser(prog_name)
        parser.add_argument(
            "--delimiter",
            metavar="<delimiter>",
            help="Field delimiter",
            default=", ",
        )
        return parser

    def take_action(self, parsed_args):
        pass


class Update(PageCommand, PageMetaCommand, PageSourceCommand, PageTreeCommand):
    def take_action(self, parsed_args):
        pass
