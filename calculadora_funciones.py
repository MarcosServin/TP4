import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('500x250')
        self.ventana.title("Calculadora")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.frame_entrada=tk.Frame(self.ventana,bg="#ffffff")
        self.frame_entrada.grid(row=0,column=0,sticky="nsew")
        self.frame_entrada.columnconfigure(0, weight=1)
        self.frame_entrada.rowconfigure(0, weight=1)

        self.entrada=tk.Entry(self.frame_entrada,justify='right',font=("arial",50),fg="white",bg="black")
        self.entrada.grid(row=0,column=0,sticky="nsew")

        self.frame_calc = tk.Frame(self.ventana)
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

        self.crear_botones()
    
    def computo_final(self):
        calculo=self.entrada.get()
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
        elif valor=="Limpiar":
            self.entrada.delete(0,index)
        else:
            self.entrada.insert(index,valor)

    def crear_boton(self, valor, fila, columna):
        button = tk.Button(self.frame_calc, text=str(valor),command=lambda:self.insertar_valor(valor),fg="white",bg="black")
        button.grid(row=fila, column=columna,sticky='NSEW')

    def crear_botones(self):
        self.crear_boton("*", 0, 0)
        self.crear_boton("/", 0, 1)
        self.crear_boton("=", 0, 2)
        self.crear_boton("←", 0, 3)
        self.crear_boton("Limpiar", 0, 4)
        self.crear_boton("7", 1, 0)
        self.crear_boton("8", 1, 1)
        self.crear_boton("9", 1, 2)
        self.crear_boton("+", 1, 3)
        self.crear_boton("(", 1, 4)
        self.crear_boton("4", 2, 0)
        self.crear_boton("5", 2, 1)
        self.crear_boton("6", 2, 2)
        self.crear_boton("-", 2, 3)
        self.crear_boton(")", 2, 4)
        self.crear_boton("1", 3, 0)
        self.crear_boton("2", 3, 1)
        self.crear_boton("3", 3, 2)
        self.crear_boton("0", 3, 3)
        self.crear_boton(".", 3, 4)

if __name__ == "__main__":
    ventana = tk.Tk()
    calculator = Calculadora(ventana)
    ventana.mainloop()
