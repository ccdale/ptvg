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

import logging
import logging.handlers

from flask import Flask

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
syslog = logging.handlers.SysLogHandler(address="/dev/log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
syslog.setFormatter(formatter)
log.addHandler(syslog)

__version__ = "0.1.6"

tvapp = Flask(__name__)

from tvapp import routes
