# -*- coding: utf-8 -*-

from PIL import Image


class Image2Code:
    def __init__(self):
        # 字符集列表
        self.pixel_list = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    '''
    字符映射方法
    
    '''
    def color_map(self, r, g, b, alpha=256):
        print('即将到来')