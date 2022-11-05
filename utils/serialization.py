from typing import List


def serialize_query(query, exclude:List[str] = ()):
    ser = {
        c.name: getattr(query, c.name)
        for c in query.__table__.columns
    }

    for field in exclude:
        ser.pop(field)
    return ser


