from win_diy import win
win.addToClipboard("lkdflk")
8^3
8*8*8
def getTitle( title, index=1 ):
	# 将得到的结果自动复制到剪贴板上
	"为标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	s = '<div class="title_hh"><a name="A'+(str(index)).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(s)
	r.update() 
	r.destroy()
	print s
	

dict = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6}
a='一'
dict[a]
dict['alk']
a="一、我的"
a[0:1]
a[0:4]
import os
b = a.decode('utf-8')
b[0:1]
b.find(u"的")
b[0:1].encode('utf-8')
a.decode('utf-8')[0:1].encode('utf-8')
str = '中国人'

str.decode（'utf-8')[0:1].encode('utf-8')

str = '中国人'

str.decode('utf-8')[0:1].encode('utf-8')

str = '中国人'
str.decode('utf-8')[0:1].encode('utf-8')
print str.decode('utf-8')[0:1].encode('utf-8')
a = str.decode('utf-8')[0:1].encode('utf-8')
a
print a
tmp = a.decode('utf-8')[0:1].encode('utf-8')
tmp
print tmp
a="一、我的"
tmp = a.decode('utf-8')[0:1].encode('utf-8')
print tmp
dict[tmp]
tmp.encode()
tmp.decode()
s = print(a)
import urllib
urllib.unquote(a)
a
print a
b="我的娘啊"
b
print b
def cutChinese(string, start, end):
    tmp = string.decode('utf-8')[start:end].encode('utf-8')
    return tmp
    
m = cutChinese("李炳南", 1, 2)
print m
def cutChinese(string, start, end=len(string)):
    tmp = string.decode('utf-8')[start:end].encode('utf-8')
    return tmp
    
def cutChinese(string, start, end=len(string)-1):
    tmp = string.decode('utf-8')[start:end].encode('utf-8')
    return tmp
    
def cutChinese(string, start):
    tmp = string.decode('utf-8')[start:(len(string)-1)].encode('utf-8')
    return tmp
    
m = cutChinese("李炳南", 1, 2)
m = cutChinese("李炳南", 1)
print m

def cutChinese(string, *vartuple):
    start = vartuple[0]
    if len(vartuple)==2:
    tmp = string.decode('utf-8')[start:end].encode('utf-8')
    return tmp
    
def cutChinese(string, *vartuple):
    start = vartuple[0]
    if len(vartuple)==2:
        end = vartuple[1]
    else:
        end = len(string)
    tmp = string.decode('utf-8')[start:end].encode('utf-8')
    return tmp
    
m = cutChinese("李炳南", 1)
print m
m = cutChinese("李炳南", 1, 2)
print m
m = cutChinese("李炳南", 1, 2, 3, 4, 5)
print m
m = cutChinese("李炳南", 1, 1, 3, 4, 5)
print m
m = cutChinese("李炳南", 1, 1)
print m
m = cutChinese("李炳南", 1, 2)
print m
def cutChinese(string, *vartuple):
    start = vartuple[0]
    if len(vartuple)>1:
        end = vartuple[1]
    else:
        end = len(string)
    tmp = string.decode('utf-8')[start:end].encode('utf-8')
    return tmp
    
print cutChinese("李炳南", 1, 2)
print cutChinese("李炳南", 1, 2, 3, 4)
print cutChinese("李炳南", 1)



>>> def cutChinese(string, *vartuple):
...     start = vartuple[0]
...     if len(vartuple)>1:
...         end = vartuple[1]
...     else:
...         end = len(string)
...     tmp = string.decode('utf-8')[start:end].encode('utf-8')
...     return tmp
...     
>>> print cutChinese("李炳南", 1, 2)
炳
>>> print cutChinese("李炳南", 1, 2, 3, 4)
炳
>>> print cutChinese("李炳南", 1)
炳南