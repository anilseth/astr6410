# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Need observer location, time, and object defined.

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import EarthLocation
from pytz import timezone
from astroplan import Observer
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astroplan import FixedTarget
from astroplan.plots import plot_airmass
from astroplan.plots import plot_sky
import numpy as np

latitude = '+40d45m31.3236s'
longitude='-111d52m34.2588s'
elevation = 1288 * u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)
slc = Observer(name='SLC', location=location, timezone=timezone('US/Mountain'))


time=Time('2020-01-18 03:00:00')

betelgeuse = FixedTarget.from_name('Betelgeuse')
sirius=FixedTarget.from_name('Sirius')
plot_airmass(betelgeuse, slc, time, brightness_shading=True, altitude_yaxis=True)
plot_airmass(sirius, slc, time, brightness_shading=True, altitude_yaxis=True)
plt.show()

manytimes=time + np.linspace(-3, 9, 13)*u.hour
plot_sky(betelgeuse, slc, manytimes, north_to_east_ccw=False)
plot_sky(sirius, slc, manytimes, north_to_east_ccw=False)
plt.show()
