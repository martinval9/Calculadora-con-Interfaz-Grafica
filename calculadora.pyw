from tkinter import *
from tkinter import messagebox as MessageBox
import math
import os

root = Tk()

root.title("Calculadora")
root.config(bd = 2 , bg = "#000" , relief = "sunken")
root.resizable(1,5)

#---------StringVars--------

num_1 = StringVar()
num_2 = StringVar()
resultado = StringVar()

#-----------Backend-----------

#------Funciones de los botones-------

def sumar():
	try:
		resultado.set(float(num_1.get()) + float(num_2.get()))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : Martin8")

def restar():
	try:
		resultado.set(float(num_1.get()) - float(num_2.get()))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : Martin8")


def multiplicar():
	try:
		resultado.set(float(num_1.get()) * float(num_2.get()))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : Martin8")

def dividir():
	try:
		resultado.set(float(num_1.get()) / float(num_2.get()))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : Martin8")

def potencia():
	try:
		resultado.set(float(num_1.get()) ** float(num_2.get()))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : martinval9")

def raiz_cuadrada():
	try:
		valor = math.sqrt(int(num_1.get()))
		resultado.set(valor)

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : martinval9")

def comprobar_num_finito():
	try:
		valor = math.isfinite(float(num_1.get()))
		resultado.set(str(valor))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : martinval9")

def comprobar_num_periodico():
	try:
		valor = math.isinf(float(num_1.get()))
		resultado.set(str(valor))

	except ValueError:
		MessageBox.showerror("ValueError :(","Error de Calculo\n_________________________\n\nPosibles Causantes = \n\n* El cuadro numerico esta vacio.\n\n* Simbolos y Caracteres especiales en el cuadro numerico.\n\n* Si usted esta escribiendo numeros decimales asegure de que esta escribiendolos con un punto (.) y no una coma (,).\n\nEjemplo = \n\n1.35 - Bien.\n\n1,35 - Mal.\n\n* Si usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.\n\nSi el problema persiste,por favor reportalo en GitHub : martinval9.")

	except OverflowError:
		MessageBox.showerror("OverflowError :(","Resultado Numerico fuera del rango.")

	except:
		MessageBox.showerror("Error Desconocido :(","Error Desconocido,por favor reportalo en GitHub : martinval9")

def borrar():
	num_1.set("")
	num_2.set("")
	resultado.set("")

#-----Funciones de la barra de navegacion-------

def acercade():
	MessageBox.showinfo("Acerca De" , "CALCULADORA\n_____________________\n\nHecho por martinval9\nFecha: 29 de agosto de 2021\nMeta: Ser desarrollador de software.")

def ayuda():
	MessageBox.showinfo("Ayuda" , "En el cuadro Número 1 colocas el primer valor (por ejemplo 5).\n\nEn el cuadro Número 2 colocas el segundo valor (por ejemplo 10).\n\nLuego en los botones de la parte inferior puedes elegir si quieres que se sumen,resten o multipliquen los 2 valores que introduciste.\n\nSi presionaste cualquiera de los botones (excepto el boton de borrar) podras ver que en la parte del resultado aparecio el valor total.\n\nSi usted esta tratando de hacer una raiz cuadrada,o comprobar un numero finito/periodico entonces solo debe completar el cuadro número 1.")

#-----------Frontend-----------

menubar = Menu(root)
root.config(menu = menubar)
filemenu = Menu(menubar , tearoff = 0)
filemenu.config(bg = "#000906" , fg = "#fff" , font = "monospace 9",relief="sunken")
salir = filemenu.add_command(label = "Salir" , command = root.quit)

file = menubar.add_cascade(label = "Archivo" , menu = filemenu)
menubar.config(bg = "#000906" , fg = "#fff" , font = "monospace 9")

acerca_de_menu = Menu(root)
acercade = menubar.add_command(label = "Acerca De" , command = acercade)
acerca_de_menu.config(font = "monospace 9")


ayuda_menu = Menu(root)
ayuda_de_menu = menubar.add_command(label = "Ayuda" , command = ayuda , font = "monospace 9")
ayuda_menu.config(font = "monospace 9")


imagen = PhotoImage(file = "grafico3.png")
imagen.config(height = 115)
Label(root , image = imagen).pack()


Label(text = "\nCalculadora\n____________",bg = "#000" , fg = "#fff" , font = "monospace 13").pack()

Label(text = "\nNúmero 1" , bg = "#000" , fg = "#00FFA7" , font = "monospace 11").pack()
Numero_1 = Entry(text="" , textvariable = num_1 , bg = "#000906" , fg = "#fff" , justify = "center").pack()

Label(text = "\nNúmero 2" , bg = "#000" , fg = "#00FFA7" , font = "monospace 11").pack()
Numero_2 = Entry(text = "" , textvariable = num_2 , bg = "#000906" , fg = "#fff" , justify = "center").pack()

Label(text = "\nResultado" , bg = "#000" , fg = "#00FFA7" , font = "monospace 11").pack()
Resultado = Entry(text = "" , textvariable = resultado , bg = "#000906" , fg = "#00E99A" , cursor = "none" , justify = "center").pack()

Label(text = "" , bg = "#000").pack()

#--------Botones------------
Button(text = "Sumar" , command = sumar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 38).pack()
Button(text = "Restar" , command = restar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 35).pack()
Button(text = "Multiplicar" , command = multiplicar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 18).pack()
Button(text = "Dividir" , command = dividir , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 32).pack()
Button(text = "Potencia" , command = potencia , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 28).pack()
Button(text = "Raíz Cuadrada" , command = raiz_cuadrada , bg = "#08412D" , fg = "#fff" , font = "monospace 9").pack()
Button(text = "Comprobar nºfinito" , command = comprobar_num_finito , bg = "#08412D" , fg = "#fff" , font = "monospace 9").pack()
Button(text = "Comprobar nºperiodico" , command = comprobar_num_periodico , bg = "#08412D" , fg = "#fff" , font = "monospace 9").pack()
Button(text = "Borrar" , command = borrar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 35).pack()


Label(root , text = "" , bg = "#030303").pack()

Label(root , text = "  Hecho por martinval9  " , bg = "#000906" , fg = "#00FFA7" , font = "Sans 12").pack()
Label(root , text = "——————————————————————————————" , bg = "#000" , fg = "#00FFA7",font = "Sans 12").pack()
root.mainloop()
