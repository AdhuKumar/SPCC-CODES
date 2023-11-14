import tkinter as tk

class TextEditor:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Text Editor")
    self.text_area = tk.Text(self.root, width=60, height=30)
    self.text_area.pack()

    self.menu_bar = tk.Menu(self.root)
    self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.file_menu.add_command(label="New", command=self.new_file)
    self.file_menu.add_command(label="Open", command=self.open_file)
    self.file_menu.add_command(label="Save", command=self.save_file)
    self.file_menu.add_separator()
    self.file_menu.add_command(label="Exit", command=self.exit)
    self.menu_bar.add_cascade(label="File", menu=self.file_menu)
    self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.edit_menu.add_command(label="Undo", command=self.undo)
    self.edit_menu.add_command(label="Redo", command=self.redo)
    self.edit_menu.add_separator()
    self.edit_menu.add_command(label="Cut", command=self.cut)
    self.edit_menu.add_command(label="Copy", command=self.copy)
    self.edit_menu.add_command(label="Paste", command=self.paste)
    self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

    self.root.config(menu=self.menu_bar)

    self.root.mainloop()

  def new_file(self):
    self.text_area.delete("1.0", tk.END)

  def open_file(self):
    file_name = tk.filedialog.askopenfilename(defaultext=".txt")
    if file_name:
      with open(file_name, "r") as f:
        self.text_area.insert("1.0", f.read())

  def save_file(self):
    file_name = tk.filedialog.asksaveasfilename(defaultext=".txt")
    if file_name:
      with open(file_name, "w") as f:
        f.write(self.text_area.get("1.0", tk.END))

  def exit(self):
    self.root.destroy()

  def undo(self):
    self.text_area.edit_undo()

  def redo(self):
    self.text_area.edit_redo()

  def cut(self):
    self.text_area.event_generate("<<Cut>>")

  def copy(self):
    self.text_area.event_generate("<<Copy>>")

  def paste(self):
    self.text_area.event_generate("<<Paste>>")

if __name__ == "__main__":
  TextEditor()
