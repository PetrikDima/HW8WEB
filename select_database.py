import sqlite3
from pprint import pprint


def executor(query_file):
    with open(query_file, 'r') as f:
        sql = f.read()

    with sqlite3.connect('hw8web.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


def main():
    u_input = input('>>>')
    match u_input:
        case '1':
            pprint(executor('query_1.sql'))
        case '2':
            pprint(executor('query_2.sql'))
        case '3':
            pprint(executor('query_3.sql'))
        case '4':
            pprint(executor('query_4.sql'))
        case '5':
            pprint(executor('query_5.sql'))
        case '6':
            pprint(executor('query_6.sql'))
        case '7':
            pprint(executor('query_7.sql'))
        case '8':
            pprint(executor('query_8.sql'))
        case '9':
            pprint(executor('query_9.sql'))
        case '10':
            pprint(executor('query_10.sql'))
        case '11':
            pprint(executor('query_11.sql'))
        case '12':
            pprint(executor('query_12.sql'))


if __name__ == '__main__':
    while True:
        main()
