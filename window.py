from main import *
from tkinter import Tk, Label, Button, Entry, Frame, StringVar, LEFT, messagebox, BOTTOM

# Window
root = Tk()
root.geometry('700x200')
root.title('Player score changer')
root.config()

# Labels and Buttons
top_frame = Frame(root)
bottom_frame = Frame(root)
bottom_frame2 = Frame(root)

entr1_var = StringVar(root)
id_status = 'text'

current_player = None

def check_id():
    global current_player

    try:
        show_text = 'ID ALREADY!'
        mg = messagebox.Message(root, message=show_text, title="ID Status")

        current_player = Player(entr1_var.get())
        if not current_player.work_id:
            current_player = None
            show_text = 'ID DONT WORK!!!'
            entr1_var.set('')
            mg = messagebox.Message(root, message=show_text, title="ID Status", icon=messagebox.ERROR)

        mg.show()
    
    except: pass

title_f1 = Label(top_frame, text='Enter ID and click "Check"')
entr_f1 = Entry(top_frame, textvariable=entr1_var, justify='center')
btn_f1 = Button(top_frame, text='Check', command=check_id)

# mg = messagebox.Message(root, message=id_status, title='ID status')

# money=0, vip=0, admin=0, license=0, ban=0, gametime=0, item_slot='', item_count='', hero_status='', gm_arena=0, gm_camp=0, gm_summer=0, hash=''

# Packs
top_frame.pack()
bottom_frame.pack()
bottom_frame2.pack(fill='x')

title_f1.pack(fill='x')
entr_f1.pack(side=LEFT, fill='x')
btn_f1.pack(side=LEFT, fill='x')



# c1
c1 = Frame(bottom_frame)
entry_var_c1 = StringVar(root, value='100')
title_c1 = Label(c1, text='MONEY:')
entry_c1 = Entry(c1, textvariable=entry_var_c1, justify='center')

title_c1.pack()
entry_c1.pack()

# c2
c2 = Frame(bottom_frame)
entry_var_c2 = StringVar(root, value='0')
title_c2 = Label(c2, text='VIP:')
entry_c2 = Entry(c2, textvariable=entry_var_c2, justify='center')

title_c2.pack()
entry_c2.pack()

# c3
c3 = Frame(bottom_frame)
entry_var_c3 = StringVar(root, value='0')
title_c3 = Label(c3, text='ADMIN:')
entry_c3 = Entry(c3, textvariable=entry_var_c3, justify='center')

title_c3.pack()
entry_c3.pack()

# c4
c4 = Frame(bottom_frame)
entry_var_c4 = StringVar(root, value='0')
title_c4 = Label(c4, text='LICENSE:')
entry_c4 = Entry(c4, textvariable=entry_var_c4, justify='center')

title_c4.pack()
entry_c4.pack()

# c5
c5 = Frame(bottom_frame)
entry_var_c5 = StringVar(root, value='0')
title_c5 = Label(c5, text='BAN:', fg='#f00000')
entry_c5 = Entry(c5, textvariable=entry_var_c5, justify='center')

title_c5.pack()
entry_c5.pack()

# c6
c6 = Frame(bottom_frame2)
entry_var_c6 = StringVar(root, value='')
title_c6 = Label(c6, text='ITEM SLOT:', fg='#f0f', width=20)
entry_c6 = Entry(c6, textvariable=entry_var_c6, justify='center', width=70)

title_c6.pack(side=LEFT)
entry_c6.pack(side=LEFT, fill='x')

# c7
c7 = Frame(bottom_frame2)
entry_var_c7 = StringVar(root, value='')
title_c7 = Label(c7, text='ITEM COUNT:', fg='#f0f', width=20)
entry_c7 = Entry(c7, textvariable=entry_var_c7, justify='center', width=70)

title_c7.pack(side=LEFT)
entry_c7.pack(side=LEFT, fill='x')

# c8
c8 = Frame(bottom_frame2)
entry_var_c8 = StringVar(root, value='')
title_c8 = Label(c8, text='HERO STATUS:', fg='#f0f', width=20)
entry_c8 = Entry(c8, textvariable=entry_var_c8, justify='center', width=70)

title_c8.pack(side=LEFT)
entry_c8.pack(side=LEFT, fill='x')

# Pack Frames
c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)
c4.pack(side=LEFT)
c5.pack(side=LEFT)
c6.pack()
c7.pack()
c8.pack()



def send_score():
    try:
        current_player.set_score(money = entry_var_c1.get(), vip=entry_var_c2.get(), admin=entry_var_c3.get(), license=entry_var_c4.get(), ban=entry_var_c5.get(), item_slot=entry_var_c6.get(), item_count=entry_var_c7.get(), hero_status=entry_var_c8.get())
        mg = messagebox.Message(root, message='Score has been updated!', title='Sended message')
        mg.show()
    except: pass

# Send Button
send_button = Button(root, text='SEND', command=send_score)
send_button.pack(fill='x')

def show_score():
    try:
        mg = messagebox.Message(root, message=current_player.score, title='Player information')
        mg.show()
    except: pass

show_button = Button(root, text='SHOW SCORE', command=show_score)
show_button.pack(fill='x')

# Loop window
root.mainloop()