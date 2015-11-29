__author__ = "smbale"

import time
import json

DELAY=1

credentials = [
                '{"username":"t1@philips.com", "password":"SouthernCrown%6saffier"}',
                '{"username":"t2@philips.com", "password":"Crab8@zeeschelp"}',
                '{"username":"t3@philips.com", "password":"lentegroen2^Swan"}',
                '{"username":"t4@philips.com", "password":"8ShockingWaterBearer%"}',
              ]

fileout = 'records.csv'

from FHIR import *

cls = Philips_FHIR()

if not cls.get_token():
    cls.finish(1)

outfile=open(fileout, 'a')

for c in credentials:

    if not cls.login(c):
        cls.finish(1)

    if not cls.get_patient():
        cls.finish(1)

    if not cls.get_observation(next=False):
        cls.finish(1)

    while cls.get_observation():
        time.sleep(DELAY)
        continue

    for record in cls.records:
        record.update(cls.metadata)
        json.dump(record, outfile)
        outfile.write('\n')

    cls.logout()

    time.sleep(10)
