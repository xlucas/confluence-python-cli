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
import xmlrpclib

from confluenceclient.api import exceptions as ex


class Proxy:
    def __init__(self, url):
        self.clients = {}
        self._imports = {}

        try:
            soap_url = "%s/rpc/xmlrpc" % url
            self.soap_client = xmlrpclib.Server(soap_url)
            self.token = None
        except xmlrpclib.Fault, e:
            raise ex.RPCException(e)

    def __getattr__(self, name):
        suffix_len = len(self.__class__.__name__.lower())
        modname = "%s.%s.client" % (self.__module__[:-(suffix_len + 1)], name)

        if name not in self.clients:
            __import__(modname)
            self._imports[name] = sys.modules[modname]
            client = getattr(self._imports[name], 'Client')(
                self.soap_client,
                self.token,
            )
            self.clients[name] = client

        return self.clients[name]
