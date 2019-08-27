import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23  #到首位数字的位置
    b = html.find(']',a)

    return (html[a:b])    #返回13（页数）

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1: 
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])  #a+9是索引到http的h，b+4是加上.jpg的长度
        else:
            b = a + 9
            
        a = html.find('img src=', b)
    
    for each in img_addrs:
        print(each)
    
def save_imgs(folder,img_addrs):
    pass

def download_mm(folder='ooxx',pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)

if __name__ == '__main__':
    download_mm()
    
