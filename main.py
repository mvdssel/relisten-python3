#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import csv
from playlists import getPlaylists

# Settings
filename = 'playlists.csv'
endDate = datetime.datetime.today() # today
startDate = endDate - datetime.timedelta(days=1) # yesterday
# startDate = endDate.replace(day=1) # first day of month

# Get all the songs
playlists = getPlaylists(startDate, endDate)

# Get a file writer
csvFile = open(filename, 'w')
csvWriter = csv.DictWriter(
    csvFile,
    fieldnames=playlists[0].keys(),
    delimiter=';',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL
)

# Write all songs to the csv
for song in playlists:
    csvWriter.writerow(song)

print('Wrote results to ' + filename)
