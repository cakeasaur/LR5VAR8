# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog


def main() -> None:
    root = tk.Tk()
    root.title("LR5VAR8 — Диалог выбора файла")
    root.geometry("520x140")

    selected_path = tk.StringVar(value="Файл не выбран")

    def choose_file() -> None:
        path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Все файлы", "*.*")],
        )
        if path:
            selected_path.set(path)

    frame = tk.Frame(root, padx=12, pady=12)
    frame.pack(fill="both", expand=True)

    title = tk.Label(frame, text="Диалог выбора файла (askopenfilename)")
    title.pack(anchor="w")

    entry = tk.Entry(frame, textvariable=selected_path)
    entry.pack(fill="x", pady=(8, 8))

    button = tk.Button(frame, text="Выбрать файл…", command=choose_file)
    button.pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()
