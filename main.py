#-*-coding:GBK -*-
from pdf_to_pic import pdf_to_pic
from pic_to_txt import pic_to_txt

"""
使用前先建立 pics 文件夹
.pdf --->  pics  ----> .txt
"""

pdf_to_pic("1.pdf", "pics")
pic_to_txt("pics", "1.txt")
