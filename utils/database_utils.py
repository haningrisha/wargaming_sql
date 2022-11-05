from typing import List

from sqlalchemy.engine import LegacyRow


def create_table(data: List[LegacyRow]):
    header = data[0]._fields
    data = [list(row) for row in data]
    return {
        'header': header,
        'content': data
    }