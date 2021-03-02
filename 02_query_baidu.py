# -*-conding:utf-8 -*-
import requests
if __name__ == "__main__":
    url = "https://www.baidu.com/s?ie=UTF-8&"
    kw = input("enter the word that you want to query:")
    param = {'wd':kw}

    response = requests.get(url=url,params=param)

    page_text = response.text
    file_name = kw + '.html'

    with open(file_name,'w',encoding = 'utf-8') as fp:
        fp.write(page_text)
        print(file_name," has been stored!!!")