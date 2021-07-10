#!/usr/bin/env python3

import sys

import ptvg
from ptvg.config import Configuration
from ptvg.credential import Credential
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
            raise Exception("Schedules Direct is not online.")
        log.info("Schedules Direct API is online.")
        cfgo.update("token", sd.token)
        cfgo.update("tokenexpires", sd.tokenexpires)
        cfgo.writeConfig()
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        log.error(msg)
        sys.exit(1)
