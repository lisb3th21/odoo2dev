# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Gestio de biblioteca',
    'version': '11.0.1.0.0',
    'author': 'Erica Poaquiza',
    'maintainer': 'Erica Poaquiza',
    'website': 'http://www.we_personal.com',
    'category': 'Services/Library',
    'summary': """
    Gestión del catalogo de libros de una biblioteca y  el prestamo de libros.""",
    'description': "Por hacer ",
    'depends': ['base'],
    'data': [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
    ],
    'images': ['static/description/banner.jpg'],
    'aplication': True,
}
