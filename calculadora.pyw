from tkinter import *
from tkinter import messagebox as MessageBox
import math

ventana = Tk()
ventana.title('Calculadora')
ventana.geometry('500x675')
ventana.resizable(0,0)
scroll_bar = Scrollbar(ventana)

canva = Canvas(ventana,bg = "#000" , yscrollcommand = scroll_bar.set)
scroll_bar.config(command=canva.yview,bg = "#009965")

scroll_bar.pack(side = RIGHT,fill = Y)

frame = Frame(canva)
frame.config(bg = "black")
canva.pack(fill = "both" , expand = True)

canva.create_window(0,0,window = frame , anchor = "nw")

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

def gplv2():
	MessageBox.showinfo("GNU GENERAL PUBLIC LICENSE Version 2" , "GNU GENERAL PUBLIC LICENSE\nVersion 2, June 1991\n\nCopyright (C) 1989, 1991 Free Software Foundation, Inc.,\n51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA\nEveryone is permitted to copy and distribute verbatim copies\nof this license document, but changing it is not allowed.\nPreamble\n\n\nThe licenses for most software are designed to take away your\nfreedom to share and change it.  By contrast, the GNU General Public\nLicense is intended to guarantee your freedom to share and change free\nsoftware--to make sure the software is free for all its users.  This\nGeneral Public License applies to most of the Free Software\nFoundation's software and to any other program whose authors commit to\nusing it.  (Some other Free Software Foundation software is covered by\nthe GNU Lesser General Public License instead.)  You can apply it to\nyour programs, too.")

def lgplv2():
	MessageBox.showinfo("GNU LESSER GENERAL PUBLIC LICENSE Version 2.1" , "GNU LESSER GENERAL PUBLIC LICENSE\nVersion 2.1, February 1999\nCopyright (C) 1991, 1999 Free Software Foundation, Inc.\n51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA\nEveryone is permitted to copy and distribute verbatim copies\nof this license document, but changing it is not allowed.\n[This is the first released version of the Lesser GPL.  It also counts\nas the successor of the GNU Library Public License, version 2, hence\nthe version number 2.1].")

#-----------Frontend-----------

menubar = Menu(ventana)
ventana.config(menu = menubar)
filemenu = Menu(menubar , tearoff = 0)
filemenu.config(bg = "#000906" , fg = "#fff" , font = "monospace 9",relief="sunken")
salir = filemenu.add_command(label = "Salir" , command = frame.quit)

file = menubar.add_cascade(label = "Archivo" , menu = filemenu)
menubar.config(bg = "#000906" , fg = "#fff" , font = "monospace 9")

acerca_de_menu = Menu(ventana)
acercade = menubar.add_command(label = "Acerca De" , command = acercade)
acerca_de_menu.config(font = "monospace 9")


ayuda_menu = Menu(ventana)
ayuda_de_menu = menubar.add_command(label = "Ayuda" , command = ayuda , font = "monospace 9")
ayuda_menu.config(font = "monospace 9")

licencia_de_menu = Menu(menubar , tearoff = 0)
licencia = Menu(ventana)
licencia_menu = menubar.add_cascade(label = "Licencia" , menu = licencia_de_menu)
gplv2 = licencia_de_menu.add_command(label = "Licencia GPLv2" , command = gplv2)
licencia_de_menu.config(bg = "#000906" , fg = "#fff" , font = "monospace 9")
lgplv2 = licencia_de_menu.add_command(label = "Licencia LGPLv2.1" , command = lgplv2)
licencia_de_menu.config(bg = "#000906" , fg = "#fff" , font = "monospace 9")


imagen = PhotoImage(file = "img/grafico3.png")
imagen.config(height = 115)
Label(frame , image = imagen).pack()


Label(frame , text = "\nCalculadora\n____________",bg = "#000" , fg = "#fff" , font = "monospace 13").pack()

Label(frame , text = "\nNúmero 1" , bg = "#000" , fg = "#00FFA7" , font = "monospace 11").pack()
Numero_1 = Entry(frame , text="" , textvariable = num_1 , bg = "#000906" , fg = "#fff" , justify = "center").pack()

Label(frame , text = "\nNúmero 2" , bg = "#000" , fg = "#00FFA7" , font = "monospace 11").pack()
Numero_2 = Entry(frame , text = "" , textvariable = num_2 , bg = "#000906" , fg = "#fff" , justify = "center").pack()

Label(frame , text = "\nResultado" , bg = "#000" , fg = "#00FFA7" , font = "monospace 11").pack()
Resultado = Entry(frame , text = "" , textvariable = resultado , bg = "#000906" , fg = "#00E99A" , cursor = "none" , justify = "center").pack()

Label(frame,text = "" , bg = "#000").pack()

#--------Botones------------
Button(frame , text = "Sumar" , command = sumar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 38).pack()
Button(frame , text = "Restar" , command = restar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 35).pack()
Button(frame , text = "Multiplicar" , command = multiplicar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 18).pack()
Button(frame , text = "Dividir" , command = dividir , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 32).pack()
Button(frame , text = "Potencia" , command = potencia , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 28).pack()
Button(frame , text = "Raíz Cuadrada" , command = raiz_cuadrada , bg = "#08412D" , fg = "#fff" , font = "monospace 9").pack()
Button(frame , text = "Comprobar nºfinito" , command = comprobar_num_finito , bg = "#08412D" , fg = "#fff" , font = "monospace 9").pack()
Button(frame , text = "Comprobar nºperiodico" , command = comprobar_num_periodico , bg = "#08412D" , fg = "#fff" , font = "monospace 9").pack()
Button(frame , text = "Borrar" , command = borrar , bg = "#08412D" , fg = "#fff" , font = "monospace 9" , padx = 35).pack()

Label(frame , text = "" , bg = "#000").pack()

Label(frame , text = "  Hecho por martinval9  " , bg = "#000906" , fg = "#00FFA7" , font = "Sans 12").pack()
Label(frame , text = "——————————————————————————————" , bg = "#000" , fg = "#00FFA7",font = "Sans 12").pack()
Label(frame , text = "GNU GENERAL PUBLIC LICENSE\nVersion 2, June 1991\nCopyright (C) 1989, 1991 Free Software Foundation, Inc.,\n51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA\nEveryone is permitted to copy and distribute verbatim copies\nof this license document, but changing it is not allowed." , bg = "#000" , fg = "#fff").pack()
ventana.update()
canva.config(scrollregion=canva.bbox("all"))
ventana.mainloop()
