#-*-coding:GBK -*-
from pdf_to_pic import pdf_to_pic
from pic_to_txt import pic_to_txt

"""
��Ҫ�Ƚ��� pics �ļ���
.pdf --->  pics  ----> .txt
"""

pdf_to_pic("1.pdf", "pics")
pic_to_txt("pics", "1.txt")
