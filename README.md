下载所有半次元点赞过的，会把链接一起下载并修改json里的链接  
但是视频不是链接所以不行  
怎么看，除了直接看json以外还没想好  

先把cookies和headers以字典的格式写进env.py
然后修改gen_metadata.py里的uid。
最后运行gen_metadata.py和down.py