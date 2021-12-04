
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import requests

windows = tk.Tk()
windows.title("Harryの音乐下载器(试用版)")
windows.geometry("500x300")  # 界面大小
windows.iconbitmap("hydromechanics.ico")
input_space = tkinter.Entry(windows,
                            fg="black",
                            bg="white",
                            width=50,
                            font=('微软雅黑', 10, 'bold'),
                            show="")
input_space.place(relx=0.3, rely=0.3,
                  anchor="center")
input_space.pack()


def convert():
    url = input_space.get()
    t.insert("insert", "http://music.163.com/song/media/outer/url?id" + url.split("/song?id")[1] + ".mp3")
    tk.messagebox.showinfo("提醒!", "转换完成DA☆ZE\n全选复制到浏览器就好了DA☆ZE")


def save_file():
    url = input_space.get()
    id = url.split("/song?id=")[1]
    url_get = "http://music.163.com/song/media/outer/url?id=" + id + ".mp3"

    file_path = "D:\\music_download\\" + id + ".mp3"
    tk.messagebox.showinfo("提醒!", "尝试下载中...")
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.159 Safari/537.36"}
    r = requests.get(str(url_get), headers=headers)

    try:
        if r.status_code == requests.codes.ok:
            with open(file_path, 'wb') as fp:
                fp.write(r.content)
            tk.messagebox.showinfo("好耶!!", "下载成功DA☆ZE")
    except ValueError:
        tk.messagebox.showinfo("haiya...", "请检查一下自己的url拼写!")
    except OSError:
        tk.messagebox.showinfo("haiya...", "remake罢, 请")
    except IndexError:
        tk.messagebox.showinfo("haiya...", "那么着急干嘛\n先去复制url")
    except TypeError:
        tk.messagebox.showinfo("haiya...", "虽然我也不知道为什么出错了\n但是就是有bug(＠_＠;)")


save_button = tkinter.Button(windows, text="神奇的下载按钮~",
                             fg="black",
                             bg="white",
                             relief=RIDGE,
                             font=('微软雅黑', 12, 'bold'),
                             command=save_file)
save_button.place(relx=0.8, rely=0.4)
save_button.pack()
convert_button = tkinter.Button(windows, text="神奇的转换按钮~",
                                fg="black",
                                bg="white",
                                relief=RIDGE,
                                font=('微软雅黑', 12, 'bold'),
                                command=convert)
convert_button.place(relx=0.3, rely=0.4, )
convert_button.pack()
t = Text(windows, width=50, font='微软雅黑')
t.pack()

windows.mainloop()
