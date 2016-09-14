# -*- coding:utf-8 -*-
import json
import ConfigParser
import base64
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

class HouseInfo(object):
    def __init__(self):
        self.subway_station = ""
        self.subway_line = ""
        self.xiaoqu = ""
        self.unit_price = ""
        self.total_price = ""
        self.house_area = ""
        self.house_type = ""
    def set_all(self, xiaoqu, house_area, house_type, subway_line, subway_station, total_price, unit_price):
        self.subway_station = subway_station
        self.subway_line = subway_line
        self.xiaoqu = xiaoqu
        self.unit_price = unit_price
        self.total_price = total_price
        self.house_area = house_area
        self.house_type = house_type

    def set_house_info(self, house_info):
        pass
    def set_subway_station(self, subway_station):
        pass
    def set_xiaoqu(self, xiaoqu):
        pass
    def set_unit_price(self, unit_price):
        pass
    def set_total_price(self, total_price):
        pass
    def set_house_area(self, house_area):
        pass
    def set_house_type(self, house_type):
        pass

class ResultParser(object):
    def __init__(self):
        self.HouseInfoList = []

    def parse(self, data_file="./data"):
        with open(data_file, 'r') as df:
            for line in df.readlines():
                if not self.parse_line(line):
                    continue
        return True

    def parse_line(self, line):
        try:
            data = json.loads(line)
            info_list = data["house_info"][0]
            house_type = info_list.split('|')[1]
            house_area = info_list.split('|')[2].split(u'平')[0]
            total_price = data["total_price"][0]
            subway_info = data["subway_station"][0].split(u'离')[1].split(u'站')[0]
            subway_line = subway_info.split(u'线')[0]
            subway_station = subway_info.split(u'线')[1]
            xiaoqu = data["xiaoqu"][0]
            unit_price = data["unit_price"][0].split(u'元')[0].split(u'价')[1]
            #print xiaoqu, house_area, house_type, subway_line, subway_station, total_price, unit_price
            house = HouseInfo()
            house.set_all(xiaoqu, house_area, house_type, subway_line, subway_station, total_price, unit_price)
            self.HouseInfoList.append(house)
            return True
        except Exception, e:
            print 'data format wrong %s' % (json.dumps(data, ensure_ascii=False))
            return False

    def write2xml(self):
        pass

if __name__ == '__main__':
    result_parser = ResultParser()
    result_parser.parse('../data/chaoyang.dat')
