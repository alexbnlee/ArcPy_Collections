from blog_diy import *
blog.getTitle3()
def getTitle4(index=1, *t):
	# 将得到的结果自动复制到剪贴板上
	"为标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	from Tkinter import Tk
	r = Tk()
	title = r.clipboard_get()
	if len(t) > 0:
		title = t[0]
	s = '<div class="title_hh"><a name="A'+(str(index)).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(s)
	r.update() 
	r.destroy()
	print s
	return s

def getTitle4(index=1, *t):
	# 将得到的结果自动复制到剪贴板上
	"为标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	from Tkinter import Tk
	r = Tk()
	title = r.clipboard_get()
	if len(t) > 0:
		title = t[0]
	s = '<div class="title_hh"><a name="A'+(str(index)).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(s)
	r.update() 
	r.destroy()
	print s

getTitle4()
getTitle4()
def getTitle4(index=1, *t):
	# 将得到的结果自动复制到剪贴板上
	"为标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	from Tkinter import Tk
	r = Tk()
	title = r.clipboard_get()
	if len(t) > 0:
		title = t[0]
	s = '<div class="title_hh"><a name="A'+(str(index)).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(s)
	r.update() 
	r.destroy()

getTitle4()
getTitle4()
from win_diy import *
print win.cutChinese("我是一个abc", 2)
print win.cutChinese("我是一个abc", 2, 4)
print win.cutChinese("我是一个abc", 2, 5)
print win.cutChinese("我是一个abc", 2, 6)
s = win.getClipboard()
print s
from win_diy import *
print win.cutChinese("我是一个abc", 2)
print win.cutChinese("我是一个abc", 2, 4)
print win.cutChinese("我是一个abc", 2, 5)
print win.cutChinese("我是一个abc", 2, 6)
s.splitlines()
from win_diy import *', u'>>> print win.cutChinese("\u6211\u662f\u4e00\u4e2aabc", 2)', u'\u4e00\u4e2aabc', u'>>> print win.cutChinese("\u6211\u662f\u4e00\u4e2aabc", 2, 4)', u'\u4e00\u4e2a', u'>>> print win.cutChinese("\u6211\u662f\u4e00\u4e2aabc", 2, 5)', u'\u4e00\u4e2aa', u'>>> print win.cutChinese("\u6211\u662f\u4e00\u4e2aabc", 2, 6)', u'\u4e00\u4e2aab']
for a in s.splitlines():
    print a
    
from win_diy import *
print win.cutChinese("我是一个abc", 2)
print win.cutChinese("我是一个abc", 2, 4)
print win.cutChinese("我是一个abc", 2, 5)
print win.cutChinese("我是一个abc", 2, 6)
cont = win.getClipboard()
cont.replace('1.', '一、')
cont.replace('1.', '3.')
a = "你好的"
b = a.decode('utf-8')
b.replace('的', 'a')
a
print a
a.decode('utf-8')
b
len(b)
len(a)
b[1:2]
b[1:2].decode('utf-8')
b[1:2].encode('utf-8')
print b[1:2].encode('utf-8')
print b
print a
b.find("的")
m = "的"
n = m.decode('utf-8')
b.find(n)
b.replace(n, '1.')
print b
print b.replace(n, '1.')
import sys
print sys.getdefaultencoding()
m
int('0xe7', 16)
int('\xe7\x9a\x84', 16)
int('xe7', 16)
o = m.decode('unicode')
m = "我是中国人"
m
print m
n = m.decode('utf-8')
n
print n
len(m)
len(n)
def decodeChinese( string ):
    tmp = string.decode('utf-8')
    return tmp
    
(decodeChinese(n)).find(decodeChinese('中'))
n = decodeChinese(n)
m = decodeChinese(n)
n
m = n.decode('utf-8')
cc = "我是中国人"
ss = decodeChinese(cc)
ss.find(decodeChinese("中")

ss.find(decodeChinese("中"))
print cc+"lsdkjf"
print ss+"lsdkfjl"
ss[2:4]
print ss[2:4]
ss[2:4].encode('utf-8')
cc.decode()
import chardet
import chardet
import chardet
print chardet.detect("abc")
print chardet.detect("我是中国人")
print chardet.detect("abc-我是中国人")

