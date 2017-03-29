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

    def create(self, name, fullname, email, password):
        self.soap_client.confluence2.addUser(
            self.token,
            {
                'name': name,
                'fullname': fullname,
                'email': email,
            },
            password,
        )

    def deactivate(self, name):
        self.soap_client.confluence2.deactivateUser(self.token, name)

    def delete(self, name):
        self.soap_client.confluence2.removeUser(self.token, name)

    def get(self, name):
        return self.soap_client.confluence2.getUser(self.token, name)

    def list_(self):
        return self.soap_client.confluence2.getActiveUsers(self.token, True)

    def reactivate(self, name):
        self.soap_client.confluence2.reactivateUser(self.token, name)

    def update(self, name, new_password):
        self.soap_client.confluence2.changeUserPassword(
            self.token,
            name,
            new_password,
        )
