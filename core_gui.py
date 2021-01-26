from tkinter import *
from tkinter import ttk as ttk
import tkinter.messagebox as msgbox
import core_module as cm
import webbrowser
from tkinter import filedialog



root = Tk()
root.title("Arcalive Lastorigin Searcher")
root.geometry("640x480+600+300")
root.resizable(False, False)


########################################################################################################################
### main
########################################################################################################################


notebook = ttk.Notebook(root, width=740, height=580)
notebook.pack()

frame1 = Frame(root)
notebook.add(frame1, text='공략')
frame2 = Frame(root)
notebook.add(frame2, text='야짤')
frame4 = Frame(root)
notebook.add(frame4, text='Info')


########################################################################################################################
### listbox (공략)
########################################################################################################################

listbox = Listbox(frame1, selectmode='single', height=0)
listbox.pack(side='right', fill='both', expand=True)

entry_text = Entry(frame1, width=30)
entry_text.pack()
entry_text.insert(END, '')

radio_value = IntVar()

radio_btn1 = ttk.Radiobutton(frame1, text='제목+내용', variable=radio_value, value=0)
radio_btn2 = ttk.Radiobutton(frame1, text='제목만', variable=radio_value, value=1)

radio_btn1.pack()
radio_btn2.pack()
Label(frame1, text='검색어를 입력하세요.\n( ex) 1-1ex , 5-8ex+카엔 )').pack()


def weblink(*args):
    index = listbox.curselection()[0]
    item = listbox.get(index)
    if 'https://' in item:
        webbrowser.open_new(item)


def error():
    msgbox.showwarning("경고", "검색어를 입력하세요")


def search_btncmd():

    value = entry_text.get()
    listbox.delete(0, END)

    if len(value) == 0:
        error()
    else:
        data_arr = cm.NamuliveSearch(radio_value.get(), value)
        listbox.bind('<<ListboxSelect>>', weblink)
        for item in data_arr:
            listbox.insert(END, item)
            listbox.itemconfig(END,fg='red' if item[0] == 'h' else 'blue')
        listbox.pack(side='right', fill='both', expand=True)


def search_callback(event):
    search_btncmd()


root.bind('<Return>', search_callback)


########################################################################################################################
### listbox (야짤)
########################################################################################################################

yazzal_title = Label(frame2, text='아카라이브 야짤탭 다운로더입니다.')
yazzal_title.pack(side='top')
Label(frame2, text='이미지파일은 글번호+글제목 형태의 폴더에 개별저장됩니다.').pack()
Label(frame2, text='(기본 페이지값은 1입니다.)').pack()


def yazzal_error():
    msgbox.showwarning("경고", "다운로드 폴더 경로를 지정하세요.")


def dir_btncmd():
    down_listbox.delete(0, END)
    dir_path = filedialog.askdirectory(parent=root, initialdir="/", title='다운로드 파일을 저장할 폴더를 선택하세요')
    if dir_path == None:
        pass
    else:
        down_listbox.insert(END, '{}'.format(dir_path))
        down_listbox.place(x=80, y=63)


def down_alarm():
    msgbox.showwarning("작업완료", "다운로드가 완료되었습니다.")


def down_btncmd():
    try:
        dir_path = down_listbox.get(0, END)[0]
        if len(dir_path) == 0 or len(dir_path) == 1:
            yazzal_error()
        else:
            cm.created_img_download(dir_path, 1)
            down_alarm()
    except:
        yazzal_error()

directory_btn = Button(frame2, width=10, text='경로지정', overrelief='solid',command=dir_btncmd)
down_listbox = Listbox(frame2, selectmode='single', height=0, width=40)
down_btn = Button(frame2, width=10, text='다운로드 시작', overrelief='solid',command=down_btncmd)

down_listbox.place(x=80, y=63)
directory_btn.place(x=380, y=60)
down_btn.place(x=480, y=60)


########################################################################################################################
###info
########################################################################################################################
Label(frame4, text='Copyright 2021. test1423 All Rights Reserved.').pack(side='bottom')



root.mainloop()
