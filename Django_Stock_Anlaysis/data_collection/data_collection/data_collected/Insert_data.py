import os
cur_dir = os.path.dirname(__file__)
import psycopg2 as pg
import datetime
from decimal importeq Decimal
connection = pg.connect(host='127.0.0.1', dbname='stock', user='stock', password='stock')
cursor = connection.cursor()

class InsertData():

    def insert_balance_sheet_data(self):
        """
        insert into short_balance_sheet ("year", "stock_name", "net_worth", "total_liabilities",
        "total_current_assests", "net_current_assets", "total_assets")
        values ('2019-04-01', 'hdfc_bank', 149206.35, 1189432.40, 949922.81, 894814.52, 1189432.40)

        :return:
        """
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

    def insert_shareholding_pattern(self):
        """

        :return:
        """

        r_lines = ['Indian Promoters',
                   'Foreign Promoters',
                   'Total Promoter',
                   'FIIs',
                   'Other Institutions',
                   'Total Institutions',
                   'Total Non-Institutions',
                   'Total Public',
                   'Grand Total', ]

        cols = '"year", "stock_name", "indian_promoter", "foreign_promoter", "total_promoter", "fiis", "other_institutions", "total_institutions", "total_non_institutions", "total_public", "grand_total"'
        years = ['2019-06-01', '2019-03-01', '2018-12-01', '2018-09-01', '2018-06-01', '2018-03-01',]
        table = 'shareholding_pattern'
        input_dir = os.path.join(cur_dir, 'shareholding_pattern_files')
        files_list = []
        for file in os.listdir(input_dir):
            file = os.path.join(input_dir,  file)
            files_list.append(open(file, 'r+'))
            # query = """ insert into {} ({}) values ('{}', '{}', {})""".format(table, cols, year, stock_name, values)
            # print(query)

    def shareholding_file_clean(self):
        input_dir = os.path.join(cur_dir, 'shareholding_pattern_files')
        output_dir = os.path.join(cur_dir, 'shareholding_pattern_cleaned')

        r_lines = ['Indian Promoters',
                   'Foreign Promoters',
                   'Total Promoter',
                   'FIIs',
                   'Other Institutions',
                   'Total Institutions',
                   'Total Non-Institutions',
                   'Total Public',
                   'Grand Total', ]

        cols = '"year", "stock_name", "indian_promoter", "foreign_promoter", "total_promoter", "fiis", "other_institutions", "total_institutions", "total_non_institutions", "total_public", "grand_total"'
        years = ['2019-06-01', '2019-03-01', '2018-12-01', '2018-09-01', '2018-06-01', '2018-03-01', ]

        for file in input_dir:
            ofile = open(os.path.join(input_dir, file), 'r+')
            for line in ofile.readlines():
                for r_line in r_lines:
                    if r_line in z



if __name__ == '__main__':
    InsertData().insert_shareholding_pattern()

