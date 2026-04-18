# 1
edad = 44

# 2
precio_pan = 1.50

# 3
ciudad = "Caracas"

# 4
estudiando = True

# 5
print(type(edad))
print(type(precio_pan))
print(type(ciudad))
print(type(estudiando))

# 6
a = 1
b = 4
c = a + b

# 7
d = b - a

# 8
e = 2.4
f = 5.1
g = e * f

# 9
h = a / b
print(type(h))

# 10
i = 2 ** 3
print(i)

# 11
user_name = input("Ingrese su nombre, por favor: ")
print(f"Hola {user_name}")

# 12
num1 = input("Ingrese un numero: ")
num2 = input("Ahora ingrese otro numero: ")
total = int(num1) + int(num2)
print(f"El total equivale a {total}")

# 13
nombre = "Gabriela"
apellido = "Montoya"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# 14
name = "Tomas"
city = "Carupano"
print(f"Hola, mi nombre es {name} y vivo en {city}")

# 15
base = float(input("Ingrese la medida de la base: "))
altura = float(input("Ahora indique la medida de la altura: "))
area = base * altura
print(f"El área es: {area}")

# 16
precio = float(input("Ingrese el precio del producto: "))
total_con_iva = precio * 1.16
print(f"Total con IVA: {total_con_iva}")

# 17
metros = int(input("Indique la cantidad de metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalen a {centimetros} centimetros")

# 18
ano_nacimiento = int(input("Año de nacimiento: "))
ano_actual = int(input("Año actual: "))
edad_calculada = ano_actual - ano_nacimiento
print(f"Tu edad es: {edad_calculada}")

# 19
frase = input("Ingrese una frase: ")
print(f"La frase tiene {len(frase)} caracteres")

# 20
oracion = input("Escriba una oración: ")
print(oracion * 10)

# 21 - Intento de sumar int + str (Lanzará TypeError)
cifra1 = 5
cifra2 = "5"
# suma_error = cifra1 + cifra2  

# 22 - Casting de float a int
decimales = 10.99
decimales_int = int(decimales)
print(f"El float {decimales} convertido a int es: {decimales_int}")

# 23
password = input("Ingrese una contraseña: ")
es_valida = len(password) > 8
print(f"¿Contraseña válida?: {es_valida}")

# 24 - Sistema de Cajero
saldo = float(input("Saldo actual: "))
retiro = float(input("Monto a retirar: "))
if retiro > saldo:
    print(f"Operación negada. El monto ${retiro} supera su saldo de ${saldo}")
else:
    print(f"Operación exitosa. Saldo restante: ${saldo - retiro}")

# 25 - Formato de Tarjeta
nom = input("Nombre y apellido: ")
borde = "*" * (len(nom) + 20)
print(borde)
print(f"*** Persona: {nom} ***")
print(borde)

# 26 - Conversión de tiempo
minutos_totales = int(input("Minutos a convertir: "))
horas = minutos_totales // 60
sobrante = minutos_totales % 60
print(f"{minutos_totales} min son {horas}h y {sobrante}min")

# 27 - Intercambio de variables
a = 2
b = 3
temporal = a
a = b
b = temporal
print(f"Intercambio: a={a}, b={b}")

# 28 - Promedio con jerarquía de operaciones
nota1 = 13
nota2 = 10
nota3 = 19
promedio = (nota1 + nota2 + nota3) / 3
print(f"Promedio redondeado: {round(promedio, 2)}")

# 29
info = input("Ingrese un dato: ")
print(f"¿Es un número?: {info.isdigit()}")

# 30 - RETO TITÁN
nombre_qa = input("Nombre del QA: ")
lenguaje = input("Lenguaje favorito: ")
exp = input("Años de experiencia: ")
sueldo = input("Sueldo deseado (USD): ")

perfil = (
    f"El QA Engineer {nombre_qa} domina {lenguaje} tras {exp} años "
    f"y aspira a un contrato de {sueldo} USD."
)
print(perfil)