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


def entry(json):
    sorted_kv = sorted(json.items(), key=lambda t: t[0])
    headers = map(lambda t: t[0].capitalize(), sorted_kv)
    rows = map(lambda t: t[1], sorted_kv)
    return (headers, rows)


def table(json, sort_field=None):
    headers = []
    rows = []
    if sort_field:
        json = sorted(json, key=lambda t: t[sort_field.lower()].lower())
    for entry in json:
        sorted_kv = sorted(entry.items(), key=lambda t: t[0])
        sorted_v = map(lambda t: t[1], sorted_kv)
        rows.append(sorted_v)
        if not headers:
            headers = map(lambda t: t[0].capitalize(), sorted_kv)
    return (headers, rows)
