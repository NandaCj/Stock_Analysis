import os
cur_dir = os.path.dirname(__file__)
import psycopg2 as pg
import datetime
from decimal import Decimal
connection = pg.connect(host='127.0.0.1', dbname='stock', user='stock', password='stock')
cursor = connection.cursor()

class InsertData():

    def insert_balance_sheet_data(self):
        input_file = open(os.path.join(cur_dir, 'balance_sheet.txt'), 'r').readlines()
        table = 'short_balance_sheet'
        for line in input_file:
            data_list = eval(line)
            for detail in data_list:
                # print(detail)
                keys = str(list(detail.keys())).strip('[]').replace("'", '"')
                year = str(list(detail.values())[0])
                name = str(list(detail.values())[1])
                values = str(list(detail.values())[2:]).strip('[]').replace("'", "")

                query = """insert into {} ({}) values ('{}', '{}', {});""".format(table, keys, year,name, values)
                print(query)
                cursor.execute(query)
                connection.commit()

        # result = cursor.execute('select * from short_balance_sheet;')
        #
        # print(cursor.fetchall())


if __name__ == '__main__':
    InsertData().insert_balance_sheet_data()

