# Copyright (C) 2017  Xavier Lucas
# Copyright (C) 2013  Remy van Elst
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


class Client(object):
    def __init__(self, soap_client, token):
        self.soap_client = soap_client
        self.token = token

    def create(self, key, name):
        self.soap_client.confluence2.addSpace(
            self.token, {
                'key': key,
                'name': name,
            }
        )

    def delete(self, key):
        self.soap_client.confluence2.removeSpace(self.token, key)

    def get(self, key):
        return self.soap_client.confluence2.getSpace(self.token, key)

    def list(self):
        return self.soap_client.confluence2.getSpaces(self.token)
