import urllib.request

req = urllib.request.Request('http://placekitten.com/200/300')
response = urllib.request.urlopen(req)
cat_img = response.read()

with open('cat_200_300.jpg','wb') as f:
    f.write(cat_img)
