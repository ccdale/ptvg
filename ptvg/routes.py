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

"""ptvg routes module."""

import sys

from flask import render_template

import ptvg
from ptvg import tvapp
from ptvg.web import channelList

log = ptvg.log


@tvapp.route("/")
def index():
    try:
        chans = channelList()
        return render_template("index.html", title="Home", chans=chans)
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        log.error(msg)
        raise


@tvapp.route("/channel/<channelid>")
def channel(channelid):
    try:
        chans = channelList()
        for chan in chans:
            if chan["stationid"] == channelid:
                channame = chan["name"]
                break
        return render_template("index.html", title=channame, chans=chans)
    except Exception as e:
        exci = sys.exc_info()[2]
        lineno = exci.tb_lineno
        fname = exci.tb_frame.f_code.co_name
        ename = type(e).__name__
        msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
        log.error(msg)
        raise
