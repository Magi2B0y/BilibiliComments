# -*- coding =utf-8 -*-
import re
import os
from unicodedata import name
from pip import main
import requests as r
from time import sleep
from organize_comments import *
# https://api.bilibili.com/x/v2/reply/main?callback=jQuery1720959189428257528_1641545094585&jsonp=jsonp&next=3&type=1&oid=337901625&mode=3&plat=1&_=164154528134
# https://api.bilibili.com/x/v2/reply/main?callback=jQuery17209056291317339473_1641957014978&jsonp=jsonp&next=0&type=1&oid=716823215&mode=3&plat=1&_=1641957015495
def main(url=""):
    a = re.findall("next=\d+", url)
    # print(a)
    URL=url.split(a[0])
    # print(URL)
    flag2=1
    size=0
    for i in range(0, 20):
        flag1=1
        while flag1:
            # try:
                file_path="./comments/comment"+str(i)+".json"
                file = open(file_path, "w+", encoding="utf-8")
                url = URL[0]+"next="+str(i)+URL[1]
                headers = {
                    'Host': 'api.bilibili.com',
                    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
                    # 'Cache-Control': 'no-cache',
                    # 'accept-encoding': 'gzip, deflate, br',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/92.0.4515.131 Safari/537.36',
                    'Referer': 'https://www.bilibili.com/video/BV15J411W7VE?from=search&seid=6268509415447256533&spm_id_from=333.337'
                            '.0.0 ',
                    'Cookie': '_uuid=D55F483D-FAD3-3623-E6A7-1651F3A0AEB999392infoc; buvid3=BC5C43E7-9C1C-4183-9C97-0C2DAF1BADE4184978infoc; CURRENT_FNVAL=2000; blackside_state=1; LIVE_BUVID=AUTO5016143380260874; PVID=3; rpdid=|(umlJYR~~u)0J\'uYuRJJ)|~k; CURRENT_QUALITY=32; fingerprint=f31f35590ae63e520d5bdd98e7b4b097; buvid_fp=BC5C43E7-9C1C-4183-9C97-0C2DAF1BADE4184978infoc; buvid_fp_plain=BC5C43E7-9C1C-4183-9C97-0C2DAF1BADE4184978infoc; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; b_ut=5; sid=54zjl7qc; SESSDATA=38e9c6b0%2C1657511756%2Cdd626%2A11; bili_jct=6e336a2d0189c77beaa77de6f9513876; DedeUserID=646155114; DedeUserID__ckMd5=e8a85bbb6dc97555; bp_video_offset_646155114=614672414916891300; b_lsid=A2DDA1082_17E4C8F541F'
                }
                page = r.get(url, headers=headers)
                # print(page.text)
                file.write(page.text)
                print(i)
                file.close()
                # page = bs(page.text, "lxml")
                if i==0:
                    size=os.stat(file_path)
                    sleep(1)
                else:
                    if size == os.stat(file_path).st_size:
                        flag2=0
                        os.remove(file_path)
                        break
                    else:
                        size = os.stat(file_path).st_size
                        # sleep(1)
                flag1 = 0
            # except:
            #     print("retry "+str(i))
            #     continue
        if flag2==0:
            break
    orgnize()
    #删除comments下的文件，防止影响下一次生成comments.csv操作
    dirpath="./comments"
    del_list = os.listdir(dirpath)
    for f in del_list:
        file_path = os.path.join(dirpath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("over")

if __name__=="__main__":
    main()