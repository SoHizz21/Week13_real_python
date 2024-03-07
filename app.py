import tkinter as tk
window = tk.Tk()

lbl_name = tk.Label(text="°F(fahrenheit)")
ent_name = tk.Entry(text="text",fg="black",width=10)
def handle_click():
      name=ent_name.get()
      lbl_greet=tk.Label(text=name,bg="pink",fg='red')
      lbl_greet.pack()

btn_click = tk.Button(text="=",command=handle_click)
Ans = tk.Label(text="100°C")


ent_name.pack(side=tk.LEFT)
lbl_name.pack(side=tk.LEFT)
btn_click.pack(side=tk.LEFT)
Ans.pack(side=tk.LEFT)

def handle_keypess(event):
      print(event.char)

window.bind("<Key>",handle_keypess)
window.mainloop()