# -*-coding:GBK -*-

import os
from paddleocr import PaddleOCR
from tqdm import tqdm


def pic_to_txt(path, output):
    j = 0
    imglist = os.listdir(path)
    print("导入文本识别器")
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)
    print("开始转换")
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
                print("图片名为：" + imglist[j] + "的图片无法提取文字，可能已损坏")
                j = j + 1
