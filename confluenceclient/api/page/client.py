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

    def list(self, space_key):
        return self.soap_client.confluence2.getPages(self.token, space_key)

    def remove(self, _id):
        self.soap_client.confluence2.removePage(self.token, _id)

    def render(self, space_key, page_id, page_content, style):
        return self.soap_client.confluence2.renderContent(
            self.token,
            space_key,
            page_id,
            page_content,
            {'style': style},
        )

    def add_label(self, label, page_id):
        self.soap_client.confluence2.addLabelByName(self.token, label, page_id)

    def delete_label(self, label, page_id):
        self.soap_client.confluence2.removeLabelByName(
            self.token,
            label,
            page_id,
        )
