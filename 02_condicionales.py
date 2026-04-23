"""# 1
preguntar_edad = int(input("Por favor, indique su edad: "))

if preguntar_edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")


# 2
validar_par = int(input("Introduzca un numero para validar si es par: "))

if validar_par % 2 == 0:
    print("Este es un numero par")
else:
    print("Este numero es impar")


# 3
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ahora escriba el segundo numero: "))

if num1 > num2:
    print("El primer numero es mayor al segundo")
elif num1 < num2:
    print("El segundo numero es mayor que el primero")
else:
    print("Los dos numeros son iguales")


# 4
valor = int(input("Ingrese un numero a verificar: "))

if valor == 0:
    print("El numero es cero")
elif valor < 0:
    print("El numero es negativo")
else:
    print("El numero es positivo")


# 5
nota = int(input("Ingrese una calificacion, por favor: "))

if nota >= 10:
    print("Usted esta aprobado")
else:
    print("Usted esta reprobado")


# 6
cifra = int(input("Ingrese un numero, por favor: "))

if cifra % 5 == 0:
    print("El numero es divisible por 5")
else:
    print("El numero no es divisible por 5")


# 7
user = input("Ingrese su nombre de usuaro, por favor: ").lower()

if user == "admin":
    print("Hola, Jefe")
else:
    print("Hola, Usuario")


# 8
monto_compra = float(input("Indique el monto de la compra, por favor: "))

if monto_compra > 100:
    print(
        f"La compra recibe un descuento de 10%.Total a pagar: {monto_compra - (monto_compra * 0.10)}"
        )


# 9
num_rango = int(input("Ingrese un numero entre 1 y 100: "))

if num_rango >= 1 and num_rango <= 100:
    print(f"El numero {num_rango} se encuentra entre 1 y 100")
else:
    print("El numero se encuentra fuera del rango solicitado")


# 10    Aqui si me jodiste, lo admito. esto no recuerdo haberlo hecho
tener_hambre = input("Indique con T(true) o F(false) si tiene hambre: ").lower()

if not tener_hambre:
    print("No hay hambre. O sea, False, el inverso a True")
else:
    print(
    "Aqui si hay hambre ya que estamos con el opuesto a False," \
    "\n o sea, True"
    )


# 11
user_age = int(input("Ingrese la edad, por favor: "))

if user_age < 13:
    print("Niño")
elif user_age >= 13 and user_age <= 17:
    print("Adolescente")
else:
    print("Adulto")


# 12
num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba ahora el segundo numero: "))
operacion = input("Ingrese ahora el simbolo de la operacion a realizar: ")

if operacion == "+":
    print(f"La operacion suma de {num1} y {num2} equivale a {num1 + num2}")
elif operacion == "-":
    print(f"La operacion resta de {num1} y {num2} equivale a {num1 - num2}")
elif operacion == "x":
    print(f"La operacion multiplicacion de {num1} y {num2} equivale a {num1 * num2}")
else:
    print(f"La operacion division de {num1} y {num2} equivale a {num1 / num2}")


# 13
semaforo = input("Introduzca el color del semaforo que prefiera: ").lower()

if semaforo == "rojo":
    print("Detengase")
elif semaforo == "amarillo":
    print("Precaucion")
elif semaforo == "verde":
    print("Avance")
else:
    print("Revise el color ingresado")


# 14
dia_semana = int(input("Ingrese el numero que corresponda al dia de la semana: "))

#  Se que hay una forma mas sencilla de hacer esto, pero esta es la que recuerdo

if dia_semana == 1:
    print("Lunes")
elif dia_semana == 2:
    print("Martes")
elif dia_semana == 3:
    print("Miercoles")
elif dia_semana == 4:
    print("Jueves")
elif dia_semana == 5:
    print("Viernes")
elif dia_semana == 6:
    print("Sabado")
elif dia_semana == 7:
    print("Domingo")
else:
    print("Error en el numero del dia ingresado")


# 15
nota = int(input("Ingrese la calificacion de la evaluacion: "))

if nota >= 18 and nota <= 20:  # Si, hay una forma mas pythonic de hacerlo pero no lo recuerdo
    print("A")
elif nota >= 15 and nota <= 17:
    print("B")
elif nota >= 14 and nota <= 16:
    print("C")
elif nota >= 11 and nota <= 14:
    print("D")
elif nota <= 10: # Si, ya se, deberia ser else, pero me gusta delimitar mejor con elif
    print("F")


# 16
info = input("Introduzca la informacion que usted quiera: ")

if info == "":
    print("Error: Campo requerido")
else:
    print("Informacion correctamente almacenada")


# 17
mes = input("Introduce el nombre del mes del año: ").lower()

if mes == "enero" or mes == "febrero" or mes == "diciembre": # Ya se que no es pythonic
    print("Invierno")
elif mes == "marzo" or mes == "abril" or mes == "mayo":
    print("Primavera")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print("Verano")
else:
    print("Otoño")


# 18
word1 = input("Escriba la primera palabra: ")
word2 = input("Ahora escriba la segunda palabra: ")

if word1 == word2:
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")


# 19
vehiculo = input("Ingrese el tipo de vehiculo a registrar: ").lower()

if vehiculo == "moto":
    print("Tipo de vehiculo: Moto. Total a pagar: $1")
elif vehiculo == "carro":
    print("Tipo de vehiculo: Carro. Total a pagar: $2")
else:
    print("Tipo de vehiculo: Camion. Total a pagar: $5")


# 20
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Introduce ahora el segundo: "))
numero3 = int(input("Ahora escribe el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero {numero1} es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es el mayor")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero {numero3} es el mayor")


# 21
codigo = input("Ingrese el codigo observado: ").lower()

if codigo == 200:
    print("Exito")
elif codigo == 404:
    print("No encontrado")
elif codigo == 500:
    print("Error en el servidor")
else:
    print("Codigo desconocido")


# 22
password = input("Ingrese su contraseña: ")

if len(password) < 8:
    print(f"El password {password} es muy debil")
else:
    print(f"El password {password} es fuerte")


# 23
bisiesto = int(input("Ingrese el año a verificar si es bisiesto o no: "))

if (bisiesto % 4 == 0 and bisiesto % 100 != 0) or (bisiesto % 400 == 0):
    print(f"El año {bisiesto} es bisiesto")
else:
    print(f"El año {bisiesto} NO es bisiesto")


# 24
email = input("Ingrese un email con formato correcto: ").lower()

if "@" in email:
    print(f"El email {email} tiene formato correcto")
else:
    print(f"El email {email} carece de @ y, por eso, no tiene formato correcto")


# 25
username = "admin"
contrasena = 12345

user = input("Ingrese su usuario, por favor: ").lower()
contra = int(input("Ahora ingrese su contraseña: "))

if user == username and contra == contrasena:
    print("Datos correctos. Acceso permitido")
else:
    print("Usuario o Contraseña incorrecta. Acceso no permitido")


# 26
saldo = 20000

retiro = float(input("Ingrese el monto a retirar, por favor: $ "))

if retiro <= saldo:
    print(f"El monto ${retiro} es menor al saldo ${saldo}. Retiro aprobado")
else:
    print("El monto de retiro excede el saldo disponible. Retiro no permitido")


# 27
lado1 = int(input("Ingrese la medida del primer lado: "))
lado2 = int(input("Ahora el segundo lado: "))
lado3 = int(input("Finalmente, ingrese la medida del tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Este es un triangulo equilatero")
elif lado1 == lado2 and lado2 > lado3:
    print("Este es un triangulo isosceles")
elif lado1 > lado2 and lado2 > lado3:
    print("Y este es un triangulo escaleno, señoras y señores")


# 28
altura = float(input("Ingrese su altura (m): "))
peso = float(input("Ahora ingrese su peso (kg), por favor: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidad tipo 1")
elif imc >= 35 and imc <= 39.9:
    print("Obesidad tipo 2")
elif imc >= 40:
    print("Obesidad tipo 3")
else:
    print("Error en datos introducidos")
"""

# 29
word = input("Ingrese una palabra a verificar si es o no palindroma: ").lower()
reverse = word[::-1]

if word == reverse:
    print(f"La palabra {word} es palindroma")
else:
    print(f"La palabra {word} no es palindroma")


