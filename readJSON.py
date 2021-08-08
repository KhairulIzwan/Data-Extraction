#!/usr/bin/env python

# Title		: Python program to read json file
# Author	: shafikah(nurshafikah.darwis@intel.com)
# -------------------------------------------------

import argparse
import json
import os

#from itertools import groupby
#import sys
#import csv

#from datetime import datetime

os.system('clear')

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
	help="path to input data")
args = vars(ap.parse_args())

# Opening JSON file
f = open(args["file"],)

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['output']:
	print(i)
#	print(i['name'])
#	print(i['dimensions'])
#	print(i['values'][0])
	print(i['count'])
#	print(i['name'])

##print(type(data))
#d = data['emp_details']
#print(d[0]['name'])

# Closing file
f.close()

