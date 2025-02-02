import tkinter as tk
import json
import os
from tkinter import filedialog, scrolledtext, messagebox
from src.file_handler import read_file
from src.lexer import lex


# Definir la ruta absoluta para 'output'
output_dir = os.path.join(os.getcwd(), "output")

def load_code():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        global code_content
        code_content = read_file(file_path)
        messagebox.showinfo("Archivo Cargado", "El archivo se ha cargado correctamente.")


def analyze_code():
    if code_content is None:
        messagebox.showwarning("Advertencia", "No hay ningún archivo cargado.")
        return

    try:
        tokens = lex(code_content)
        text_output.delete("1.0", tk.END)

        text_output.insert(tk.END, "Tokens encontrados:\n")
        for token in tokens:
            text_output.insert(tk.END, f"{token}\n")

        # Crear la carpeta 'output/' si no existe
        os.makedirs(output_dir, exist_ok=True)

        # Guardar tokens en un archivo JSON dentro de la carpeta 'output'
        with open(os.path.join(output_dir, "tokens.json"), "w", encoding="utf-8") as file:
            json.dump(tokens, file, indent=2)

        text_output.insert(tk.END, "\nTokens guardados en 'output/tokens.json'\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Crear la ventana principal
root = tk.Tk()
root.title("Analizador Léxico - GUI")
root.geometry("600x500")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

btn_load = tk.Button(frame, text="Cargar Archivo", command=load_code)
btn_load.pack()

btn_analyze = tk.Button(frame, text="Analizar Código", command=analyze_code)
btn_analyze.pack()

text_output = scrolledtext.ScrolledText(frame, width=70, height=25)
text_output.pack()

root.mainloop()
