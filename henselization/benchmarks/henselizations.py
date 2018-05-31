# -*- coding: utf-8 -*-
r"""
Benchmarks for construction and working with Henselizations.
"""
#*****************************************************************************
#       Copyright (C) 2018 Julian Rüth <julian.rueth@fsfe.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from __future__ import absolute_import
from sage.all import QQ

class Rational:
    r"""
    Creation of relatively trivial Henselizations.

    TESTS::

        sage: import henselization
        sage: from henselization.benchmarks.henselizations import Rational
        sage: Rational().time_create()

    """
    def time_create(self):
        QQ.henselization(2)
