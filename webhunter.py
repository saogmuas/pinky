# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:20:43 2017

@author: ubuntupapa
"""


import urllib
import urllib2


main_webpage = "http://www.ravaonline.com/v2/empresas/precioshistoricos.php?e=MERVAL&csv=0"
main_webpage = "http://www.ravaonline.com"


testfile = urllib.URLopener()
a=testfile.retrieve(main_webpage, "hist_MERVAL20170930.csv")
testfile.retrieve(main_webpage, "hola.csv")

#<a href="/v2/empresas/precioshistoricos.php?e=MERVAL&amp;csv=1">» Bajar en formato Excel</a>

response = urllib2.urlopen(main_webpage)
html = response.read()
html = urllib.urlretrieve ("http://www.ravaonline.com/v2/empresas/precioshistoricos.php?e=MERVAL&amp;csv=1", "pepe.csv")
type(html[1])


response = urllib2.urlopen("http://www.ravaonline.com/v2/empresas/precioshistoricos.php?e=MERVAL&csv=0")
html = response.read()
html = urllib.urlretrieve ("http://www.ravaonline.com/v2/empresas/precioshistoricos.php?e=MERVAL&amp;csv=1", "pepe.csv")
type(html[1])




import csv
import urllib2

url = 'www.ravaonline.com/v2/empresas/precioshistoricos.php?e=MERVAL&csv=1'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()














