{
    'name': "My library",
    'summary': "Manage books easily",
    'description': """ 
         Manage Library
         ==============
         Description related to library.
     """,
    'author': "Gilberto S.B:",
    'website': "http://www.odoo.isumit.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml'
    ],
    'application': True,
}