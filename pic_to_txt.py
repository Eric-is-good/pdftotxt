# -*-coding:GBK -*-

import os
from paddleocr import PaddleOCR
from tqdm import tqdm


def pic_to_txt(path, output):
    j = 0
    imglist = os.listdir(path)
    print("�����ı�ʶ����")
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)
    print("��ʼת��")
    with open(output, "w") as f:
        for img in tqdm(imglist):
            try:
                result = ocr.ocr(os.path.join(path, img), cls=True)
                txts = [line[1][0] for line in result]
                for i in txts:
                    f.write(i)
                    f.write("\n")
                j = j + 1
                f.write("\n")
                f.write("#############################################################")
                f.write("\n")
            except:
                print("ͼƬ��Ϊ��" + imglist[j] + "��ͼƬ�޷���ȡ���֣���������")
                j = j + 1
