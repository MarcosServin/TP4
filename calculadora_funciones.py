import tkinter as tk
from math import sqrt , cos , tan

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('500x250')
        self.ventana.title("Calculadora")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.frame_entrada=tk.Frame(self.ventana,bg="black")
        self.frame_entrada.grid(row=0,column=0,sticky="nsew")
        self.frame_entrada.columnconfigure(0, weight=1)
        self.frame_entrada.rowconfigure(0, weight=1)

        self.entrada=tk.Entry(self.frame_entrada,justify='right',font=("arial",30),insertwidth="200",fg="white",bg="black")
        self.entrada.grid(row=0,column=0,sticky="nsew")

        self.frame_calc = tk.Frame(self.ventana,bg="black")
        self.frame_calc.grid(row=1, column=0, sticky="nsew")
        self.frame_calc.columnconfigure(0, weight=1)
        self.frame_calc.rowconfigure(0, weight=1)
        self.frame_calc.columnconfigure(1, weight=1)
        self.frame_calc.rowconfigure(1, weight=1)
        self.frame_calc.columnconfigure(2, weight=1)
        self.frame_calc.rowconfigure(2, weight=1)
        self.frame_calc.columnconfigure(3, weight=1)
        self.frame_calc.rowconfigure(3, weight=1)
        self.frame_calc.columnconfigure(4, weight=1)
        self.frame_calc.rowconfigure(4, weight=1)
        self.frame_calc.columnconfigure(5, weight=1)

        self.crear_botones()
    
    def computo_final(self):
        calculo=self.entrada.get()
        calculo=calculo.replace("x","*")
        calculo=calculo.replace("^","**")
        calculo=calculo.replace("√","sqrt")
        indi=len(calculo)
        try:
            self.entrada.delete(0,indi)
            calculo=eval(calculo)
            self.entrada.insert(0,calculo)
        except:
            self.entrada.delete(0,indi)
            self.entrada.insert(0,"ERROR")
    
    def insertar_valor(self,valor):
        texto=self.entrada.get()
        index=len(texto)
        if valor=='=':
            self.computo_final()
        elif valor=='←':
            self.entrada.delete(index-1)
        elif valor=="L":
            self.entrada.delete(0,index)
        else:
            if valor=='√':
                valor='√('
            if valor=="sin":
                valor="sin("
            if valor=="cos":
                valor="cos("
            if valor=="tan":
                valor="tan("
            self.entrada.insert(index,valor)

    def crear_boton(self, valor, fila, columna):
        button = tk.Button(self.frame_calc, text=str(valor),font=(10),command=lambda:self.insertar_valor(valor),fg="white",bg="black")
        button.grid(row=fila, column=columna,sticky='NSEW')

    def crear_botones(self):
        self.crear_boton("cos", 0, 0)
        self.crear_boton("sin", 1, 0)
        self.crear_boton("tan", 2, 0)
        self.crear_boton("^", 3, 0)
        self.crear_boton("√", 4, 0)
        self.crear_boton("L", 0, 1)
        self.crear_boton("7", 1, 1)
        self.crear_boton("4", 2, 1)
        self.crear_boton("1", 3, 1)
        self.crear_boton("(", 0, 2)
        self.crear_boton("8", 1, 2)
        self.crear_boton("5", 2, 2)
        self.crear_boton("2", 3, 2)
        self.crear_boton("0", 4, 2)
        self.crear_boton(")", 0, 3)
        self.crear_boton("9", 1, 3)
        self.crear_boton("6", 2, 3)
        self.crear_boton("3", 3, 3)
        self.crear_boton(".", 4, 3)
        self.crear_boton("x", 0, 4)
        self.crear_boton("/", 1, 4)
        self.crear_boton("-", 2, 4)
        self.crear_boton("+", 3, 4)
        self.crear_boton("←", 4, 4)
        self.crear_boton("=", 0, 5)

if __name__ == "__main__":
    ventana = tk.Tk()
    calculator = Calculadora(ventana)
    ventana.mainloop()
