import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="grey")
window.geometry("300x200")
window.resizable(False,False)
window.title("say Hello")

# function & variable
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def click_button():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"{NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, ganteng sekali..."
    showinfo(title="say hello",message=pesan)

# frame input
input_frame = ttk.Frame(window)

# penempatan grid,pack, dan place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen
# label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang:")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# tombol
hello_button = ttk.Button(input_frame,text="say hi!",command=click_button)
hello_button.pack(fill='x',expand=True,padx=10,pady=10)

# main loop window
window.mainloop()
