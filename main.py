# -*- coding:utf-8 -*-

import os
from parse_result.parse_result import HouseInfo, ResultParser
from write_xls.write_xls import XlsWriter
from hire_tool.spiders.dmoz_spider import DmozSpider

def main():

    #exec spider
    cmd = "scrapy crawl dmoz"
    os.system(cmd)

    #parse result

    parser = ResultParser()
    if not parser.parse('data/chaoyang.dat'):
        print 'parse result failed'
        return False

    xls_writer = XlsWriter(parser.HouseInfoList, 'chaoyang.xlsx')
    if not xls_writer.write():
        print 'write xls failed'
        return false

    return True

if __name__ == '__main__':
    main()
