import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入需要翻译的内容(输入"q!"退出程序)：')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    data = {}
    data['i'] =  content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] =  'dict'
    data['client']= 'fanyideskweb'
    data['salt'] = '15664823954980'
    data['sign'] = '8b17ac6d72b1d9b60b0234380dc3722a'
    data['ts'] = '1566482395498'
    data['bv'] = '7e3150ecbdf9de52dc355751b074cf60'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print('翻译结果:%s' % (target['translateResult'][0][0]['tgt']))
    time.sleep(3)
