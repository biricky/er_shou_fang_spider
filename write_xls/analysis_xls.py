# -*- coding:utf-8 -*-

import xlrd
import xlsxwriter
from xlutils import *
import sys
sys.path.append('../')
from parse_result.parse_result import ResultParser, HouseInfo

class XlsAnalysis(object):
    def __init__(self, file_name):
        self.price_dict = {}
        self.file_name = file_name
        self.title_tuple = ()

    def set_price_dict(self, key, price):
        if key in self.price_dict:
            price_list = self.price_dict[key]
            price_list.append(price)
            self.price_dict[key] = price_list
        else:
            price_list = []
            price_list.append(price)
            self.price_dict[key] = price_list

    def set_title(self, title_tuple):
        self.title_tuple = title_tuple

    def write(self):
        workbook = xlsxwriter.Workbook(self.file_name)
        worksheet = workbook.add_worksheet()
        header_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#D7E4BC',
            'border': 1
        })

        worksheet.write_row('A1', self.title_tuple, header_format)
        row = 1
        col = 0
        num = 1
        sorted_price_dict = {}
        for key in self.price_dict:
            sum_price = 0.0
            avg_price = 0.0
            for p in self.price_dict[key]:
                sum_price = sum_price + float(p)
            avg_price = sum_price / len(self.price_dict[key])
            sorted_price_dict[avg_price] = key

        for key in sorted(sorted_price_dict.keys()):
            worksheet.write_number(row, col, num)
            num += 1
            worksheet.write_string(row, col+1, sorted_price_dict[key])
            worksheet.write_number(row, col+2, key)
            row += 1

        self.create_chart(workbook, worksheet, row)
        workbook.close()
        return True

    def create_chart(self, workbook, worksheet, row):
        chart_top10= workbook.add_chart({'type': 'column'})
        worksheet.insert_chart('A20', chart_top10)
        chart_top10.set_title({'name': '价格最底Top15'})
        chart_top10.add_series({
            'categories':['Sheet1', 1, 1, 15, 1],
            'values': ['Sheet1', 1, 2, 15, 2],
        })
        chart_bottom10= workbook.add_chart({'type': 'column'})
        worksheet.insert_chart('A10', chart_bottom10)
        chart_bottom10.set_title({'name': '价格最高Top15'})
        chart_bottom10.add_series({
            'categories':['Sheet1', row, 1, row-15, 1],
            'values': ['Sheet1', row, 2, row-15, 2],
        })
        return True

if __name__ == '__main__':
    pass
