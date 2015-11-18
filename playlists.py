#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime

from stations import getStations
from songs import getSongs

def getPlaylists(startDate, endDate):
    playlist = []

    dates = generateDatesBetween(startDate, endDate)
    stations = getStations()

    for station in stations:
        for date in dates:
            songs = getSongs(station, date)
            playlist.extend(songs)
            print('Fetched {} songs from {} ({})'.format(len(songs), station, date.strftime('%d-%m-%Y')))
            sys.stdout.flush()

    return playlist

def generateDatesBetween(start, end):
    current = start
    delta = datetime.timedelta(days=1)
    dates = [current]

    while current < end:
        current += delta
        dates.append(current)

    return dates

