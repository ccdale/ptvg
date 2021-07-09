# Copyright (c) 2021, Christopher Allison
#
#     This file is part of ptvg.
#
#     ptvg is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     ptvg is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with ptvg.  If not, see <http://www.gnu.org/licenses/>.

"""tests for ptvg application sdapi object"""

import pytest

import ptvg


@pytest.fixture
def setsdapi():
    cfgo = ptvg.config.Configuration(appname="ptvg")
    cfg = cfgo.config
    cfgun = cfg.get("username", "wibble")
    cfgtok = cfg.get("token", None)
    cfgtokexp = cfg.get("tokenexpires", 0)
    sdhostname = "schedulesdirect.org"
    CREDS = ptvg.credential.Credential(cfgun, sdhostname)
    hpw = CREDS.getPassword()
    # note, if you set debug to true
    # your hashed password and the current api token
    # will appear in the logs
    sd = ptvg.sdapi.SDApi(cfgun, hpw, debug=False, token=cfgtok, tokenexpires=cfgtokexp)
    return (sd, cfgo)


def test_config():
    cfgo = ptvg.config.Configuration(appname="ptvg")
    cfg = cfgo.config
    cfgun = cfg.get("username", "wibble")
    assert cfgun == "chrisallison"


def test_setup(setsdapi):
    wanted = [
        {
            "description": "List of countries which are available.",
            "type": "COUNTRIES",
            "uri": "/20141201/available/countries",
        },
        {
            "description": "List of language digraphs and their language names.",
            "type": "LANGUAGES",
            "uri": "/20141201/available/languages",
        },
        {
            "description": "List of satellites which are available.",
            "type": "DVB-S",
            "uri": "/20141201/available/dvb-s",
        },
        {
            "description": "List of Freeview transmitters in a country. Country options: GBR",
            "type": "DVB-T",
            "uri": "/20141201/transmitters/{ISO 3166-1 alpha-3}",
        },
    ]
    sd, cfgo = setsdapi
    avail = sd.available()
    assert avail == wanted


def test_apiOnline(setsdapi):
    sd, cfgo = setsdapi
    sd.apiOnline()
    cfgo.update("token", sd.token)
    cfgo.update("tokenexpires", sd.tokenexpires)
    cfgo.writeConfig()
    assert sd.online is True
