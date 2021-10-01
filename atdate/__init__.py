from datetime import datetime
from typing import Optional

from .api import AtDateParser


def parse(at_date_string: str) -> Optional[datetime]:
    parser = AtDateParser()
    return parser.execute(at_date_string)


__all__ = ["AtDateParser", "parse"]
