# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .typified import *


def register():
    Pool.register(
        Category,
        Description,
        module='typified_description', type_='model')
