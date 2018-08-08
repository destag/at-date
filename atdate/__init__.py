from .api import AtDateParser


def parse(at_date_string):
    parser = AtDateParser(at_date_string)
    return parser.execute()


__all__ = [AtDateParser, parse]
