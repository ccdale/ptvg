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

"""tests for ptvg application"""

from ptvg.config import Configuration
from ptvg import __version__


def test_version():
    assert __version__ == "0.1.2"


def test_config():
    cfgo = Configuration(appname="ptvg")
    cfg = cfgo.config
    cfgun = cfg.get("username", "wibble")
    assert cfgun == "chrisallison"
