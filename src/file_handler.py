import json

# Lee un archivo de entrada
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Escribe un archivo de salida
def write_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)