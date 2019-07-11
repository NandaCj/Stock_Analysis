import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../Django_Stock_Analysis.settings")
from stocks_detail_api.models import ShortBalanceSheetModel

root_dir = os.path.dirname(os.getcwd())
data_collected = os.path.join(root_dir, 'data_collection/data_collection/data_collected')


class Insert_Data():

    def insert_balance_sheet(self):
        input_file = os.path.join(data_collected,'balance_sheet.txt')
        for line in open(input_file, 'r').readlines():
            print(line)

if __name__ == '__main__':
    Insert_Data().insert_balance_sheet()