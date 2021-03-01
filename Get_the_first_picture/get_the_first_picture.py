import requests
import os

p = "I:\python\spiders\Get_the_first_picture\picture"
url = "https://big.diercun.com/hd2/2021/0227/26/24mnorg_1 9.jpg"
root = "/picture/"
path = root + url.split("/")[-1]
try:
    #whether the picture already exists
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        #check the internet
        r.raise_for_status()
        #we use the "with" format to avoid to close the file by ourselves
        with open(p,"wb")as f:
            f.write(r.content)
        print("succeeded")
    else:
        print("the picture already exists")
except Exception as e:
    print("failed")
