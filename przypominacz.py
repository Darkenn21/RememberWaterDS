import tkinter as tk
from tkinter import messagebox
import time
import threading
# Funkcja do przypominania
def remind():
    while True:
        time.sleep(15)  # Przypomnienie co godzinę (można zmienić interwał)
        messagebox.showinfo("Przypomnienie", "Pora na szklankę wody!")

# Główna funkcja GUI
def start_app():
    root = tk.Tk()
    root.title("Przypominacz o wodzie")

    label = tk.Label(root, text="Aplikacja przypomina o piciu wody!", font=("Arial", 16))
    label.pack(pady=20)

    start_button = tk.Button(root, text="Start", command=lambda: threading.Thread(target=remind, daemon=True).start())
    start_button.pack(pady=10)

    exit_button = tk.Button(root, text="Zamknij", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_app()
