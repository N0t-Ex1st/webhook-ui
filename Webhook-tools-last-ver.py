import random
import time
import requests
from tkinter import *
from tkinter import messagebox


def webhook():
    global w
    global hook_text
    try:
        root.destroy()
    except:
        pass
    w = Tk()
    w.title('Webhook tools by Anonym')
    w['bg'] = '#323232'
    w.geometry('300x200')

    title = Label(text="Enter webhook", bg='#323232', fg='#601ba6', font='Comfortaa 15')
    title.pack()

    hook_text = Entry(w, bg='#323232')
    hook_text.pack()

    cont_btn = Button(w, text='Ok', bg='#601ba6', width='15', activebackground='#601ba6', command=main)
    cont_btn.place(y=53, x=92)

    wl = Label(text='by Anonym', bg='#323232', fg='#601ba6', font='Consolas 12')
    wl.place(y=170, x=200)

    w.mainloop()


def main():
    global hook
    global root
    try:
        hook = hook_text.get()
        w.destroy()
    except:
        pass
    try:
        spam.destroy()
    except:
        pass
    try:
        inf.destroy()
    except:
        pass

    root = Tk()
    root.title('Main menu by Anonym')
    root['bg'] = '#323232'
    root.geometry('400x350')

    maintitle = Label(text="Main menu", bg='#323232', fg='#601ba6', font='Comfortaa 15')
    maintitle.pack()

    sbtn = Button(root, text='Spammer', bg='#601ba6', width='15', height='3', font='Comfortaa 15',
                  activebackground='#601ba6', command=spammer)
    sbtn.place(y=50, x=10)

    tbtn = Button(root, text='Terminate', bg='#601ba6', width='15', height='3', font='Comfortaa 15',
                  activebackground='#601ba6', command=terminate)
    tbtn.place(y=50, x=217)

    ibtn = Button(root, text='Info grabber', bg='#601ba6', width='15', height='3', font='Comfortaa 15',
                  activebackground='#601ba6', command=info)
    ibtn.place(y=200, x=10)

    bbtn = Button(root, text='Back to hook enter', bg='#601ba6', width='15', height='3', font='Comfortaa 15',
                  activebackground='#601ba6', command=webhook)
    bbtn.place(y=200, x=217)

    wl = Label(text='by Anonym', bg='#323232', fg='#601ba6', font='Consolas 12')
    wl.place(y=325, x=310)

    root.mainloop()


mesc = 0


def spammer():
    global nametoogle, spam
    root.destroy()

    spam = Tk()
    spam.title('Spammer by Anonym')
    spam['bg'] = '#323232'
    spam.geometry('400x350')
    check = BooleanVar()
    check.set(True)

    title = Label(text='Discord webhook spammer', bg='#323232', fg='#601ba6', font='Comfortaa 15')
    title.pack()

    def nametoogle():
        global nametitle, INmess, countt, INcount, messstitle, INmesss, counttt, INcountt, INname, messtitle
        global boo, mescount, mesc, txt
        txt = StringVar()
        txt.set(f"Message sent: {mesc}!")

        boo = check.get()

        if boo:
            try:
                messstitle.destroy()
                INmesss.destroy()

                counttt.destroy()
                INcountt.destroy()
            except:
                pass

            nametitle = Label(text='Enter name for webhook', bg='#323232', fg='#601ba6', font='Consolas 12')
            nametitle.pack()

            INname = Entry(spam, bg='#404040', fg='#601ba6')
            INname.pack()

            messtitle = Label(text='Enter message for spam', bg='#323232', fg='#601ba6', font='Consolas 12')
            messtitle.place(y=75, x=100)

            INmess = Entry(spam, bg='#404040', fg='#601ba6')
            INmess.place(y=100, x=138)

            countt = Label(text='Enter count message', bg='#323232', fg='#601ba6', font='Consolas 12')
            countt.place(y=125, x=115)

            INcount = Entry(spam, bg='#404040', fg='#601ba6')
            INcount.place(y=150, x=138)

            spammbtn = Button(spam, text='Send', bg='#601ba6', width='20', activebackground='#601ba6', command=ONspam)
            spammbtn.place(y=175, x=125)

        elif not boo:
            try:
                nametitle.destroy()
                INname.destroy()

                messtitle.destroy()
                INmess.destroy()

                countt.destroy()
                INcount.destroy()
            except:
                pass

            messstitle = Label(text='Enter message for spam', bg='#323232', fg='#601ba6', font='Consolas 12')
            messstitle.place(y=30, x=100)

            INmesss = Entry(spam, bg='#404040', fg='#601ba6')
            INmesss.place(y=55, x=138)

            counttt = Label(text='Enter count message', bg='#323232', fg='#601ba6', font='Consolas 12')
            counttt.place(y=75, x=115)

            INcountt = Entry(spam, bg='#404040', fg='#601ba6')
            INcountt.place(y=100, x=138)

        mescount = Label(textvariable=txt, bg='#323232', fg='#601ba6', font='Consolas 12')
        mescount.place(y=205, x=125)

        mbtn = Button(spam, text='Back to main menu', bg='#601ba6', width='20', activebackground='#601ba6',
                      command=main)
        mbtn.place(y=325, x=1)

        wl = Label(text='by Anonym', bg='#323232', fg='#601ba6', font='Consolas 12')
        wl.place(y=325, x=315)

    nameCh = Checkbutton(text='Edit name', variable=check, command=nametoogle,
                         bg='#323232', fg='#601ba6', activebackground='#323232', activeforeground='#601ba6',
                         selectcolor='#323232', font='Comfortaa 10')
    nameCh.place(y=30, x=300)
    nametoogle()

    spam.mainloop()


def ONspam():
    global count, payload, mesc, counter
    payload = {}
    counter = 0

    if requests.get(hook).json()["message"] != "Unknown Webhook":
        pass
    else:
        messagebox.showerror(title='Error', message="Webhook doesn't exist")
        return

    try:
        count = int(INcount.get())
    except:
        messagebox.showerror(title='Error', message='Invalid count of message')
        return

    try:
        if INmess.get() != "":
            if len(INmess.get()) <= 2000:
                payload["content"] = INmess.get()
            else:
                messagebox.showerror(title='Error', message='Only 2000 characters allowed in the message!')
                return
        else:
            messagebox.showerror(title='Error', message='Invalid message')
            return
    except:
        messagebox.showerror(title='Error', message='Invalid message')
        return

    if boo:
        try:
            if INname.get() != "":
                if len(INname.get()) <= 80:
                    payload["username"] = INname.get()
                else:
                    messagebox.showerror(title='Error', message='Only 80 characters allowed in the name!')
                    return
            else:
                messagebox.showerror(title='Error', message='Invalid name')
                return
        except:
            messagebox.showerror(title='Error', message='Invalid name')
            return

    while counter < count:
        try:
            sender()
        except:
            messagebox.showerror(title='Error', message="Unknown error")
            return


def sender():
    global mesc, counter
    time.sleep(random.uniform(0.05, 0.3))
    req = requests.post(hook, json=payload)
    if req.status_code == 204:
        mesc += 1
        counter += 1
        txt.set(f"Message sent: {mesc}!")
        spam.update()
    elif req.status_code == 429:
        if req.json()["message"] == "You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently. Please read our docs at https://discord.com/developers/docs/topics/rate-limits to prevent this moving forward.":
            txt.set("You are being blocked from accessing Discord API...")
            spam.update()
            return
        else:
            cd = int(req.json()['retry_after']) / 1000
            txt.set(f"Message sent: {mesc}!\nWaiting cooldown... {cd}s")
            spam.update()
            time.sleep(cd)


def terminate():
    x = messagebox.askquestion(title='Sure?', message='Do you really want to delete this webhook?', icon='warning')
    if x == 'yes':
        try:
            nuke = requests.delete(hook)
            if nuke.status_code == 204:
                messagebox.showinfo(title='Successful', message='Term is done')
            else:
                messagebox.showerror(title='Error', message="Webhook doesn't exist")
        except:
            messagebox.showerror(title='Error', message='Unknown error')
    else:
        return


def grab():
    infg = StringVar()

    def cop():
        inf.clipboard_append(f'Name: {Wname}, Avatar: {avatar}, Server ID: {servid}')
        inf.update()

    if requests.get(hook).json()["message"] != "Unknown Webhook":
        pass
    else:
        messagebox.showerror(title='Error', message="Webhook doesn't exist")
        return

    try:
        gbtn.destroy()
        ghk = requests.get(hook, headers={"content-type": "application/json"}).json()
        Wname = ghk["name"]
        avatar = ghk["avatar"]
        if avatar is None:
            avatar = "Default"
        servid = ghk["guild_id"]

        infg.set(f'Name: {name}\nAvatar: {avatar}\nServer ID: {servid}')

        out = Label(textvariable=infg, bg='#323232', fg='#601ba6', font='Consolas 12')
        out.pack()

        cbtn = Button(inf, text='Copy info in clipboard', bg='#601ba6', width='20', activebackground='#601ba6',
                      command=cop)
        cbtn.pack()

    except:
        messagebox.showerror(title='Error', message="Unknown error")
        return


def info():
    global inf, gbtn
    root.destroy()
    inf = Tk()

    inf.title('Info grabber by Anonym')
    inf.geometry('550x300')
    inf['bg'] = '#323232'

    title = Label(text='Info webhook grabber', bg='#323232', fg='#601ba6', font='Comfortaa 15')
    title.pack()

    bbtn = Button(inf, text='Back to main menu', bg='#601ba6', width='20', activebackground='#601ba6', command=main)
    bbtn.place(y=275, x=1)

    gbtn = Button(inf, text='Grab info', bg='#601ba6', width='20', activebackground='#601ba6', command=grab)
    gbtn.pack()

    wl = Label(text='by Anonym', bg='#323232', fg='#601ba6', font='Consolas 12')
    wl.place(y=275, x=460)

    inf.mainloop()


if __name__ == '__main__':
    webhook()
