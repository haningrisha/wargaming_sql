from typing import List

from sqlalchemy.sql import text

from playground.playground import playground


def get_init_operations() -> List[str]:
    with open('playground/init.sql', 'r') as file:
        return [oper + ';' for oper in file.read().split(';')]


def main():
    init_operations = get_init_operations()
    with playground.connect() as connection:
        for operation in init_operations:
            connection.execute(text(operation))


if __name__ == '__main__':
    main()
