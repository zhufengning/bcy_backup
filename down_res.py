import json
import re
import os
import shutil

from utils import calc_sha1, get_auth, get_image_extension

res_ok = json.load(open("res_ok.json","r",encoding="utf-8"))

def search_urls(text):
    # 定义正则表达式匹配URL的模式
    url_pattern = re.compile(
        r'((https?|ftp)://(?:[^\s"<>#]|[!$&\'()*+,.;=:@/?]|%[0-9a-fA-F]{2})*)+'
    )

    # 使用正则表达式在文本中查找所有匹配的URL
    matched_urls = url_pattern.findall(text)

    # 输出匹配的URL
    urls = []
    for url in matched_urls:
        urls.append(url[0])
    return urls

def down_res(path):
    text = open(path, "r", encoding="utf-8").read()
    urls = search_urls(text)
    # print(urls)
    for url in urls:
        print(url)
        flag = False
        for i in res_ok:
            if i["url"] == url:
                print("Skip")
                flag = True
        if flag:
            continue
        res = get_auth(url)
        with open("tmp", "wb") as f:
            f.write(res.content)
        sha1 = calc_sha1("tmp")
        tail = get_image_extension(open("tmp", "rb").read())

        res_path = "out/res/%s%s" % (sha1, tail)
        text = text.replace(url, res_path)
        shutil.move("tmp", res_path)
        res_ok.append({"url":url,"sha1":sha1})
        json.dump(list(res_ok), open("res_ok.json","w",encoding="utf-8"))
    open("out/new/%s"%(path.replace("out/info", "")), "w", encoding="utf-8").write(text)
    
