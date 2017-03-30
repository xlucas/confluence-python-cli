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

import pdfkit


def build_option_parser(parser):
    parser.add_argument(
        "--pdf-file",
        metavar="<file>",
        help="Output PDF file",
    )
    parser.add_argument(
        "--pdf-option",
        metavar="<key=value>",
        type=str,
        nargs='+',
        help="wkhtmltopdf render option",
    )


def after_command(app, cmd, result, error):
    if cmd.cmd_name == 'page render' and not error:
        options = {}
        for option in app.options.pdf_option:
            kv = option.split('=')
            options[kv[0]] = kv[1]
        html = result.encode('ascii', 'xmlcharrefreplace')
        pdfkit.from_string(html, app.options.pdf_file, options)


def before_command(app, cmd):
    pass


def initialize(app):
    pass
