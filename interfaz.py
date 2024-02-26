import tkinter as tk
from tkinter import ttk
import funcion


def check_code():
    # Limpia las tablas de tokens y errores antes de una nueva ejecución
    for item in token_table.get_children():
        token_table.delete(item)
    for item in error_table.get_children():
        error_table.delete(item)

    code = txt.get("1.0", tk.END).strip()
    if not code:
        result_label.config(text="No hay código para verificar.")
        return  

    # Realiza el análisis y obtiene los errores y tokens
    errores, tokens = funcion.analizar(code) 
    
    # Muestra los errores en la interfaz gráfica
    for error in errores:
        error_table.insert('', 'end', values=(error,))

    # Muestra los tokens en la interfaz gráfica
    for token_type, token_value in tokens:
        token_table.insert('', 'end', values=(token_type, token_value))
    
    

    if not errores:
        result_label.config(text="La sintaxis es correcta.")
    else:
        result_label.config(text="Se encontraron errores de sintaxis.")

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")
root.configure(bg='white')

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configuración del área de texto para ingresar código
codigo = '''numero => int(99)'''
txt = tk.Text(main_frame, width=40, height=20)
txt.grid(row=0, column=0, padx=10, pady=10)
txt.insert(tk.END, codigo)

# Botón para iniciar el análisis
btn = tk.Button(main_frame, text="Analizar", command=check_code, width=10, height=2)
btn.grid(row=1, column=0, padx=10, pady=10)

# Configuración del área para mostrar los tokens identificados
token_frame = ttk.LabelFrame(main_frame, text="Tokens", padding=10)
token_frame.grid(row=0, column=1, padx=10, pady=10)

token_table = ttk.Treeview(token_frame, columns=('Type', 'Value'), show='headings')
token_table.heading('Type', text='Token')
token_table.heading('Value', text='Valor')
token_table.pack()

# Configuración del área para mostrar los errores sintácticos
error_frame = ttk.LabelFrame(main_frame, text="Errores de Sintaxis", padding=10)
error_frame.grid(row=1, column=1, padx=10, pady=10)

error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings')
error_table.heading('Error', text='Mensaje de Error')
error_table.pack()

# Etiqueta para mostrar el resultado del análisis
result_label = tk.Label(main_frame, text="", fg="red")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
