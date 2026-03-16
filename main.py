import tkinter as tk
from tkinter import filedialog, messagebox

# Main Window
root = tk.Tk()
root.title("Sakshi Sharma Text Editor")
root.geometry("900x600")

# Dark Mode Colors
bg_color = "#1e1e1e"
text_color = "#ffffff"

# Text Frame
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Text Area
text = tk.Text(
    frame,
    wrap=tk.WORD,
    font=("Helvetica", 12),
    yscrollcommand=scrollbar.set,
    bg=bg_color,
    fg=text_color,
    insertbackground="white"
)

text.pack(expand=True, fill="both")
scrollbar.config(command=text.yview)

# Status Bar
status = tk.Label(root, text="Lines: 1 | Words: 0", anchor="w")
status.pack(fill="x", side="bottom")

# Update Status Bar
def update_status(event=None):
    content = text.get(1.0, tk.END)
    lines = content.count("\n")
    words = len(content.split())
    status.config(text=f"Lines: {lines} | Words: {words}")

text.bind("<KeyRelease>", update_status)

# New File
def new_file(event=None):
    text.delete(1.0, tk.END)

# Open File
def open_file(event=None):
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Save File
def save_file(event=None):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully")

# Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New (Ctrl+N)", command=new_file)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Keyboard Shortcuts
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)

# Run App
root.mainloop()