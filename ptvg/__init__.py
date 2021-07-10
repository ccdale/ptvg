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

"""The Personal TV Guide Application."""

import datetime
import logging
import logging.handlers

from flask import Flask

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
syslog = logging.handlers.SysLogHandler(address="/dev/log")
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
syslog.setFormatter(formatter)
log.addHandler(syslog)

__version__ = "0.1.10"

tvapp = Flask(__name__)
tvappname = "ptvg"

from ptvg import routes


def getTimeStamp(dt, dtformat="%Y-%m-%dT%H:%M:%SZ"):
    """Returns the integer epoch timestamp for the date time described by dt."""
    try:
        return int(datetime.datetime.strptime(dt, dtformat).timestamp())
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        log.error(msg)
        raise


def showJson(jresp):
    """Pretty print json responses."""
    try:
        print(json.dumps(jresp, indent=4, sort_keys=True), end="\n\n", flush=True)
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        # print(msg)
        log.error(msg)
        raise
