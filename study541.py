import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容：')

url = 'http://fanyi.youdao.com/translate'
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
