import urllib
import urllib.parse
import urllib.request
import ssl
url = "https://www.proovl.com/api/send.php?"
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
params = {
'user': "user",
'token': "token",
'from': "from",
'to': "to",
'text': "text"}
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
query_string = urllib.parse.urlencode(params)
http_req = url + query_string
req = urllib.request.Request(http_req, headers=hdr)
f = urllib.request.urlopen(req)
freq = (f.read().decode('utf-8'))
x = freq.split(";")
g = x[1].replace("\"","")
y = x[0].replace("\"","")
if x[0] == "Error":
  print("Error message: ",x[1])
else:
  print("Message ID: ",x[1])
f.close()
