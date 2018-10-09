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
from win_diy import *
a = "我是一个中国人"
def decodeChinese( string ):
	"将中文 utf-8 编码转为 Unicode 编码"
	tmp = string.decode('utf-8')
	return tmp

def encodeChinese( string ):
	"将 Unicode 编码转为 utf-8 编码"
	tmp = string.encode('utf-8')
	return tmp

a = "我是一个中国人"
# 转成 Unicode
b = decodeChinese(a)
# 将“中国人”替换成“abc”
c = "中国人"
# 转成 Unicode
d = decodeChinese(c)
e = b.replace(b, d, "abc")
e = b.replace(c, "abc")
e = b.replace(c, "abc".decode())
e = b.replace(d, "abc")
e
# 转码为 utf-8
f = encodeChinese(e)
print f
chardet.detect(f)
def replaceChinese( string, old_str, new_str ):
    string_uni = decodeChinese(string)
    old_str_uni = decodeChinese(old_str)
    new_str_uni = decodeChinese(new_str)
    tmp = string_uni.replace(old_str_uni, new_str_uni)
    tmp_utf_8 = encodeChinese(tmp)
    return tmp_utf_8
    
replaceChinese("我是中国人", "中国人", "abc")
print replaceChinese("我是中国人", "中国人", "abc")
print a
a.replace("中国人", "日本人")
print a.replace("中国人", "日本人")
print a.replace("中国人", "abc")
a = "我是一个abc"
a.replace("abc", "中国人")
print a.replace("abc", "中国人")
a = "1. 我是一个abc"
print a.replace("1. ", "一、")
con = win.getClipboard()
print con.replace("1. ", "一、")
print con.replace("1. ", "2. ")
    a=10
    print a
    
    mylist.append([1,2,3,4])
    print mylist
    return
    
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age: ", age
   return
   
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age: ", age
   return
   
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age: ", age
   return
   
   "打印任何传入的字符串"
   print "Name1: ", name
   flag = 2
   for var in vartuple:
       print "Name"+str(flag)+": ", var
       flag=flag+1
       
print replaceChinese(con, "1. ", "一、")
print con
    a=10
    print a
    
    mylist.append([1,2,3,4])
    print mylist
    return
    
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age: ", age
   return
   
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age: ", age
   return
   
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age: ", age
   return
   
   "打印任何传入的字符串"
   print "Name1: ", name
   flag = 2
   for var in vartuple:
       print "Name"+str(flag)+": ", var
       flag=flag+1
       
con_uni = decodeChinese(con)
chardet.detect(con)
con = win.getClipboard()
chardet.detect(con)
con_array = con.splitlines()
chardet.detect(con_array[0])
print con_array[0]
con_array[0]
chardet.detect(a)
chardet.detect(con_array[0])
con_array[0].replace("www", "wwwwwwwwwwwwwwwww")
con
con_array[0].replace("www", "上岛咖啡了时代峰峻")
con_array[0].replace(u"www", "上岛咖啡了时代峰峻")
con_array[0].replace(u"www", u"上岛咖啡了时代峰峻")
con = win.getClipboard()
con.replace(u"1. ", u"一、")
con.replace(u"2. ", u"二、")
con.replace(u"3. ", u"三、")
con.replace(u"4. ", u"四、")
con.replace(u"5. ", u"五、")
con.replace(u"6. ", u"六、")
con = con.replace(u"1. ", u"一、")
con = con.replace(u"2. ", u"二、")
con = con.replace(u"3. ", u"三、")
con = con.replace(u"4. ", u"四、")
con = con.replace(u"5. ", u"五、")
con = con.replace(u"6. ", u"六、")
win.addToClipboard(con)
con = win.getClipboard()
con_array = con.splitlines()
for s in con_array:
    index = s.find(u'一、')
    if index >= 0:
        if s.find(u'<li>') < 0: 
            
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------

for num in num_CHN:
    num
    
# 查找相关标题指示
num_CHN = ['一、', '二、', '三、', '四、', '五、', '六、', '七、', '八、']             

# 查找其所在行，并判断不是目录，进行行的替换
# 转换为 Unicode 编码才可以操作
for num in num_CHN:
    i = 0
    for s in con_array:
        index = s.find(num.decode('utf-8'))
        if index >= 0:
            if s.find(u'<li>') < 0: 
                index_end = s.find(u'</', index)
                title = s[index:index_end]
                con_array[i] = blog.getTitle(title)
        i = i + 1
        
# 通过回车将列表合并起来
n = '\n'
# 将其复制到剪切板
win.addToClipboard(n.join(con_array))

