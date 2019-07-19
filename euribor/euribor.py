#!/bin/python
# API for ECB european central bank can be found here: https://sdw-wsrest.ecb.europa.eu/help/
# API URL with correct stream and series key: https://sdw-wsrest.ecb.europa.eu/service/data/FM/M.U2.EUR.RT.MM.EURIBOR6MD_.HSTA
# Add parameters like firstNObservations and lastNObservations

import smtplib
import requests
import xml.etree.ElementTree as ET


def get_euribor(url):
  num = requests.get(url)
  root = ET.fromstring(num.content)
  euribor_rate = root[1][0][2][1].attrib['value']
  euribor_date = root[1][0][2][0].attrib['value']
  print("Date: {}  Rate: {}".format(euribor_date, euribor_rate))


if __name__ == '__main__':
  url="https://sdw-wsrest.ecb.europa.eu/service/data/FM/M.U2.EUR.RT.MM.EURIBOR6MD_.HSTA?lastNObservations=1"
  get_euribor(url)
