##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Marlon Falcón Hernandez
#    (<http://www.ynext.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Gestio de biblioteca',
    'version': '0.1',
    'author': 'Erica Poaquiza',
    'maintainer': 'Ynext SpA',
    'website': 'http://www.we_personal.com',
    'license': 'AGPL-3',
    'category': 'Services/Library',
    'summary': """
    Gestión del catalogo de libros de una biblioteca y  el prestamo de libros.""",
    'description': "Por hacer ",
    'depends': ['base'],
    'data': [
        'views/library_menu.xml'
    ],
    'images': ['static/description/banner.jpg'],
}
