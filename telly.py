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
"""Television Guide."""

import sys

import ptvg

log = ptvg.log


def getCreds(username):
    try:
        sdhostname = "schedulesdirect.org"
        CREDS = ptvg.credential.Credential(username, sdhostname)
        hpw = CREDS.getPassword()
        un = username
        if hpw is None:
            un = input("Schedules Direct Username: ")
            print("The password will be stored in your keyring.")
            pw = input("Schedules Direct password: ")
            if pw is not None:
                hpw = hashlib.sha1(pw.encode()).hexdigest()
                CREDS = ptvg.credential.Credential(un, sdhostname)
                CREDS.setPassword(hpw)
            else:
                raise Exception("No credentials supplied")
        return un, hpw
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


def telly(debug=False):
    try:
        cfgo = ptvg.config.Configuration(appname="ptvg")
        cfg = cfgo.config
        cfgun = cfg.get("username", "")
        un, pw = getCreds(cfgun)
        sd = ptvg.sdapi.SDApi(
            cfgun,
            pw,
            debug=debug,
            token=cfg.get("token", None),
            tokenexpires=cfg.get("tokenexpires", 0),
        )
        cfgo.writeConfig()
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        print(msg)
        raise


if __name__ == "__main__":
    telly()
