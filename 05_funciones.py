"""
Módulo 02: Lógica de Condicionales y Funciones
Propósito: Ejercicios de validación, modularización, tipos de datos, control de flujo y lógica booleana.
Autor: Richard Rosal
Fecha: Mayo 2026
"""

# 1. El griton
def gritar_nombre(nombre: str):
    return nombre.upper()

# 2. El validador de vacio
def verificar_texto(texto: str):
    if texto == "":
        return "Esta vacio"
    return "Tiene contenido"

# 3. El multiplicador seguro
def duplicar_numero(numero: int):
    doble = numero * 2
    return doble

# 4. El multiplicador triple
def multiplicador_triple(numero: int):
    triple = numero * 3
    return triple

# 5. Concatenador de identidad
def concatenador_identidad(nombre: str, apellido: str):
    concatenacion = nombre + " " + apellido
    return concatenacion

# 6. Calculador de segundos
def calculador_segundos(minutos: int):
    calculador = minutos * 60
    return calculador

# 7. Area de rectangulo
def area_rectangulo(base: int, altura: int):
    area = base * altura
    return area

# 8. Detector de negativos
def detector_negativos(numero: int):
    if numero < 0:
        return "Negativo"
    return "Positivo"

# 9. Validador de password
def validar_password(clave: str):
    if len(clave) < 8:
        return False
    return True

# 10. Filtro de paridad
def filtro_paridad(numero: int):
    if numero % 2 == 0:
        return True
    return False

# 11. Simulador de envio
def simulador_envio(precio: int, costo_envio: int = 5):
    costo_total = precio + costo_envio
    return costo_total

# 12. Saludador de turno
def saludador_turno(nombre: str, saludo: str = "Buenos dias"):
    saludo_turno = saludo + ", " + nombre
    return saludo_turno

# 13. Repetidor dinamico
def repetidor_dinamico(texto: str, veces: int = 2):
    repeticion = texto * veces
    return repeticion

# 14. El inversor de strings
def inversor_textos(texto: str):
    inversor = texto[::-1]
    return inversor

# 15. El calculador de promedio simple
def calculador_promedio(num1: int, num2: int, num3: int):
    promedio = (num1 + num2 + num3) / 3
    return f"{promedio:.2f}"

# 16. Formateador de moneda
def formateador_moneda(cantidad: int):
    formateador = f"${cantidad}"
    return formateador

# 17. Contador de caracteres total
def contador_caracteres(lista_palabras: list):
    total = len(lista_palabras[0]) + len(lista_palabras[1])
    return total

# 18. Conversor de letras
def conversor_letras(texto: str, a_mayusculas: bool):
    if a_mayusculas:
        return texto.upper()
    return texto.lower()

# 19. Validador de rango de edad
def validar_edad(edad: int):
    if 18 <= edad <= 65:
        return True
    return False

# 20. Calculador de descuento
def calcular_descuento(precio: float, porcentaje_descuento: int = 5):
    porcentaje = precio * porcentaje_descuento / 100
    total = precio - porcentaje
    return total

# 21. Generador de ID
def generador(nombre: str, ano_nacimiento: int):
    return f"{nombre}{ano_nacimiento}"

# 22. Verificador de sufijos
def verificador(archivo: str, sufijo: str):
    if archivo.endswith(sufijo):
        return True
    return False

# 23. Repetidor con separador
def repetidor_separador(texto: str, separador: str = "-"):
    return f"{texto + separador + texto}"

# 24. El validador de email simple
def validador_email(email: str):
    if "@" in email:
        return True
    return False

# 25. Calculador de IVA dinamico
def calculadora_iva(precio: float): 
    calculo = precio * 16 / 100
    return calculo

# 26. El griton elegante
def griton_elegante(texto: str):
    griton = f"{texto + '!!!'}"
    return griton

# 27. Buscador de palabra
def buscador_palabras(frase: str, palabra: str):
    if palabra.lower() in frase.lower():
        return True
    return False

# 28. Formateador de ruta
def formatear_ruta(carpeta: str, ruta: str):
    return f"{carpeta + '/' + ruta}"

# 29. Calculador de potencia
def calculo_potencia(base: int, exponente: int = 2):
    calculo = base ** exponente
    return calculo

# 30. Censor de palabras
def censor_palabras(texto: str):
    if texto.lower() == "maldicion":
        return "****"
    return texto

# 31. Verificador de lista vacia
def verificador_vacios(lista: list):
    if len(lista) == 0:
        return True
    return False

# 32. Unificador de nombres
def unificador_nombres(nombre: str, apellido: str, titulo: str = ""):
    if titulo == "":
        return f"{nombre + ' ' + apellido}"
    return f"{titulo + ' ' + nombre + ' ' + apellido}"

# 33. Composicion de funciones
def suma(num1: int, num2: int):
    return num1 + num2

resultado_final = suma(suma(1, 2), suma(3, 4))

# --- Seccion extra: isinstance() ---

def griton_seguro(texto: str):
    if isinstance(texto, str):
        return texto.upper()
    return "Entrada invalida"

def suma_protegida(num1: int, num2: int):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    return "Solo sumo numeros"

def filtro_usuario(nombre: str):
    if not isinstance(nombre, str):
        return "Nombre debe ser texto"
    if nombre == "":
        return "Nombre vacio"
    return "Bienvenido"