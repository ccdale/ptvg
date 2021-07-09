import logging
import logging.handlers

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
syslog = logging.handlers.SysLogHandler(address="/dev/log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
syslog.setFormatter(formatter)
log.addHandler(syslog)

__version__ = "0.1.6"
