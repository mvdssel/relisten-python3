#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request

homePage = 'https://relisten.be'
stationIdentifierRegexp = re.compile('data-stationurl="([^"]+)"')

def getStations():
    response = urllib.request.urlopen(homePage)
    html = str(response.read())
    return stationIdentifierRegexp.findall(html)
