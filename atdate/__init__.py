from .api import AtDateParser


def parse(at_date_string):
    parser = AtDateParser()
    return parser.execute(at_date_string)


__all__ = ['AtDateParser', 'parse']
