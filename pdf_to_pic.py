#-*-coding:GBK -*-

import office

def pdf_to_pic(pdf_path, out_dir):
    office.pdf.pdf2imgs(
        pdf_path=pdf_path,
        out_dir=out_dir
    )
