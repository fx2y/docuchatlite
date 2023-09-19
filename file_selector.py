import tkinter as tk

from tkinter import filedialog


class FileSelector:
    def __init__(self, root):
        self.root = root
        self.file_paths = []

    def select_files(self):
        file_types = (
            ("PDF files", "*.pdf"),
            ("Text files", "*.txt"),
            ("Word files", "*.docx"),
            ("All files", "*.*")
        )
        file_paths = filedialog.askopenfilenames(
            title="Select one or more files",
            filetypes=file_types
        )
        self.file_paths.extend(file_paths)

    def clear_files(self):
        self.file_paths = []

    def get_file_paths(self):
        return self.file_paths

    def create_file_selector_ui(self):
        select_button = tk.Button(
            self.root,
            text="Select Files",
            command=self.select_files
        )
        select_button.pack(side=tk.LEFT, padx=5, pady=5)

        clear_button = tk.Button(
            self.root,
            text="Clear Files",
            command=self.clear_files
        )
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)
