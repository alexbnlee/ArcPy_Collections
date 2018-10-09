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
	return s


def getTitleFromClipboard( index=1 ):
	# 将得到的结果自动复制到剪贴板上
	"为标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	from Tkinter import Tk
	r = Tk()
	title = r.clipboard_get()
	s = '<div class="title_hh"><a name="A'+(str(index)).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(s)
	r.update() 
	r.destroy()
	return s

def getTitle3(index=1, *t):
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
	return s


