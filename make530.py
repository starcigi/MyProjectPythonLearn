# -- coding:gbk --
import re
import urllib, urllib2, cookielib
 
loginurl = 'https://www.douban.com/accounts/login'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
 
params = {
"form_email":"your email",
"form_password":"your password",
"source":"index_nav" #û�еĻ���¼���ɹ�
}
 
#����ҳ�ύ��¼
response=opener.open(loginurl, urllib.urlencode(params))
 
#��֤�ɹ���ת����¼ҳ
if response.geturl() == "https://www.douban.com/accounts/login":
    html=response.read()
 
    #��֤��ͼƬ��ַ
    imgurl=re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url=imgurl.group(1)
        #��ͼƬ������ͬĿ¼��
        res=urllib.urlretrieve(url, 'v.jpg')
        #��ȡcaptcha-id����
        captcha=re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
        if captcha:
            vcode=raw_input('������ͼƬ�ϵ���֤�룺')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "��¼"
            #�ύ��֤����֤
            response=opener.open(loginurl, urllib.urlencode(params))
            ''' ��¼�ɹ���ת����ҳ '''
            if response.geturl() == "http://www.douban.com/":
                print 'login success ! '
