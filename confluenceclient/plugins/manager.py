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

import pkg_resources
import pkgutil
import sys


class PluginManager(object):
    def __init__(self, namespace):
        self.namespace = namespace
        self._load_plugins()

    def active_plugins(self, options):
        active = []
        for group in self.plugins:
            for plugin in self.plugins[group]:
                if getattr(options, "plugin.%s.%s" % (group, plugin.name)):
                    active.append(plugin)
        return active

    def build_option_parser(self, parser):
        for group in self.plugins:
            self._build_plugin_group_selection(group, parser)
            self._build_plugin_group_options(group, parser)

    def _import(self, name):
        __import__(name)
        return sys.modules[name]

    def _load_plugin_group(self, group, group_module):
        for _, modname, _ in pkgutil.iter_modules(group_module.__path__):
            plugin = self._import(
                "%s.%s.plugin" % (group_module.__name__, modname),
            )
            plugin.name = modname
            self.plugins[group].append(plugin)

    def _load_plugins(self):
        self.plugins = {}
        self.groups = {}
        for ep in pkg_resources.iter_entry_points(self.namespace):
            self.plugins[ep.name] = []
            group_module = self._import(ep.module_name)
            self.groups[ep.name] = group_module
            self._load_plugin_group(ep.name, group_module)

    def _build_plugin_group_options(self, group, parser):
        for plugin in self.plugins[group]:
            arg_group = parser.add_argument_group(
                "plugin.%s.%s" % (group, plugin.name)
            )
            getattr(plugin, 'build_option_parser')(arg_group)

    def _build_plugin_group_selection(self, group, parser):
        if getattr(self.groups[group], 'EXCLUSIVE'):
            parser = parser.add_mutually_exclusive_group()

        for plugin in self.plugins[group]:
            parser.add_argument(
                "--plugin.%s.%s" % (group, plugin.name),
                help="Enable %s plugin for %s." % (plugin.name, group),
                action="store_true",
            )
