import tkinter as tk
from tkinter import ttk
import json
import os
from tkinter import filedialog, messagebox
from src.file_handler import read_file
from src.lexer import lex

output_dir = os.path.join(os.getcwd(), "output")

def load_code():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        global code_content
        code_content = read_file(file_path)
        messagebox.showinfo("Archivo Cargado", "El archivo se ha cargado correctamente.")
        status_label.config(text="Archivo cargado: " + os.path.basename(file_path))

def analyze_code():
    if code_content is None:
        messagebox.showwarning("Advertencia", "No hay ningún archivo cargado.")
        return

    try:
        tokens = lex(code_content)
        for item in tree.get_children():
            tree.delete(item)

        for token in tokens:
            tree.insert("", tk.END, values=(token["type"], token["value"], token["line"], token["column"]))

        os.makedirs(output_dir, exist_ok=True)

        with open(os.path.join(output_dir, "tokens.json"), "w", encoding="utf-8") as file:
            json.dump(tokens, file, indent=2)

        messagebox.showinfo("Éxito", "Tokens guardados en 'output/tokens.json'")
        status_label.config(text="Tokens exportados a 'output/tokens.json'")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Analizador Léxico - GUI")
root.geometry("800x600")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", padding=20)

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

btn_load = ttk.Button(frame, text="Cargar Archivo", command=load_code)
btn_load.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

btn_analyze = ttk.Button(frame, text="Analizar Código", command=analyze_code)
btn_analyze.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

columns = ("type", "value", "line", "column")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("type", text="Tipo")
tree.heading("value", text="Valor")
tree.heading("line", text="Línea")
tree.heading("column", text="Columna")
tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

status_label = ttk.Label(frame, text="Estado: Esperando acción", font=("Helvetica", 10))
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

root.mainloop()
