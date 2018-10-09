    
getTitle("呵呵", 2)
a = "一、实例的"
b = a.decode(encoding="UTF-8")
b.find(u"的")
a.find(u"的")
a.find("的")


from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append('i can has clipboardz?')
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

def getTitle( title, index=1 ):
    s = '<div class="title_hh"><a name="A'+(str(index)).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'
    from Tkinter import Tk
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(s)
    r.update() 
    r.destroy()
    print s
    return s
    
getTitle("一、Python 算术运算符", 1)
getTitle("1. import 语句（模块的引入）", 1)
getTitle("2. From&hellip;import 语句", 2)
getTitle("3. From&hellip;import * 语句", 3)
getTitle("4. dir() 函数", 4)
getTitle("5. Python 中的包", 5)
getTitle("6. PYTHONPATH 变量", 6)


def addToClipboard( string ):
    from Tkinter import Tk
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(string)
    r.update()
    r.destroy()
    
addToClipboard("alex lee")
addToClipboard("alex lee33333")

