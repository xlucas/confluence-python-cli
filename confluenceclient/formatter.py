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

import operator

tuple_key = operator.itemgetter(0)
tuple_val = operator.itemgetter(1)


def entry(json):
    sorted_kv = sorted(json.items(), key=tuple_key)
    headers = map(lambda t: tuple_key(t).capitalize(), sorted_kv)
    rows = map(tuple_val, sorted_kv)
    return (headers, rows)


def table(json, sort_field=None):
    headers = []
    rows = []
    if sort_field:
        json = sorted(json, key=lambda t: t[sort_field.lower()].lower())
    for entry in json:
        sorted_kv = sorted(entry.items(), key=tuple_key)
        sorted_v = map(tuple_val, sorted_kv)
        rows.append(sorted_v)
        if not headers:
            headers = map(lambda t: tuple_key(t).capitalize(), sorted_kv)
    return (headers, rows)
