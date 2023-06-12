from down_res import down_res
from utils import get_post_data
import json
import time

data_list = json.load(open("fav.json", encoding="utf-8"))

import os
os.makedirs("out/info", exist_ok=True)
os.makedirs("out/new", exist_ok=True)
os.makedirs("out/res", exist_ok=True)

for i in data_list:
    id = i["item_detail"]["item_id"]
    print(id)
    info_path = "out/info/%s.json"%id
    if os.path.exists(info_path):
        print("Skipped")
    else:
        open(info_path, "w", encoding="utf-8").write(json.dumps(get_post_data(id),ensure_ascii=False))
    down_res(info_path)
    
