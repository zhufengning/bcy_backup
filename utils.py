import hashlib
import json
import time
import requests
from env import cookies, headers
from bs4 import BeautifulSoup


def get_ssr_data(like):
    like = BeautifulSoup(like, features="lxml")
    for i in like.find_all("script"):
        t = i.get_text()
        if "window.__ssr_data" in t:
            init_param = json.loads(
                eval(
                    t.splitlines()[0].replace("window.__ssr_data = JSON.parse", "")[:-1]
                )
            )
            return init_param


def get_post_data(id):
    item_url = "https://bcy.net/item/detail/%s" % id

    return get_ssr_data(get_auth(item_url).text)


def get_auth(url):
    time.sleep(0.5)
    return requests.get(url, cookies=cookies, headers=headers)


def calc_sha1(filepath):
    with open(filepath, "rb") as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash


def get_image_extension(file_bytes):
    if file_bytes.startswith(b"\xFF\xD8"):
        return ".jpeg"
    elif file_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    elif file_bytes.startswith(b"GIF87a") or file_bytes.startswith(b"GIF89a"):
        return ".gif"
    elif file_bytes.startswith(b"BM"):
        return ".bmp"
    elif file_bytes.startswith(b"\x00\x00\x00\x0c\x6a\x50\x20\x20\x0d\x0a\x87\x0a"):
        return ".jp2"
    elif file_bytes.startswith(b"II*\x00") or file_bytes.startswith(b"MM\x00*"):
        return ".tiff"
    elif file_bytes.startswith(b"\x00\x00\x01\x00"):
        return ".ico"
    elif file_bytes.startswith(b"\x00\x00\x02\x00"):
        return ".cur"
    else:
        return ""
