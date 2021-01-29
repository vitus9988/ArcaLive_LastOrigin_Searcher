from tkinter import *
from tkinter import ttk as ttk
import tkinter.messagebox as msgbox
import core_module as cm
import webbrowser
from tkinter import filedialog


root = Tk()
root.title("Arcalive Lastorigin Searcher 1.0.0")
root.geometry("640x480+600+300")
root.resizable(False, False)


########################################################################################################################
### main
########################################################################################################################


notebook = ttk.Notebook(root, width=740, height=580)
notebook.pack()

frame1 = Frame(root)
notebook.add(frame1, text=u"공략")
frame2 = Frame(root)
notebook.add(frame2, text=u"야짤")
frame3 = Frame(root)
notebook.add(frame3, text=u"창작물(야짤)")
frame4 = Frame(root)
notebook.add(frame4, text=u"Info")


########################################################################################################################
### listbox (공략)
########################################################################################################################

listbox = Listbox(frame1, selectmode="single", height=0)
listbox.pack(side="right", fill="both", expand=True)

entry_text = Entry(frame1, width=30)
entry_text.pack()
entry_text.insert(END, "")

radio_value = IntVar()

radio_btn1 = ttk.Radiobutton(frame1, text=u"제목+내용", variable=radio_value, value=0)
radio_btn2 = ttk.Radiobutton(frame1, text=u"제목만", variable=radio_value, value=1)

radio_btn1.pack()
radio_btn2.pack()
Label(frame1, text=u"검색어를 입력하세요.\n( ex) 1-1ex , 5-8ex+카엔 )").pack()


def weblink(*args):
    index = listbox.curselection()[0]
    item = listbox.get(index)
    if "https://" in item:
        webbrowser.open_new(item)


def error():
    msgbox.showwarning(u"경고", u"검색어를 입력하세요")


def search_btncmd():

    value = entry_text.get()
    listbox.delete(0, END)

    if len(value) == 0:
        error()
    else:
        data_arr = cm.NamuliveSearch(radio_value.get(), value)
        listbox.bind("<<ListboxSelect>>", weblink)
        for item in data_arr:
            listbox.insert(END, item)
            listbox.itemconfig(END, fg="red" if item[0] == "h" else "blue")
        listbox.pack(side="right", fill="both", expand=True)


def search_callback(event):
    search_btncmd()


root.bind("<Return>", search_callback)


########################################################################################################################
### listbox (야짤)
########################################################################################################################

yazzal_title = Label(frame2, text=u"아카라이브 야짤탭 다운로더입니다.")
yazzal_title.pack(side="top")
Label(frame2, text=u"이미지파일은 글번호+글제목 형태의 폴더에 개별저장됩니다.").pack()
#Label(frame2, text=u"(기본 페이지값은 1입니다.)").pack()

spin_label = Label(frame2, text=u"페이지 수를 입력하세요")
spin_label.pack()


def yazzal_spin_check(self):
    spin_label.config(text=u"다운받을 페이지를 입력하세요. (1~250)")
    valid = False
    if self.isdigit():
        if int(self) <= 250 and int(self) >= 1:
            valid = True
    elif self == '':
        valid = True
    return valid

def yazzal_spin_error(self):
    spin_label.config(text=u"최소 수치는 1\n최대 수치는 250입니다")


validate_command = (frame2.register(yazzal_spin_check), "%P")
invalid_command = (frame2.register(yazzal_spin_error), "%P")

yazzal_spinbox = Spinbox(frame2, from_=1, to=250, validate='all',
                         validatecommand=validate_command,
                         invalidcommand=invalid_command)
yazzal_spinbox.pack()


def yazzal_spinbox_value():
    return yazzal_spinbox.get()





def yazzal_error():
    msgbox.showwarning(u"경고", u"다운로드 폴더 경로를 지정하세요.")


def dir_btncmd():
    down_listbox.delete(0, END)
    dir_path = filedialog.askdirectory(parent=root, initialdir="/", title=u"다운로드 파일을 저장할 폴더를 선택하세요")
    if dir_path is None:
        pass
    else:
        down_listbox.insert(END, "{}".format(dir_path))
        down_listbox.place(x=80, y=103)


def down_alarm():
    msgbox.showwarning(u"작업완료", u"다운로드가 완료되었습니다.")


def down_btncmd():
    yazzal_page = int(yazzal_spinbox_value())
    try:
        dir_path = down_listbox.get(0, END)[0]
        if len(dir_path) == 0 or len(dir_path) == 1:
            yazzal_error()
        else:
            cm.created_img_download(dir_path, yazzal_page, 1)
            down_alarm()
    except IndexError:
        yazzal_error()


directory_btn = Button(frame2, width=10, text=u"경로지정", overrelief="solid",command=dir_btncmd)
down_listbox = Listbox(frame2, selectmode="single", height=0, width=40)
down_btn = Button(frame2, width=10, text=u"다운로드 시작", overrelief="solid",command=down_btncmd)

down_listbox.place(x=80, y=103)
directory_btn.place(x=380, y=100)
down_btn.place(x=480, y=100)



########################################################################################################################
### 창작물
########################################################################################################################
#
yazzal_title = Label(frame3, text=u"아카라이브 창작물(야짤)탭 다운로더입니다.")
yazzal_title.pack(side="top")
Label(frame3, text=u"이미지파일은 글번호+글제목 형태의 폴더에 개별저장됩니다.").pack()
#Label(frame2, text=u"(기본 페이지값은 1입니다.)").pack()

cre_spin_label = Label(frame3, text=u"페이지 수를 입력하세요")
cre_spin_label.pack()


def cre_yazzal_spin_check(self):
    cre_spin_label.config(text=u"다운받을 페이지를 입력하세요. (1~49)")
    valid = False
    if self.isdigit():
        if int(self) <= 49 and int(self) >= 1:
            valid = True
    elif self == '':
        valid = True
    return valid

def cre_yazzal_spin_error(self):
    cre_spin_label.config(text=u"최소 수치는 1\n최대 수치는 49입니다")


cre_validate_command = (frame3.register(cre_yazzal_spin_check), "%P")
cre_invalid_command = (frame3.register(cre_yazzal_spin_error), "%P")

cre_yazzal_spinbox = Spinbox(frame3, from_=1, to=250, validate='all',
                         validatecommand=cre_validate_command,
                         invalidcommand=cre_invalid_command)
cre_yazzal_spinbox.pack()


def cre_yazzal_spinbox_value():
    return cre_yazzal_spinbox.get()


def cre_yazzal_error():
    msgbox.showwarning(u"경고", u"다운로드 폴더 경로를 지정하세요.")


def cre_dir_btncmd():
    cre_down_listbox.delete(0, END)
    dir_path = filedialog.askdirectory(parent=root, initialdir="/", title=u"다운로드 파일을 저장할 폴더를 선택하세요")
    if dir_path is None:
        pass
    else:
        cre_down_listbox.insert(END, "{}".format(dir_path))
        cre_down_listbox.place(x=80, y=103)


def cre_down_alarm():
    msgbox.showwarning(u"작업완료", u"다운로드가 완료되었습니다.")


def cre_down_btncmd():
    cre_yazzal_page = int(cre_yazzal_spinbox_value())
    try:
        dir_path = cre_down_listbox.get(0, END)[0]
        if len(dir_path) == 0 or len(dir_path) == 1:
            cre_yazzal_error()
        else:
            cm.created_img_download(dir_path, cre_yazzal_page, 2)
            cre_down_alarm()
    except IndexError:
        cre_yazzal_error()



cre_directory_btn = Button(frame3, width=10, text=u"경로지정", overrelief="solid",command=cre_dir_btncmd)
cre_down_listbox = Listbox(frame3, selectmode=u"single", height=0, width=40)
cre_down_btn = Button(frame3, width=10, text=u"다운로드 시작", overrelief="solid",command=cre_down_btncmd)

cre_down_listbox.place(x=80, y=103)
cre_directory_btn.place(x=380, y=100)
cre_down_btn.place(x=480, y=100)



########################################################################################################################
### info
########################################################################################################################

def git_callback(event):
    webbrowser.open_new(event.widget.cget("text"))


Label(frame4, text="Copyright 2021. vitus9988 All Rights Reserved.").pack(side="bottom")
git_label = Label(frame4, text=r"https://github.com/vitus9988", fg="blue", cursor="hand2")
git_label.pack(side="bottom")
git_label.bind("<Button-1>", git_callback)
thanks_to = Label(frame4, text=r'Thanks To  SANIC , 섭섭맨').pack(side='bottom')


root.mainloop()

# pyinstaller -F core_gui.spec로 빌드