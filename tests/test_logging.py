import ptvg

log = ptvg.log


def test_logmessage():
    log.error("this is an error message")
    log.warning("this is a warning message")
    log.info("this is an info message")
    log.debug("this is a debug message")
    assert 1 == 1
