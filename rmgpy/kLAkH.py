#!/usr/bin/env python3

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2021 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

"""
This module contains the LiquidVolumetricMassTransferCoefficientData class and HenryLawConstantData class for storing sampled kLA and kH properties.
"""

from rmgpy.rmgobject import RMGObject


class LiquidVolumetricMassTransferCoefficientData(RMGObject):
    """
    A set of transport properties.
    
    The attributes are:
    =================  ============================================================
    Attribute          Description
    =================  ============================================================
    `Ts`        		Sampled temperatures
    `kLAs`           	Liquid volumetric mass transfer coefficients corresponding to Ts
    =================  ============================================================
    
    """

    def __init__(self, Ts=[], kLAs=[]):
        self.Ts = Ts
        self.kLAs = kLAs

    def __repr__(self):
        """
        Return a string representation that can be used to reconstruct the
        LiquidVolumetricMassTransferCoefficientData object.
        """
        attributes = []
        if self.Ts:
            attributes.append(f'Ts={self.Ts}')
        if self.kLAs:
            attributes.append(f'kLAs={self.kLAs}')
        string = 'LiquidVolumetricMassTransferCoefficientData({0!s})'.format(', '.join(attributes))
        return string

class HenryLawConstantData(RMGObject):
    """
    A set of transport properties.
    
    The attributes are:
    =================  ============================================================
    Attribute          Description
    =================  ============================================================
    `Ts`        		Sampled temperatures
    `kHs`           	Henry's law constants corresponding to Ts
    =================  ============================================================
    
    """

    def __init__(self, Ts=[], kHs=[]):
        self.Ts = Ts
        self.kHs = kHs

    def __repr__(self):
        """
        Return a string representation that can be used to reconstruct the
        HenryLawConstantData object.
        """
        attributes = []
        if self.Ts:
            attributes.append(f'Ts={self.Ts}')
        if self.kHs:
            attributes.append(f'kHs={self.kHs}')
        string = 'HenryLawConstantData({0!s})'.format(', '.join(attributes))
        return string

class liquidVolumetricMassTransferCoefficientPowerLaw(RMGObject):
    def __init__(self, prefactor=0, diffusion_coefficient_power=0, solvent_viscosity_power=0, solvent_density_power=0):
        self.prefactor = prefactor
        self.diffusion_coefficient_power = diffusion_coefficient_power
        self.solvent_viscosity_power = solvent_viscosity_power
        self.solvent_density_power = solvent_density_power