from tkinter import *
from customtkinter import *
from uuid import uuid4
import json
import network

window = Tk()
window.resizable(False, False)
window.geometry("1150x650")
title = window.title("Slide! Slip! Nothing more!")

CHANNEL = 'x'
USER = ''

main_frame1_arr = []
main_frame2_arr = []
main_frame3_arr = []


def event_handler(**kwargs):
    if kwargs['action'] == 'move_task_to_right':
        move_task_to_right_with_id(kwargs['id'])
    elif kwargs['action'] == 'move_task_to_left':
        move_task_to_left_with_id(kwargs['id'])
    elif kwargs['action'] == 'delete_task':
        delete_task_with_id(kwargs['id'])
    elif kwargs['action'] == 'edit_task':
        edit_task_with_id(kwargs['id'], kwargs['text'])


network.connect(CHANNEL, USER, event_handler)


def data_sender(action, id):
    data = {'action': action, 'id': id}
    data_json = json.dumps(data)
    network.send(data_json)


def find_task_in_arrays(id):
    for i in main_frame3_arr:
        if i['id'] == id:
            return i
    for i in main_frame2_arr:
        if i['id'] == id:
            return i
    for i in main_frame1_arr:
        if i['id'] == id:
            return i


def move_task_to_right(frame, my_task, task):
    x = my_task.winfo_children()
    if frame._name in ['1', '2']:
        if frame._name == '1':
            add_task(main_frame2, x[0].cget('text'), None, task._name)
            my_task.destroy()
        elif frame._name == '2':
            add_task(main_frame3, x[0].cget('text'), None, task._name)
            my_task.destroy()


def move_task_to_right_with_id(id):
    task = find_task_in_arrays(id)
    move_task_to_right(task['task'].master, task['task'], task['task'])


def move_task_to_left(frame, my_task, task):
    x = my_task.winfo_children()
    if frame._name in ['3', '2']:
        if frame._name == '2':
            add_task(main_frame1, x[0].cget('text'), None, task._name)
            my_task.destroy()
        elif frame._name == '3':
            add_task(main_frame2, x[0].cget('text'), None, task._name)
            my_task.destroy()


def move_task_to_left_with_id(id):
    task = find_task_in_arrays(id)
    move_task_to_left(task['task'].master, task['task'], task['task'])


def delete_task(frame):
    frame.destroy()


def delete_task_with_id(id):
    task = find_task_in_arrays(id)
    delete_task(task['task'])


def edit_task(frame, label, text=None):
    def edit_task_button(edit_task):
        label.config(text=edit_task.get())
        newWindow.destroy()
    if text:
        edit_task_button(text)

    newWindow = Toplevel(window)
    t = label.cget("text")

    newWindow.title(f"edit { t }")

    newWindow.geometry("500x100")
    edit_task = StringVar()
    Label(newWindow, text="make new name for this task.").pack()
    edit_task_entry1 = Entry(
        newWindow, textvariable=edit_task, width="42")
    edit_task_entry1.pack()

    submit_edit = Button(newWindow,
                         text="edit", command=lambda: edit_task_button(edit_task)).pack(side="bottom")


def edit_task_with_id(id, text):
    task = find_task_in_arrays(id)
    edit_task(task['task'], task['task'].nametowidget('.!label'), text)


def add_task(task_frame, text, entry, id):
    if id:
        for i in main_frame3_arr:
            if i['id'] == id:
                main_frame3_arr.remove(i)
        for i in main_frame2_arr:
            if i['id'] == id:
                main_frame2_arr.remove(i)
        for i in main_frame1_arr:
            if i['id'] == id:
                main_frame1_arr.remove(i)
    if not id:
        id = str(uuid4())
    assigned_task_frame = Frame(
        task_frame, background="black", padx="3", pady="2", name=id)
    assigned_task_frame.pack(side="top", expand=False, fill="x")
    assigned_task_frame.config(height="50")
    added_todo_task_text = Label(
        assigned_task_frame, text=text, bg="light green", padx="3", pady="1")
    added_todo_task_text.pack(side="left")

    edit_button = Button(assigned_task_frame,
                         text="edit", command=lambda: edit_task(assigned_task_frame, added_todo_task_text)).pack(side="right")
    move_button2 = Button(assigned_task_frame,
                          text="->", command=lambda: move_task_to_right(task_frame, assigned_task_frame, assigned_task_frame)).pack(side="right")
    move_button = Button(assigned_task_frame,
                         text="<-", command=lambda: move_task_to_left(task_frame, assigned_task_frame, assigned_task_frame)).pack(side="right")

    delete_button = Button(assigned_task_frame,
                           text="delete", command=lambda: delete_task(assigned_task_frame)).pack(side="right")

    if task_frame._name == '1':
        main_frame1_arr.append({'id': id, 'task': assigned_task_frame})
    elif task_frame._name == '2':
        main_frame2_arr.append({'id': id, 'task': assigned_task_frame})
    else:
        main_frame3_arr.append({'id': id, 'task': assigned_task_frame})

    if (entry):
        entry.delete(0, END)


def login(username, window_login):
    USER = username.get()
    window_login.destroy()
    window.deiconify()


if __name__ == '__main__':

    top_frame = Frame(window, background="blue")
    top_frame.pack(side="top", fill="x", padx="2", pady="2")
    top_frame.config(height="120")

    bottom_frame = Frame(window, background="red", padx="2", pady="2")
    bottom_frame.pack(expand=True, fill=BOTH)

    # to do column
    todo_frame = Frame(bottom_frame, name="to do", background="black")
    todo_frame.pack(side="left", expand=True, fill=BOTH)
    title_frame = Frame(todo_frame)
    todo_label = Label(title_frame, text="To Do").pack(
        anchor="n", expand=True, fill="x")

    # in progress column
    inprogress_frame = Frame(
        bottom_frame, name="in progress", background="yellow")
    inprogress_frame.pack(side="left", expand=True, fill=BOTH)

    # Done column
    done_frame = Frame(bottom_frame, name="done!", background="orange")
    done_frame.pack(side="left", expand=True, fill=BOTH)

    # # task line 1
    task_frame1 = Frame(todo_frame, background="purple")
    task_frame1.pack(anchor="n", fill="x")
    task_frame1.config(height="100", padx="2", pady="1")
    task_entry1_text = StringVar()
    add_task_entry1 = Entry(
        task_frame1, textvariable=task_entry1_text, width="42")
    add_task_entry1.pack(side="left")

    add_button1 = Button(task_frame1, text="ADD", height="1",
                         width="3", padx="2", pady="1", command=lambda: add_task(main_frame1, task_entry1_text.get(), add_task_entry1, None)).pack(side="right")

    # # main 1
    main_frame1 = Frame(todo_frame, background="green", name='1')
    main_frame1.pack(anchor="center", expand=True,
                     fill=BOTH, padx="3", pady="2")
    scrollbar1 = Scrollbar(main_frame1, bg="light blue",
                           borderwidth="1").pack(side=RIGHT, fill=BOTH)

    # # task line 2
    task_frame2 = Frame(inprogress_frame, background="grey")
    task_frame2.pack(anchor="n", fill="x")
    task_frame2.config(height="100", padx="2", pady="1")
    task_entry2_text = StringVar()
    add_task_entry2 = Entry(
        task_frame2, textvariable=task_entry2_text, width="42")
    add_task_entry2.pack(side="left")
    add_button2 = Button(task_frame2, text="ADD", height="1",
                         width="3", padx="2", pady="1", command=lambda: add_task(main_frame2, task_entry2_text.get(), add_task_entry2, None)).pack(side="right")
    # # main 2
    main_frame2 = Frame(inprogress_frame, background="blue", name='2')
    main_frame2.pack(anchor="center", expand=True,
                     fill=BOTH, padx="3", pady="2")
    scrollbar1 = Scrollbar(main_frame2, bg="light blue",
                           borderwidth="1").pack(side=RIGHT, fill=BOTH)
    assigned_task2 = Frame(main_frame2, background="purple").pack(
        anchor="center", expand=True, fill=BOTH, padx="3", pady="2")

    # # task line 3
    task_frame3 = Frame(done_frame, background="pink")
    task_frame3.pack(anchor="n", fill="x", padx="3", pady="2")
    task_frame3.config(height="100")
    task_entry3_text = StringVar()

    add_task_entry3 = Entry(task_frame3, width="42",
                            textvariable=task_entry3_text)
    add_task_entry3.pack(
        side="left", padx="3", pady='1')
    add_button3 = Button(task_frame3, text="ADD", padx="2",
                         pady="1", command=lambda: add_task(main_frame3, task_entry3_text.get(), add_task_entry3, None)).pack(side="right")

    # # main
    main_frame3 = Frame(done_frame, background="Red", name='3')
    main_frame3.pack(anchor="center", expand=True,
                     fill=BOTH, padx="3", pady="2")
    scrollbar1 = Scrollbar(main_frame3, bg="light blue",
                           borderwidth="1").pack(side=RIGHT, fill=BOTH)
    # login :
    window.withdraw()
    loginWindow = Toplevel()
    loginWindow.title(f"please enter username")
    loginWindow.geometry("500x100")
    username = StringVar()
    Label(loginWindow, text="please enter your username.").pack()
    edit_task_entry1 = Entry(
        loginWindow, textvariable=username, width="42")
    edit_task_entry1.pack()
    submit_edit = Button(loginWindow,
                         text="login", command=lambda: login(username, loginWindow)).pack(side="bottom")

    window.mainloop()
