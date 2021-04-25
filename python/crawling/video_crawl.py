import os
import urllib.request as urllib2
import ssl

url_link = '<UNL LINK>'

# req = urllib2.Request(url_link, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
# gcontext = ssl.SSLContext()  # Only for gangstars
# info = urllib2.urlopen(req, context=gcontext).read()


#context = ssl._create_unverified_context()

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

urllib2.urlretrieve(url_link, '<Video Name>') 
