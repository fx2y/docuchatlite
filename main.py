import tkinter as tk
from file_selector import FileSelector

root = tk.Tk()
file_selector = FileSelector(root)
file_selector.create_file_selector_ui()
root.mainloop()

# To get the selected file paths:
file_paths = file_selector.get_file_paths()
print(file_paths)
