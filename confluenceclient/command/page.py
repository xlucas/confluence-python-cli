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

import sys

from confluenceclient import formatter
from confluenceclient.command.common.lister import OrderedLister
from cliff.command import Command
from cliff.show import ShowOne


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


class PageLabelCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageCommand, self).get_parser(prog_name)
        parser.add_argument(
            "--label",
            metavar="<name>",
            help="Label name",
            required=True,
        )
        return parser


class PageMetaCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageMetaCommand, self).get_parser(prog_name)
        parser.add_argument(
            "--label",
            metavar="<label>",
            help="Page label",
            default="generated_with_api",
        )
        return parser


class PageSourceCommand(Command):
    def get_parser(self, prog_name):
        parser = super(PageSourceCommand, self).get_parser(prog_name)
        source = parser.add_mutually_exclusive_group()
        source.add_argument(
            "--in-file",
            metavar="<file>",
            help="File to read content from",
        )
        source.add_argument(
            "--stdin",
            help="Read content from stdin",
            action='store_true',
        )
        return parser

    def read_source(self, parsed_args):
        if hasattr(parsed_args, 'file'):
            return open(parsed_args.in_file, 'rb').read()
        if parsed_args.stdin:
            return sys.stdin.read()


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
        self.app.proxy.page.store(
            parsed_args.space,
            parsed_args.parent,
            parsed_args.name,
            self.read_source(parsed_args),
        )


class Content(PageCommand):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        return page['content']


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
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.origin)
        self.app.proxy.page.store(
            page['space'],
            page['parentId'],
            parsed_args.name,
            page['content'],
        )


class Info(PageCommand, ShowOne):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        del (page['content'])
        return formatter.entry(page)


class List(OrderedLister):
    def get_parser(self, prog_name):
        parser = super(List, self).get_parser(prog_name)
        parser.add_argument(
            "--space",
            metavar="<key>",
            help="Space key",
            required=True,
        )
        return parser

    def take_action(self, parsed_args):
        return formatter.table(
            self.app.proxy.page.list_(parsed_args.space),
            parsed_args.order_by,
        )


class Remove(PageCommand):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        self.app.proxy.page.remove(page['id'])


class Render(PageCommand):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        return self.app.proxy.page.render(page['id'])


class Update(PageCommand, PageMetaCommand, PageSourceCommand, PageTreeCommand):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        self.app.proxy.page.store(
            page['space'],
            page['parentId'],
            page['title'],
            self.read_source(parsed_args),
        )


class LabelAdd(PageCommand, PageLabelCommand):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        self.app.proxy.page.add_label(parsed_args.label, page['id'])


class LabelRemove(PageCommand, PageLabelCommand):
    def take_action(self, parsed_args):
        page = self.app.proxy.page.get(parsed_args.space, parsed_args.name)
        self.app.proxy.page.delete_label(parsed_args.label, page['id'])
