#!/usr/bin/python
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate EV difference between photos')
parser.add_argument('-e', required=True, type=str, metavar='exp', help='Comma-separated list of exposures in seconds as numbers, decimals or fractions, without spaces, e.g. "2,0.5,1/100"')
parser.add_argument('-a', required=True, type=str, metavar='aper', help='Comma-separated list of apertures, without spaces, e.g. "2,3.5,8"')

args = parser.parse_args()

exposures = args.e.split(',')
apertures = [float(i) for i in args.a.split(',')]

if len(exposures) != len(apertures):
    raise Exception("{} exposures and {} apertures given".format(len(exposures), len(apertures)))

for index, item in enumerate(exposures):
    if item.find('/') > -1:
        exposures[index] = float(item.split('/')[0])/float(item.split('/')[1])
    else:
        exposures[index] = float(item)

ev=[]
for i in range(len(apertures)):
    ev.append(math.log(apertures[i]**2.0/exposures[i],2))
    print "EV at exposure {} F {} is {}".format(exposures[i], apertures[i], ev[i])
    if i==0: continue
    print "Difference from previous EV: {}".format(ev[i] - ev[i-1])
