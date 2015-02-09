# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from medical_family_details import Party
from enrollment_system import PartyPersonalDetails


def register():
    Pool.register(
        Party,
        PartyPersonalDetails,
        module='enrollment_system', type_='model'
    )
