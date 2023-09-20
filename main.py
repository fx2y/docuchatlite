import tkinter as tk
from file_selector import FileSelector

root = tk.Tk()
file_selector = FileSelector(root)
file_selector.create_file_selector_ui()
root.mainloop()

# To get the selected file paths:
file_paths = file_selector.get_file_paths()
print(file_paths)

# To check if a file path is in a supported format:
file_path = "example.pdf"
is_supported = file_selector.is_supported_format(file_path)
print(is_supported)
