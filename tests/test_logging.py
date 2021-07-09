import ptvg

log = ptvg.log


def test_logmessage():
    log.error("this is an error message")
    assert 1 == 1
