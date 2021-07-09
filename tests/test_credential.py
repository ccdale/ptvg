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

"""tests for ptvg application credential object"""

from ptvg.credential import Credential


def test_creds_not_exist():
    un = "wibble"
    host = "fictitious.host"
    CREDS = Credential(un, host)
    hpw = CREDS.getPassword()
    assert hpw is None


def test_creds_create():
    un = "wibble"
    host = "fictitious.host"
    CREDS = Credential(un, host)
    CREDS.setPassword(password="hotticket")
    hpw = CREDS.getPassword()
    assert hpw == "hotticket"
    CREDS.deletePassword()


def test_creds_delete():
    un = "wibble"
    host = "fictitious.host"
    CREDS = Credential(un, host)
    CREDS.setPassword(password="something else")
    CREDS.deletePassword()
    hpw = CREDS.getPassword()
    assert hpw is None
