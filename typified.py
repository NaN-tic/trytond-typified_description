#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['Category', 'Description']


class Category(ModelSQL, ModelView):
    'Typfied Description Category'
    __name__ = 'typified.description.category'

    name = fields.Char('Name', translate=True, required=True)


class Description(ModelSQL, ModelView):
    'Typified Description'
    __name__ = 'typified.description'

    name = fields.Char('Name', translate=True, required=True)
    category = fields.Many2One('typified.description.category', 'Category',
        select=True)
    description = fields.Text('Description', translate=True, required=True)
