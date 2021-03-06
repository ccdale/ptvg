#!/usr/bin/env python3
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

"""ptvg update db script."""


import sys

import ptvg
from ptvg.config import Configuration
from ptvg.credential import Credential
from ptvg.db import SDDb
from ptvg.schedule import doUpdate
from ptvg.sdapi import SDApi


ptvg.log.setLevel(ptvg.logging.INFO)
log = ptvg.log


def begin():
    try:
        cfgo = Configuration(appname="ptvg")
        cfg = cfgo.config
        cfgun = cfg.get("username", "wibble")
        cfgtok = cfg.get("token", None)
        cfgtokexp = cfg.get("tokenexpires", 0)
        sdhostname = "schedulesdirect.org"
        CREDS = Credential(cfgun, sdhostname)
        hpw = CREDS.getPassword()
        # note, if you set debug to true
        # your hashed password and the current api token
        # will appear in the logs
        sd = SDApi(cfgun, hpw, debug=False, token=cfgtok, tokenexpires=cfgtokexp)
        return (sd, cfgo)
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        log.error(msg)
        sys.exit(1)


def update():
    try:
        log.info(f"ptvg version {ptvg.__version__} starting.")
        sd, cfgo = begin()
        sd.apiOnline()
        if not sd.online:
            raise Exception("Schedules Direct API is not online.")
        cfgo.update("token", sd.token)
        cfgo.update("tokenexpires", sd.tokenexpires)
        sdb = SDDb(appname=ptvg.tvappname)
        cfg = cfgo.config
        doUpdate(cfg, sd, sdb)
        cfgo.writeConfig()
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        log.error(msg)
        sys.exit(1)


if __name__ == "__main__":
    update()
