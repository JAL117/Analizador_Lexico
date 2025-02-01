import tkinter as tk
from tkinter import scrolledtext, messagebox
from file_loader import load_file
from lexer import tokenize_with_count

code_content = None

def load_code():
    global code_content
    code_content = load_file()
    if code_content is not None:
        messagebox.showinfo("Archivo Cargado", "El archivo se ha cargado correctamente.")

def analyze_code():
    if code_content is None:
        messagebox.showwarning("Advertencia", "No hay ningún archivo cargado.")
        return

    try:
        tokens, token_count = tokenize_with_count(code_content)
        text_output.delete("1.0", tk.END)
        
        text_output.insert(tk.END, "Tokens encontrados:\n")
        for token in tokens:
            text_output.insert(tk.END, f"{token}\n")

        text_output.insert(tk.END, "\nConteo de Tokens:\n")
        for token_type, count in token_count.items():
            text_output.insert(tk.END, f"{token_type}: {count}\n")

    except SyntaxError as e:
        messagebox.showerror("Syntax Error", str(e))


root = tk.Tk()
root.title("Analizador Léxico")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

btn_load = tk.Button(frame, text="Cargar Archivo", command=load_code)
btn_load.pack()

btn_analyze = tk.Button(frame, text="Analizar", command=analyze_code)
btn_analyze.pack()

text_output = scrolledtext.ScrolledText(frame, width=60, height=25)
text_output.pack()

root.mainloop()