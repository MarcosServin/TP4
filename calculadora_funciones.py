import tkinter as tk
from math import sqrt , cos , tan

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana#trae el programa creado de afuera
        self.ventana.geometry('500x250')#configura el tamaño incial
        self.ventana.title("Calculadora")#cambia el titulo de el programa
        self.ventana.columnconfigure(0, weight=1)#le da los valores necesarios a la fila 0 y columna 0
        self.ventana.rowconfigure(0, weight=1)

        self.ventana.columnconfigure(1, weight=1)#le da los valores necesarios a la fila 1  y columna 1
        self.ventana.rowconfigure(1, weight=1)

        #crea el frame en donde va a estar el widget de entrada de datos
        self.frame_entrada=tk.Frame(self.ventana,bg="black")#pega el frame a la ventana,con bg=,lo cambia a color negro
        self.frame_entrada.grid(row=0,column=0,sticky="nsew")
        self.frame_entrada.columnconfigure(0, weight=1)
        self.frame_entrada.rowconfigure(0, weight=1)

        self.entrada=tk.Entry(self.frame_entrada,justify='right',font=("arial",30),insertwidth="200",fg="white",bg="black")
        self.entrada.grid(row=0,column=0,sticky="nsew")

        self.frame_calc = tk.Frame(self.ventana,bg="black")
        self.frame_calc.grid(row=1, column=0, sticky="nsew")

        #configura cada fila y columna,el primer parametro es la fila o columna y el segundo parametro cambia la prioridad en caudricula
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

        #crea todo los botones
        self.crear_botones()
    
    def computo_final(self):
        calculo=self.entrada.get()#toma lo que se encuentre en widget self.entrada
        calculo=calculo.replace("x","*")#cambia todas las x por * ,para poder realizar la operacion matematica,x es una letra no funciona para nada
        calculo=calculo.replace("^","**")#cambia ^ por ** ,no pude encontrar la forma correcta de usar ^,asi que lo cambie en la funcion pero lo deje en boton
        calculo=calculo.replace("√","sqrt")#cambia √ por la FUNCION math.sqrt() para calcular la raiz cuadrada
        indi=len(calculo)
        try:
            self.entrada.delete(0,indi)
            calculo=eval(calculo)
            self.entrada.insert(0,calculo)
        except:
            self.entrada.delete(0,indi)
            self.entrada.insert(0,"ERROR")
    
    #Toma el valor en el boton y lo inserta en widget de entrada(Entry)
    def insertar_valor(self,valor):
        texto=self.entrada.get()#guarde el texto de el widget entrada en la var texto usando la funcion .get()
        index=len(texto)#Cuando se apreta un boton calcula la longitud de el texto en el widget entrada y para saber cual es el último índice
        #Si el boton es = llama a la funcion que realiza el caluclo "computo_final()"
        if valor=='=':
            self.computo_final()
        #Si el boton apretado es "←" borra el caracter indicado con el indice
        elif valor=='←':
            self.entrada.delete(index-1)
        #El boton "L" borra todo en el widget entrada,usando la funcion .delete(),la funcion utiliza un rango,aca uso el indice 0 y el ultimo
        elif valor=="L":
            self.entrada.delete(0,index)
        
        else:#cambia el valor de las funciones complejas por uno valido para la libreria "math",después lo inserta con .insert() en el ultimo indice y el valor
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
        #crea un widget boton,el primer parametro es el frame en donde va a estar(self.frame_calc)
        #lo demas son las config,"text="toma el valor,"font="el tamaño de el valor,"command=" llama la funcion que ocurre cuando se lo preciona
        #"fg=","bg=". son el foreground y el bacground,los usé para cambiar el color de los caracteres "fg" y el boton "bg"
        boton = tk.Button(self.frame_calc, text=str(valor),font=(10),command=lambda:self.insertar_valor(valor),fg="white",bg="black")
        #.grid() es la forma de ordenar los botones en la cuadricula de la pantalla como en un excel
        # la configuracion "sticky=" es para que los botones cambien de tamaño con la pantalla
        boton.grid(row=fila, column=columna,sticky='NSEW')

    def crear_botones(self):
        #primer parametros es el valor que se le da al boton,el segundo es la fila y el tercero la columna
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
