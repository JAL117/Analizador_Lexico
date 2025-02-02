---

# **Analizador Léxico en Python**

## **Descripción del Repositorio**

Es un **analizador léxico** desarrollado en **Python**, diseñado para escanear código fuente y convertirlo en una secuencia de **tokens**. Utiliza **expresiones regulares (RegEx)** y un **Autómata Finito Determinista (AFD)** para reconocer identificadores, números, operadores y palabras clave en un lenguaje de programación definido.

## **Características**
- ✅ Reconocimiento de **tokens**: palabras clave, identificadores, números, operadores y delimitadores.
- ✅ Implementado con **expresiones regulares** y técnicas de **teoría de autómatas**.
- ✅ Soporte para **comentarios y espacios en blanco**.
- ✅ Salida en formato **JSON** para facilitar el análisis sintáctico.
- ✅ Código modular con pruebas unitarias en **unittest**.
- ✅ Interfaz gráfica (GUI) con **tkinter**.

## **Estructura del Proyecto**
```plaintext
/LexiPy/
│
├── src/                # Código fuente
│   ├── lexer.py        # Implementación del lexer
│   ├── token_types.py  # Definición de tipos de tokens
│   └── file_handler.py # Gestión de archivos
│
├── test/               # Pruebas unitarias
│   └── test_lexer.py
│
├── input/              # Archivos de entrada
│   └── example.txt
│
├── output/             # Tokens generados
│   └── tokens.json
│
├── interface.py        # Interfaz gráfica (GUI)
├── requirements.txt    # Dependencias
├── README.md           # Documentación
└── .gitignore          # Archivos ignorados por Git
```

## **Instalación de Dependencias**

### 1️⃣ **Clona el repositorio**  
```bash
git clone https://github.com/JesusHernandez223258/LexiPy.git
cd LexiPy
```

### 2️⃣ **Instala dependencias**  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Instala Tkinter (si es necesario)**  
En algunas distribuciones de Linux, `tkinter` no viene preinstalado. Si obtienes un error relacionado con `tkinter`, instálalo manualmente:

- **Fedora**:  
  ```bash
  sudo dnf install python3-tkinter
  ```

- **Debian/Ubuntu**:  
  ```bash
  sudo apt install python3-tk
  ```

- **Arch Linux**:  
  ```bash
  sudo pacman -S tk
  ```

### 4️⃣ **Ejecuta el analizador léxico**  
```bash
python src/lexer.py
```

### 5️⃣ **Ejecuta la interfaz gráfica (GUI)**  
```bash
python interface.py
```

### 6️⃣ **Verifica los tokens generados en `output/tokens.json`**  

---

## **Ejemplo de Uso**

### **Interfaz Gráfica (GUI)**
La interfaz gráfica te permite cargar un archivo de código fuente, analizarlo y ver los tokens generados en una ventana interactiva.

1. Ejecuta la GUI:
   ```bash
   python interface.py
   ```
2. Carga un archivo de código fuente desde la interfaz.
3. Haz clic en "Analizar" para generar los tokens.
4. Los tokens se mostrarán en la ventana y se guardarán en `output/tokens.json`.

---