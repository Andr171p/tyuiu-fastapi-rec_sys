import json
import logging


class JsonFormatter(logging.Formatter):
    def __init__(self) -> None:
        super(JsonFormatter, self).__init__()

    def format(self, record: logging.LogRecord) -> str:
        json_record = dict()
        json_record['message'] = record.getMessage()
        if "req" in record.__dict__:
            json_record["req"] = record.__dict__["req"]
        if "res" in record.__dict__:
            json_record["res"] = record.__dict__["res"]
        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)
        return json.dumps(json_record)


logger = logging.root
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.DEBUG)
