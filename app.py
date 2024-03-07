import tkinter as tk
window = tk.Tk()

lbl_name = tk.Label(text="Please input name:")
ent_name = tk.Entry()
def handle_click():
      name=ent_name.get()
      lbl_greet=tk.Label(text=name,bg="pink",fg='red')
      lbl_greet.pack()

btn_click = tk.Button(text="Clickme!",command=handle_click)
lbl_name.pack()
ent_name.pack()
btn_click.pack()


def handle_keypess(event):
      print(event.char)

window.bind("<Key>",handle_keypess)
window.mainloop()