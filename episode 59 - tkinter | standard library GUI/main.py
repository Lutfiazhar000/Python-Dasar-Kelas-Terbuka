import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="grey")
window.geometry("300x200")
window.resizable(False,False)
window.title("say Hello")

# frame input
input_frame = ttk.Frame(window)

# penempatan grid,pack, dan place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen
# label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,pady=10,fill="x",expand=True)
# entry nama depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame,NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=10,fill="x",expand=True)


window.mainloop()
