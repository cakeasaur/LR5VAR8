# -*- coding: utf-8 -*-
import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Task 11 — Listbox и выбор элемента")
    root.geometry("420x260")

    items = ["Python", "Tkinter", "PyQt5", "Кнопки", "Поля ввода", "Списки"]

    selected_text = tk.StringVar(value="Выберите элемент из списка")

    def on_select(_: tk.Event) -> None:
        selection = listbox.curselection()
        if not selection:
            return
        index = selection[0]
        selected_text.set(f"Вы выбрали: {items[index]}")

    frame = tk.Frame(root, padx=12, pady=12)
    frame.pack(fill="both", expand=True)

    label = tk.Label(frame, text="Список (Listbox):")
    label.pack(anchor="w")

    listbox = tk.Listbox(frame, height=8)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.pack(fill="x", pady=(6, 10))

    listbox.bind("<<ListboxSelect>>", on_select)

    result = tk.Label(frame, textvariable=selected_text)
    result.pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()
