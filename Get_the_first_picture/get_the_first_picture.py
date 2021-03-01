import requests
import os

url = "https://img.tupianzj.com/uploads/allimg/180528/9-1P52Q94401.jpg"
root = "/python/spiders/Get_the_first_picture/"
path = root + url.split("/")[-1]
try:
    # 判断文件是否存在
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        # 判断网络连接的状态
        r.raise_for_status()
        #使用with语句可以不用自己手动关闭已经打开的文件流
        with open('001.jpg' ,"wb") as f:
            # 返回的是bytes型也就是二进制的数据
            f.write(r.content)
        print("爬取完成")
    else:
        print("文件已存在")
except Exception as e:
    print("爬取失败:"+str(e))
