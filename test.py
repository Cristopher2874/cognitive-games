import tkinter as tk

def mostrar_matriz():
    # Matriz de 10 filas y 2 columnas con texto en la columna 1 y números en la columna 2
    matriz = [
        ["Elemento 1,1", 10],
        ["Elemento 2,1", 20],
        ["Elemento 3,1", 30],
        ["Elemento 4,1", 40],
        ["Elemento 5,1", 50],
        ["Elemento 6,1", 60],
        ["Elemento 7,1", 70],
        ["Elemento 8,1", 80],
        ["Elemento 9,1", 90],
        ["Elemento 10,1", 100]
    ]

    # Crear una nueva ventana de Tkinter
    ventana = tk.Tk()
    ventana.title("Matriz de 10x2")

    # Crear una etiqueta para mostrar la matriz
    texto = "\n".join([f"{fila[0]}:\t{fila[1]}" for fila in matriz])
    etiqueta = tk.Label(ventana, text=f"Matriz de 10x2:\n{texto}", font=("Arial", 12))
    etiqueta.pack(padx=20, pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    mostrar_matriz()
