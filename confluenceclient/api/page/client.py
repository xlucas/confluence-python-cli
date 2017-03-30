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

    def get(self, space_key, name):
        return self.soap_client.confluence2.getPage(
            self.token,
            space_key,
            name,
        )

    def list_(self, space_key):
        return self.soap_client.confluence2.getPages(self.token, space_key)

    def remove(self, id_):
        self.soap_client.confluence2.removePage(self.token, id_)

    def render(self, id_):
        return self.soap_client.confluence2.renderContent(
            self.token,
            '',
            id_,
            '',
        )

    def store(self, space_key, parent_id, name, content):
        self.soap_client.confluence2.storePage(
            self.token, {
                'title': name,
                'content': content,
                'space': space_key,
                'parentId': parent_id,
            }
        )

    def add_label(self, label, id_):
        self.soap_client.confluence2.addLabelByName(self.token, label, id_)

    def delete_label(self, label, id_):
        self.soap_client.confluence2.removeLabelByName(
            self.token,
            label,
            id_,
        )
