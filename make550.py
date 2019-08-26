import urllib.request
import re
from bs4 import BeautifulSoup

def main():
    url = "http://baike.baidu.com/view/284853.htm"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser") #使用python默认的解析器

    for  each in soup.find_all(href=re.compile("view")):
        print(each.text,"->",''.join(["http://baike.baidu.com", each["href"]]))
        #上边用join()不用+直接拼接，是因为join()被证明执行效率高很多

if __name__ == "__main__":
    main()
