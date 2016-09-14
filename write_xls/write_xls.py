# -*- coding:utf-8 -*-

import xlrd
import xlsxwriter
from xlutils import *
import sys
sys.path.append('../')
from parse_result.parse_result import ResultParser, HouseInfo
from analysis_xls import XlsAnalysis

class XlsWriter(object):
    def __init__(self, house_list, file_name):
        self.house_list = house_list
        self.file_name = file_name

    def write(self):
        workbook = xlsxwriter.Workbook(self.file_name)
        worksheet = workbook.add_worksheet()
        title = (u'序号', u'小区', u'面积平米', u'户型', u'地铁', u'地铁站', u'总价（万元）',  u'均价（元）')
        header_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#D7E4BC',
            'border': 1
        })
        analysis_xiaoqu = XlsAnalysis('xiaoqu.xlsx')
        xiaoqu_title = (u'序号', u'小区', u'均价')
        analysis_xiaoqu.set_title(xiaoqu_title)

        analysis_station = XlsAnalysis('station.xlsx')
        station_title = (u'序号', u'地铁站', u'均价')
        analysis_station.set_title(station_title)
        worksheet.write_row('A1', title, header_format)
        row = 1
        col = 0
        num = 1
        for house in self.house_list:
            worksheet.write_number(row, col, num)
            num += 1
            worksheet.write_string(row, col+1, house.xiaoqu)
            worksheet.write_string(row, col+2, house.house_area)
            worksheet.write_string(row, col+3, house.house_type)
            worksheet.write_string(row, col+4, house.subway_line)
            worksheet.write_string(row, col+5, house.subway_station)
            worksheet.write_string(row, col+6, house.total_price)
            worksheet.write_string(row, col+7, house.unit_price)
            row += 1
            analysis_xiaoqu.set_price_dict(house.xiaoqu, house.unit_price)
            analysis_station.set_price_dict(house.subway_station, house.unit_price)

        workbook.close()
        analysis_xiaoqu.write()
        analysis_station.write()
        return True


if __name__ == '__main__':
    result_parser = ResultParser()
    result_parser.parse('../data/chaoyang.dat')
    xls_writer = XlsWriter(result_parser.HouseInfoList, './data.xlsx')
    xls_writer.write()
