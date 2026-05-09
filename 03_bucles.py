"""
<<<<<<< HEAD
Módulo 03: Fundamentos de Python - Mi camino a QA Automation
Autor: Richard Rosal
Objetivo: Dominio de Bucles y Lógica de Control
"""

# 01. Conteo simple (For)
for i in range(1, 11):
    print(f"Paso número: {i}")

# 02. Cuenta regresiva (While)
num = 10
while num >= 1:
    print(f"Lanzamiento en: {num}")
    num -= 1

# 03. Sumatoria de naturales
limite = 50
suma = 0
n = 1
while n <= limite:
    suma += n
    n += 1
print(f"La suma de los primeros {limite} números es: {suma}")

# 04. Filtrado de pares (Optimizado)
# Saltamos de 2 en 2 para no procesar números innecesarios
for num in range(2, 21, 2):
    print(f"{num} es par")

# 05. Tabla de multiplicar dinámica
tabla = 7 
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

# 06. Contador de letras específico
frase = "Tener paciencia es una virtud".lower()
letra_objetivo = "a"
# Usando count() para mayor eficiencia
contador = frase.count(letra_objetivo) 
print(f"La letra '{letra_objetivo}' aparece {contador} veces")

# 07. Suma de impares (1-100)
suma_impares = sum([i for i in range(1, 101) if i % 2 != 0])
print(f"Total impares: {suma_impares}")

# 08. Cuadrados perfectos
for i in range(1, 11):
    print(f"El cuadrado de {i} es {i**2}")

# 09. Simulación de Login Seguro
password_correcta = "admin123"
intento = ""
while intento != password_correcta:
    intento = input("Introduce la clave, Richard: ")
    if intento != password_correcta:
        print("Clave incorrecta. Inténtalo de nuevo.")
print("Acceso concedido.")

# 10. Múltiplos de 5
for i in range(5, 51, 5):
    print(f"{i} es múltiplo de 5")

# 11. Validador de Precios (QA Alerta)
precios = [256, 56, 189, 999, 17867, 17897987]
for p in precios:
    if p > 1000:
        print(f"ALERTA: El precio ${p} es demasiado alto.")

# 12. Contador de Vocales Total
usuario = "Isabela".lower()
total_vocales = 0
for char in usuario:
    if char in "aeiou":
        total_vocales += 1
print(f"El nombre {usuario} tiene {total_vocales} vocales.")

# 13. Inversión Manual de Texto
palabra = "Automation"
invertida = ""
for letra in palabra:
    invertida = letra + invertida
print(f"Original: {palabra} -> Invertida: {invertida}")

# 14. El Factorial
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"El factorial de {n} es {fact}")

# 15. Filtro de Dominios (Gmail)
correos = ["ma.corina@gmail.com", "luis.ugalde@hotmail.com", "pepe.perez@gmail.com"]
for c in correos:
    if c.endswith("@gmail.com"):
        print(f"Correo verificado: {c}")

# 16. Búsqueda con Break
objetivo = "Andrea"
nombres = ["Sara", "Ana", "Maria", "Luisa", "Andrea", "Ambar"]
for n in nombres:
    if n == objetivo:
        print(f"¡Encontré a {objetivo}!")
        break

# 17. El filtrado inteligente
for i in range(1, 12):
    if i == 5 or i == 8:
        continue
    print(f"ID de usuario {i} verificado con éxito")

# 18. El centinela (Uso de For-Else)
procesos = ["Update", "Backup", "Scan", "Clean"]
for i in procesos:
    if i == " ":
        print("¡Amenaza detectada! Abortando...")
        break
else:
    print("Análisis completo: No se encontraron amenazas en el sistema.")

# 19. El validador de datos de experiencia
while True:
    try:
        anos = int(input("Introduce tus años de experiencia: "))
        if anos < 0:
            print("Error: los años no pueden ser negativos")
            continue
        elif anos == 0:
            print("Parece que estás empezando. Saliendo del registro...")
            break
        else:
            print(f"Perfecto. {anos} años registrados con éxito")
            break
    except ValueError:
        print("Dato inválido. Por favor introduce un número.")

# 20. Testeando coordenadas (Bucle anidado)
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"Testeando botón en Fila {fila}, Columna {columna}")

# 21. Gestión de la suite de pruebas
lista_qa = ["Login", "Registro", "Carrito"]
lista_qa.append("Pago")
lista_qa.insert(0, "Bug_Critico")
for i in lista_qa:
    print(f"Módulo: {i}")

# 22. Ejecución y limpieza
tarea_en_proceso = lista_qa.pop(0)
print(f"Ejecutando ahora mismo: {tarea_en_proceso}")
if "Registro" in lista_qa:
    lista_qa.remove("Registro")
for i in lista_qa:
    print(f"Tareas pendientes: {i}")

# 23. El orden de los navegadores
browsers = ["Chrome", "Safari", "Edge", "Firefox", "Opera"]
browsers.sort() # El orden se mantiene después de aplicar el método
print(f"Ordenados: {browsers}")
browsers.reverse() 
print(f"Inversos: {browsers}")

# 24. Auditoría de resultados
resultados = ["Pass", "Fail", "Pass", "Error", "Fail", "Pass"]
fallos = resultados.count("Fail")
posicion_error = resultados.index("Error")
print(f"Total de fallos: {fallos}")
print(f"El error crítico está en la posición: {posicion_error}")

# 25. Segmentación de reportes (Slicing)
logs_semanales = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
laborales = logs_semanales[0:5]
fin_semana = logs_semanales[-2:]
print(f"Laborales: {laborales}, Fin de semana: {fin_semana}")

# 26. Configuración inmutable (Tuplas)
config_servidor = ("192.168.1.1", 8080, "HTTPS")
puerto = config_servidor[1]
print(f"Servidor: {config_servidor}, Puerto: {puerto}")

# 27. Desempaquetado del estudiante
estudiante = ("Adrian", "Inglés", "Intermedio")
nombre, materia, nivel = estudiante
print(f"El estudiante {nombre} estudia {materia} en nivel {nivel}")

# 28. El recolector de basura (Unpacking)
log_qa = ("2026-04-28", "FAILED", "Button_Click", "Chrome", "v124", "Win11")
fecha, resultado, *basura = log_qa
print(f"Log de fecha {fecha} con resultado {resultado}. Resto de datos: {basura}")

# 29. El diccionario del bug
reporte_bug = {
    "id": 101,
    "severidad": "Crítica",
    "estado": "Abierto"
}
print(f"Reporte: bug {reporte_bug['id']} con severidad {reporte_bug['severidad']}")

# 30. Actualización de datos
reporte_bug["estado"] = "En progreso"
reporte_bug["prioridad"] = "Alta"
print(f"Reporte actualizado: {reporte_bug}")

# 31 a 33. Filtros y contadores de resultados
resultados = ["Pass", "Fail", "Skipped", "Error", "Pass", "Skipped"]
correctos, fallos, saltados = [], [], []

for test in resultados:
    if test == "Skipped":
        saltados.append(test)
    elif test == "Pass":
        correctos.append(test)
    else:
        fallos.append(test)
print(f"Resultados: {len(correctos)} Pass, {len(fallos)} Fallos, {len(saltados)} Saltados")

# 34. Centinela de errores
logs = ["OK", "OK", "CORRUPT_DATA", "OK", "OK"]
for index, error in enumerate(logs, start=1):
    if error == "CORRUPT_DATA":
        print(f"Error catastrófico en iteración {index}. Deteniendo.")
        break
    print(f"Revisando iteración {index}...")

# 35 a 36. Gestión de Timeouts y Conexiones
intentos = 1
while intentos <= 5:
    print(f"Verificando conexión... Intento {intentos}")
    if intentos == 3:
        print("Conexión establecida. Deteniendo intentos.")
        break
    intentos += 1

# 37. Validación de entrada positiva
while True:
    numero = int(input("Introduzca el número maestro: "))
    if numero > 0:
        print("Dato aceptado")
        break
    print("Error: el valor debe ser positivo.")

# 38. Menú de operaciones
while True:
    print("\n--- Menú de Operaciones ---")
    print("1. Ejecutar Smoke Test")
    print("2. Ver reporte de errores")
    print("3. Salir")
    seleccion = input("Seleccione una opción, Richard: ")
    
    if seleccion == "1":
        print("Lanzando suite crítica... [Sistema OK]")
    elif seleccion == "2":
        print("Accediendo a logs de la base de datos...")
    elif seleccion == "3":
        print("Cerrando sesión. ¡Hasta la próxima!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

# 39. El filtro de datos (Uso de continue)
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue
    print(f"Transacción válida ID: {numero}")

# 40. Simulador de Retry Logic
intentos = 0
while intentos < 5:
    intentos += 1
    print(f"Intentando conexión... Intento {intentos}")
    if intentos == 3:
        print("¡Conexión exitosa!")
        break
else:
    print("Error crítico: El servidor no respondió después de 5 intentos.")
=======
Módulo 03: Fundamentos de Python - Bucles (Loops)
Propósito: Práctica de iteraciones controladas (for) y condicionales (while) para QA Automation.
Autor: Richard Rosal
Fecha: Abril 2026
"""

# 01. Imprimir números del 1 al 10 con `for`.
for i in range(1, 11):
    print(i)


# 02. Imprimir números del 10 al 1 con `while`.
num = 10

while num >= 1:
    print(num)
    num -= 1


# 03. Sumar los primeros 50 números naturales.
num = 1
sum = 0

while num <= 50:
    sum += num
    num += 1
print(sum)


# 04. Imprimir solo los números pares del 1 al 20.
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
    else:
        continue


# 05. Generar la tabla de multiplicar de un número dado.
tabla = int(input("Indique la tabla de multiplicar a generar: "))

for i in range(1, 11):
    print(f"{tabla} X {i} es igual a {tabla * i}")
>>>>>>> dbd03517bba10f999931eebcfbcc7e642929b0e3
