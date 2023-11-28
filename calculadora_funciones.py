import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('500x500')
        self.ventana.title("Calculadora")
        self.crear_botones()

    def crear_boton(self, valor, fila, columna):
        button = tk.Button(self.ventana, text=str(valor))
        button.grid(row=fila, column=columna)

    def crear_botones(self):
        self.crear_boton(i, row, col)

if __name__ == "__main__":
    ventana = tk.Tk()
    calculator = Calculadora(ventana)
    ventana.mainloop()
