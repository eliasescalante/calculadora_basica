from tkinter import *
from tkinter import messagebox

################## VARIABLES GLOBALES ####################
numero1 = ""
operador = ""

################## FUNCIONES ####################

def calcular():
    global numero1
    global operador
    
    numero2 = entry.get()
    if numero2:
        if operador == "+":
            resultado = int(numero1) + int(numero2)
            messagebox.showinfo("Resultado", f"El resultado de la suma es: {resultado}")
        elif operador == "-":
            resultado = int(numero1) - int(numero2)
            messagebox.showinfo("Resultado", f"El resultado de la resta es: {resultado}")
        elif operador == "X":
            resultado = int(numero1) * int(numero2)
            messagebox.showinfo("Resultado", f"El resultado de la multiplicacion es: {resultado}")
        elif operador == "/":
            if numero2 != "0":
                resultado = int(numero1) / int(numero2)
                messagebox.showinfo("Resultado", f"El resultado de la division es: {resultado}")
            else:
                messagebox.showerror("Error", "No se puede dividir entre cero")
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Ingrese un número para realizar la operación")

def insertar_numero(numero):
    global numero1
    global operador
    if operador == "+" or operador == "-" or operador == "X" or operador == "/":
        entry.delete(0, END)
    entry.insert(END, numero)

def operacion(op):
    global numero1
    global operador
    numero1 = entry.get()
    if numero1:
        operador = op
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Ingrese un número antes de seleccionar una operación")

################## MAQUETACION ##################

#Inicio de la app
calculadora = Tk()

# Seteo el titulo de la app y su tamaño
calculadora.title("Mi primera calculadora")
calculadora.geometry("400x300")

# Inserto los widget
#inserto los botones de la calculadora utilizando place

# Entrada para insertar los numeros para calcular
entry = Entry(calculadora) #crear un entry para que el usuario pueda ingresar numeros
entry.place(x=125, y=40, height=40, width=160) 

# botones con los numeros
boton_1=Button(calculadora,text="1",width=5, command=lambda: insertar_numero("1"))
boton_1.place(x=80,y=100)

boton_2=Button(calculadora,text="2",width=5, command=lambda: insertar_numero("2"))
boton_2.place(x=140,y=100)

boton_3=Button(calculadora,text="3",width=5, command=lambda: insertar_numero("3"))
boton_3.place(x=200,y=100)

boton_4=Button(calculadora,text="4",width=5, command=lambda: insertar_numero("4"))
boton_4.place(x=80,y=140)

boton_5=Button(calculadora,text="5",width=5, command=lambda: insertar_numero("5"))
boton_5.place(x=140,y=140)

boton_6=Button(calculadora,text="6",width=5, command=lambda: insertar_numero("6"))
boton_6.place(x=200,y=140)

boton_7=Button(calculadora,text="7",width=5, command=lambda: insertar_numero("7"))
boton_7.place(x=80,y=180)

boton_8=Button(calculadora,text="8",width=5, command=lambda: insertar_numero("8"))
boton_8.place(x=140,y=180)

boton_9=Button(calculadora,text="9",width=5, command=lambda: insertar_numero("9"))
boton_9.place(x=200,y=180)

boton_0=Button(calculadora,text="0",width=5, command=lambda: insertar_numero("0"))
boton_0.place(x=80,y=220)

# Botones con  las operaciones
boton_mas=Button(calculadora, text="+", command=lambda: operacion("+"), width=5)
boton_mas.place(x=260, y=100)

boton_menos=Button(calculadora, text="-",command=lambda:operacion("-") , width=5)
boton_menos.place(x=260, y=140)

boton_x=Button(calculadora,text="*", command=lambda:operacion("X") , width=5)
boton_x.place(x=260, y=180)

boton_div=Button(calculadora,text="/",command=lambda:operacion("/") , width=5)
boton_div.place(x=260, y=220)

boton_igual=Button(calculadora,text="=",command=calcular, width=10)
boton_igual.place(x=140, y=220)

calculadora.mainloop()
