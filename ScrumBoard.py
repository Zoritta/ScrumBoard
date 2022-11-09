from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *


window = Tk()
window.resizable(False, False)
window.geometry("900x650")
title = window.title("Slide! Slip! Nothing more!")


def add_task():
    assigned_task_frame = Frame(
        main_frame1, background="black", padx="3", pady="2")
    assigned_task_frame.pack(side="top", expand=False, fill="x")
    assigned_task_frame.config(height="50")
    added_todo_task_text = Label(
        assigned_task_frame, text=task_entry1_text.get(), bg="light green", padx="3", pady="1")
    added_todo_task_text.grid(row=0, column=0)

    # # Read the Image
    image = Image.open("download.png")

    # # Resize the image using resize() method
    resized_image = image.resize((20, 20))

    edit_button_photo = ImageTk.PhotoImage(resized_image)

    edit_button = Button(assigned_task_frame,
                         text="edit").grid(row=0, column=1)

    move_button = Button(assigned_task_frame,
                         text="move").grid(row=0, column=2)
    delete_button = Button(assigned_task_frame,
                           text="delete").grid(row=0, column=3)


top_frame = Frame(window, background="blue")
top_frame.pack(side="top", fill="x", padx="2", pady="2")
top_frame.config(height="120")


bottom_frame = Frame(window, background="red", padx="2", pady="2")
bottom_frame.pack(expand=True, fill=BOTH)

# delete_button_photo = PhotoImage(file=)
# add_button_photo = PhotoImage(file=)
# move_button_photo = PhotoImage(file=)


# to do column
todo_frame = Frame(bottom_frame, name="to do", background="black")
todo_frame.pack(side="left", expand=True, fill=BOTH)
title_frame = Frame(todo_frame)
todo_label = Label(title_frame, text="To Do").pack(
    anchor="n", expand=True, fill="x")

# in progress column
inprogress_frame = Frame(bottom_frame, name="in progress", background="yellow")
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
    task_frame1, textvariable=task_entry1_text, width="42").pack(side="left")


def add_button1_command():
    pass


add_button1 = Button(task_frame1, text="ADD", height="1",
                     width="3", padx="2", pady="1", command=add_task).pack(side="right")


# # main 1
main_frame1 = Frame(todo_frame, background="green")
main_frame1.pack(anchor="center", expand=True, fill=BOTH, padx="3", pady="2")
scrollbar1 = Scrollbar(main_frame1, bg="light blue",
                       borderwidth="1").pack(side=RIGHT, fill=BOTH)


# # botton line 1
# botton_frame1 = Frame(todo_frame, background="blue")
# botton_frame1.pack(anchor="s", fill="x")
# botton_frame1.config(height="100")
# edit_button1 = Button(botton_frame1, height="1",
#                       width="3").pack(anchor="center")


# # task line 2
task_frame2 = Frame(inprogress_frame, background="grey")
task_frame2.pack(anchor="n", fill="x")
task_frame2.config(height="100", padx="2", pady="1")
task_entry2_text = StringVar()
add_task_entry2 = Entry(
    task_frame2, textvariable=task_entry2_text, width="42").pack(side="left")
add_button2 = Button(task_frame2, text="ADD", height="1",
                     width="3", padx="2", pady="1").pack(side="right")

# # main 2
main_frame2 = Frame(inprogress_frame, background="blue")
main_frame2.pack(anchor="center", expand=True, fill=BOTH, padx="3", pady="2")
scrollbar1 = Scrollbar(main_frame2, bg="light blue",
                       borderwidth="1").pack(side=RIGHT, fill=BOTH)
assigned_task2 = Frame(main_frame2, background="purple").pack(
    anchor="center", expand=True, fill=BOTH, padx="3", pady="2")

# # botton line 2
# botton_frame2 = Frame(inprogress_frame, background="black")
# botton_frame2.pack(anchor="s", fill="x")
# botton_frame2.config(height="100")
# edit_button2 = Button(botton_frame2, height="1",
#                       width="3").pack(anchor="center")


# # task line 3
task_frame3 = Frame(done_frame, background="pink")
task_frame3.pack(anchor="n", fill="x", padx="3", pady="2")
task_frame3.config(height="100")
add_task_entry3 = Entry(task_frame3, width="42").pack(
    side="left", padx="3", pady='1')
# image = Image.open("zohre_bubble_image.png")
# resized_image2 = image.resize((20, 20))
add_button3 = Button(task_frame3, text="ADD", padx="2",
                     pady="1").pack(side="right")

# # main
main_frame3 = Frame(done_frame, background="green")
main_frame3.pack(anchor="center", expand=True, fill=BOTH, padx="3", pady="2")
scrollbar1 = Scrollbar(main_frame3, bg="light blue",
                       borderwidth="1").pack(side=RIGHT, fill=BOTH)

# # botton line
# botton_frame3 = Frame(done_frame, background="blue")
# botton_frame3.pack(anchor="s", fill="x")
# botton_frame3.config(height="100")
# edit_button3 = Button(botton_frame3, height="1",
#                       width="3").pack(anchor="center")


window.mainloop()
