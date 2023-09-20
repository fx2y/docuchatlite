import tkinter as tk
from file_selector import FileSelector
from file_converter import FileConverter

root = tk.Tk()

# Create file selector UI
file_selector = FileSelector(root)
file_selector.create_file_selector_ui()

# Create file converter
file_converter = FileConverter()


# Create file conversion UI
def convert_files():
    file_paths = file_selector.get_file_paths()
    texts = [file_converter.convert_to_text(file_path) for file_path in file_paths]
    for file_path, file_type, text in zip(file_paths, map(file_converter.detect_file_type, file_paths), texts):
        print(f"File path: {file_path}")
        print(f"File type: {file_type}")
        print(f"Text: {text}")
        print()


convert_button = tk.Button(
    root,
    text="Convert Files",
    command=convert_files
)
convert_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
