import tkinter as tk
window = tk.Tk()
main_frame = tk.Frame(window)
main_frame.pack(expand=True, pady=20)

def handle_click():
      F = float(ent_name.get())
      run_Ans = (F-32)*5/9
      Ans.config(text=f"{run_Ans:.2f}°C")

def handle_keypess(event):
      print(event.char)


lbl_name = tk.Label(main_frame,text="°F(fahrenheit)")
ent_name = tk.Entry(main_frame,text="text",fg="black",width=10)
btn_click = tk.Button(main_frame,text="=",command=handle_click)
Ans = tk.Label(main_frame,text="100°C")

ent_name.pack(side=tk.LEFT)
lbl_name.pack(side=tk.LEFT)
btn_click.pack(side=tk.LEFT)
Ans.pack(side=tk.LEFT)

window.bind("<Key>",handle_keypess)
window.mainloop()