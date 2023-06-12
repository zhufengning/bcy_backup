import json
from utils import get_auth, get_ssr_data
uid = "2511341"
local_like = False
with open("res_ok.json","w",encoding="utf-8") as f:
    f.write("[]")

if local_like:
    like = open("like.html", "r", encoding="utf-8")
else:
    r = get_auth("https://bcy.net/u/%s/like"%uid)
    open("like.html", "w", encoding="utf-8").write(r.text)

    like = r.text


init_param = get_ssr_data(like)

metadata = []
next_list = init_param["page"]["list"]
next_time = init_param["page"]["since"]

while len(next_list) > 0:
    metadata += next_list

    res = get_auth("https://bcy.net/apiv3/user/favor?uid=%s&ptype=like&mid=%s&since=%s&size=35"%(uid,uid,next_time)).json()
    # print(res)
    next_list = res["data"]["list"]
    if len(next_list) > 0:
        next_time = next_list[-1]["since"]

json.dump(metadata, open("fav.json", "w", encoding="utf-8"), ensure_ascii=False)
