# -*- coding: utf-8 -*-
# @Time    : 10/4/2020 5:22 PM
# @Author  : Enmo Ren
# @FileName: geoJson.py
# @Software: PyCharm
import geojson


class MyPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y

@property
def __geo_interface__(self):
    return {'type': 'Point', 'coordinates': (self.x, self.y)}


if __name__=="__main__":
    point_instance = MyPoint(52.235, -19.234)