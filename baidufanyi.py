from tkinter import *
import requests,json


def fanYi():
    # 翻译内容，返回翻译的结果
    # 输出翻译结果时去除前面多余的空格
    content = entry1.get().strip()
    url = "https://fanyi.baidu.com/transapi"
    data = {"query": content}
    r = requests.post(url, data=data).text
    ret = json.loads(r)
    res.set(ret["data"][0]["dst"])


master = Tk()   # 实例化一个对象，对象里面有很多方法,其中一个功能就是让我们的对象展示出来。
master.title('翻译软件')

# 设定软件的坐标位置和软件界面的宽和高
master.geometry('400x100+560+150')

# master.geometry('')
label1 = Label(master, text='输入内容：', fg='red', font=('GB2312', 18))
label1.grid(row=0, column=0)

label2 = Label(master, text='结果：', fg='red', font=('GB2312', 18))
label2.grid(row=1, column=0)

entry1 = Entry(master, fg='red', font=('GB2312', 18))
entry1.grid(row=0, column=1)

res = StringVar()
entry2 = Entry(master, fg='red', font=('GB2312', 18), textvariable=res)
entry2.grid(row=1, column=1)

button1 = Button(master, width=10, text='翻译', fg='blue', font=('GB2312',18), command=fanYi)
button1.grid(row=2, column=0, sticky=W)

button2 = Button(master,width=10, text='退出',fg='blue', font=('GB2312',18), command=master.quit)
button2.grid(row=2,column=1, sticky=E)

master.mainloop()   # 能够让图形化界面出现
