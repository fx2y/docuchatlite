import os
import tkinter as tk

from document_chunker import DocumentChunker
from file_saver import FileSaver
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
    for file_path in file_paths:
        text = file_converter.convert_to_text(file_path)
        document_chunker = DocumentChunker(window_size=100, stride=50)
        chunks = document_chunker.generate_chunks(text)
        for chunk in chunks:
            file_saver = FileSaver("storage")
            file_id = file_saver.save_file(chunk)
            print(file_id)

            file_path = os.path.join("storage", f"{file_id}.txt")
            with open(file_path, "r") as f:
                text = f.read()
                print(text)


convert_button = tk.Button(
    root,
    text="Convert Files",
    command=convert_files
)
convert_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
