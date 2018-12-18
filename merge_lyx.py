#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import jinja2
from jinja2 import Template
import glob
from pathlib import Path
import argparse

lyx_jinja_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath('.'))
)


def get_pdfs(dir):
    part=os.path.split(dir)[1]
    pdfs=sorted(glob.glob(os.path.join(dir,"*.pdf")))
    pdfs_list=list(map(lambda path:{"pdf_path":path.replace('\\', '/'),
         "pdf_name":os.path.splitext(os.path.split(path)[1])[0]},pdfs))
    part_dict={"part_name":part,"pdfs":pdfs_list}
    return part_dict

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="生成LyX代码")
    parser.add_argument('--dirname', help="文件夹名称",default="example")
    parser.add_argument('--title', help="报告名称",default="Example Reports")
    parser.add_argument('--author', help="报告作者",default="Example Author")
    args = parser.parse_args()
    dirs=glob.glob(args.dirname+"/*")
    dirs=sorted(list(filter(lambda path:os.path.isdir(path),dirs)))
    dirs=list(map(lambda path:os.path.abspath(path),dirs))
    parts=list(map(get_pdfs,dirs))
    template=lyx_jinja_env.get_template('template.lyx')
    output=template.render(title=args.title,author=args.author,parts=parts)
    if not os.path.isdir("./build"):
        os.makedirs("./build")
    with open(os.path.join("./build/",args.dirname+".lyx"),"w",encoding="utf-8") as fout:
        fout.write(output)
