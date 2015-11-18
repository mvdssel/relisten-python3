#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request

baseUrl = 'https://relisten.be/playlists';

titleRegexp = re.compile('itemprop="name">([^<]+)</span>')
artistRegexp = re.compile('itemprop="byArtist">([^<]+)</span>')
playtimeRegexp = re.compile('class="pull-right">(\\d\\d):(\\d\\d)</small>')

def getSongs(station, date):
    url = generateUrl(station, date)
    response = urllib.request.urlopen(url)
    html = str(response.read())
    return extractSongs(station, date, html)

def extractSongs(station, date, html):
    songs = []

    titles = re.findall(titleRegexp, html)
    artists = re.findall(artistRegexp, html)
    playtimes = re.findall(playtimeRegexp, html)

    for i, title in enumerate(titles):

        # create playtime based on date and time
        playtime = date.replace(
            hour = int(playtimes[i][0]),
            minute = int(playtimes[i][1]),
            second = 0,
            microsecond = 0
        )

        songs.append({
            'title': title,
            'artist': artists[i],
            'playtime': playtime,
            'station': station
        })
    return songs

def generateUrl(station, date):
    formattedDate = date.strftime('%d-%m-%Y')
    return '%s/%s/%s.html' % (baseUrl, station, formattedDate)
