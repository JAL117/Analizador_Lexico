import tkinter as tk
from tkinter import ttk
import json
import os
from tkinter import filedialog, messagebox, scrolledtext
from src.lexer import lex

output_dir = os.path.join(os.getcwd(), "output")


def analyze_code_from_input():
    code_content = code_input.get("1.0", tk.END) 
    if not code_content.strip(): 
        messagebox.showwarning("Advertencia", "El área de entrada de código está vacía.")
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


def load_code():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code_content = file.read()
                code_input.delete("1.0", tk.END) 
                code_input.insert("1.0", code_content) 
            messagebox.showinfo("Archivo Cargado",
                                "El archivo se ha cargado correctamente en el área de texto.")
            status_label.config(text="Archivo cargado: " + os.path.basename(file_path))
        except Exception as e:
            messagebox.showerror("Error al cargar el archivo", str(e))


root = tk.Tk()
root.title("Analizador Léxico - GUI")


style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", padding=20)

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)



code_input = scrolledtext.ScrolledText(
    frame, wrap=tk.WORD, font=("Courier New", 12))
code_input.grid(row=0, column=0, columnspan=2,
                padx=10, pady=10, sticky="nsew")

btn_analyze_input = ttk.Button(
    frame, text="Analizar Código (Entrada)", command=analyze_code_from_input)
btn_analyze_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

btn_load = ttk.Button(frame, text="Cargar Archivo", command=load_code)
btn_load.grid(row=1, column=1, padx=10, pady=10, sticky="ew")


columns = ("type", "value", "line", "column")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("type", text="Tipo")
tree.heading("value", text="Valor")
tree.heading("line", text="Línea")
tree.heading("column", text="Columna")
tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


status_label = ttk.Label(
    frame, text="Estado: Esperando acción", font=("Helvetica", 10))
status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=3)  
frame.rowconfigure(1, weight=0)  
frame.rowconfigure(2, weight=2)  
frame.rowconfigure(3, weight=0) 


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()