# -*- coding: utf-8 -*-
"""
    enrollment_system.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta


__all__ = ['PartyPersonalDetails']
__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active'),
}
DEPENDS = ['active']


class PartyPersonalDetails:
    "Party"
    __name__ = "party.party"

    gender = fields.Selection([
        ('male', 'M'),
        ('female', 'F'),
        ('undefined', 'N/A'),
        ], 'Gender', required=True,
        states=STATES, depends=DEPENDS
    )

    dob = fields.Date(
        "Date of Birth", required=True, states=STATES, depends=DEPENDS
    )

    pan_number = fields.Char(
        "pan_number", size=10, required=True, states=STATES, depends=DEPENDS
    )

    passport = fields.Char(
        "Passport_Number", size=9, states=STATES,
        depends=DEPENDS, select=True
    )

    birthplace = fields.Char(
        "Birth_Place", required=True, states=STATES, depends=DEPENDS
    )
    bloodgroup = fields.Char(
        "Blood_Group", states=STATES, depends=DEPENDS
    )
    age = fields.Numeric(
        "Age", states=STATES, depends=DEPENDS
    )
    hobbies = fields.Text(
        "Hobbies", states=STATES, depends=DEPENDS
    )
    nationality = fields.Char(
        "Nationality", states=STATES, depends=DEPENDS
    )
    height = fields.Numeric(
        "Height", states=STATES, depends=DEPENDS
    )
    weight = fields.Numeric(
        "Weight", states=STATES, depends=DEPENDS
    )
    identificationmark = fields.Char(
        "Identification_Mark", states=STATES, depends=DEPENDS
    )
    maritalstatus = fields.Selection([
        ('YES', 'y'),
        ('NO', 'n'),
        ('undefined', 'N/A'),
        ], 'Maritial Status', states=STATES, depends=DEPENDS
    )

    @staticmethod
    def default_gender():
        return 'male'

    @staticmethod
    def default_nationality():
        return 'India'
