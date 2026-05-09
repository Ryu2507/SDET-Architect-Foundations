"""
================================================================================
PROYECTO: SDET Architect Foundations
MÓDULO: 04 - Estructuras de Datos
ESTUDIANTE: Richard Rosal
================================================================================
"""

# 01. Registro de bugs
bugs_encontrados = ["interfaz", "bdd", "api"]
bugs_encontrados.append("encendido")
print(bugs_encontrados)


# 02. Selector de URL
urls_de_prueba = [
    "https://www.amazon.com/shop", 
    "https://github.com/richard-qa", 
    "https://api.stripe.com/v1", 
    "https://www.binance.com/es-VE", 
    "https://playwright.dev/python"
]
print(urls_de_prueba[0])
print(urls_de_prueba[-1])


# 03. Ordenamiento de precios
precios = [10.5, 20.0, 5.75, 50.0]
precios.sort()
print(precios)


# 04. Limpieza de sesion
usuarios_activos = ["Richard", "Admin_Test", "Guest_01", "Dev_User"]
del usuarios_activos[1] # Elimino Admin_Test por posicion
print(usuarios_activos)


# 05. Validador de cantidad
checkboxes = [True, True, False, True, False]
print(len(checkboxes))


# 06. Slicing de datos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_slice = numeros[2:7]
print(mi_slice)


# 07. Buscador de botones
botones = ["Home", "Login", "Submit", "Logout"]
print(botones.index("Submit"))


# 08. Logger de errores
log_errores = []
log_errores.append("Error_A")
log_errores.append("Error_B")
log_errores.append("Error_C")
print(log_errores)


# 09. Fusion de servidores
srv_a = ["srv1", "srv2"]
srv_b = ["srv3", "srv4"]
red_completa = srv_a + srv_b
print(red_completa)


# 10. Reversa de pasos
pasos = ["Login", "Seleccionar Producto", "Pagar"]
pasos.reverse()
print(pasos)


# 11. Configuracion inmutable
coordenadas_click = (1050, 720)
# coordenadas_click[0] = 1080  <- Da error porque las tuplas no se pueden cambiar
print(coordenadas_click)


# 12. Desempaquetado de DB
db_config = ("127.0.0.1", "root", "secret123")
host, user, password = db_config
print(f"Host: {host}, Usuario: {user}, Pass: {password}")


# 13. Data provider
usuarios_test = [("admin", "123"), ("tester", "456"), ("guest", "789")]
print(usuarios_test[1])


# 14. Check de version
versiones = ("v120", "v121", "v122")
if "v124" in versiones:
    print("v124 encontrado")
else:
    print("v124 no esta en la lista")


# 15. Seguridad de entorno
paises = ["VE", "MX", "AR", "CO"]
paises_fijos = tuple(paises) # Lo paso a tupla para que no lo muevan
print(paises_fijos)


# 16. Mapeo de test case
test_case = {"id": 101, "titulo": "Compra Exitosa", "estado": "Pass"}
print(test_case)


# 17. Extraccion segura
print(test_case.get("estado"))


# 18. Inyeccion de metadatos (Prioridad)
error_info = {"code": 500, "msg": "Server Down"}
error_info["prioridad"] = "Alta"
print(error_info)


# 19. Update de URL
env_config = {"url": "https://staging.app.com", "retry": 3}
env_config["url"] = "https://app.com"
print(env_config)


# 20. Limpieza de PII (Password)
registro = {"nombre": "Richard", "email": "r@mail.com", "pass": "secret"}
registro.pop("pass")
print(registro)


# 21. API Schema Check
api_res = {"id": 1, "status": "ok", "data": [], "token": "abc"}
for clave, valor in api_res.items():
    print(f"Clave: {clave} | Valor: {valor}")


# 22. User Database
empleados = {
    101: {"nom": "Richard", "cargo": "QA"}, 
    102: {"nom": "Ana", "cargo": "Dev"}
}
# Acceso directo al nombre del 101
print(empleados[101]["nom"])


# 23. Token Validator
response = {"status": 200, "token": "xyz123"}
if "token" in response:
    print(f"Token hallado: {response['token']}")


# 24. Reporte dinamico
ajustes = {"v_size": "1080p", "headless": True, "speed": "fast"}
for clave, valor in ajustes.items():
    print(f"Ajuste: {clave}, Valor: {valor}")


# 25. Data Driven Starter
productos = [
    {"nom": "PC", "precio": 1200}, 
    {"nom": "Mouse", "precio": 25}, 
    {"nom": "Monitor", "precio": 300}
]

for p in productos:
    if p["precio"] >= 100:
        print(f"Producto: {p['nom']} - Precio: {p['precio']}")


# 26. Matrix Generator
tabla_datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in tabla_datos:
    if 5 in fila:
        print("Numero 5 encontrado en la matriz")


# 27. Unique Identifiers
ids = [101, 102, 101, 103, 102, 104, 105, 101]
lista_limpia = list(set(ids))
print(lista_limpia)


# 28. The Log Auditor
logs = ["ERROR", "SUCCESS", "ERROR", "ERROR", "SUCCESS", "TIMEOUT"]
contador = {}
for mensaje in logs:
    if mensaje in contador:
        contador[mensaje] += 1
    else:
        contador[mensaje] = 1
print(contador)


# 28.1. The Salary Auditor
pagos = [("VE", 50), ("MX", 100), ("VE", 20), ("AR", 80), ("MX", 30)]
dinero = {}

for pais, monto in pagos:
    if pais in dinero:
        dinero[pais] += monto
    else:
        dinero[pais] = monto
print(dinero)


# 28.2. Dict Comprehension (Cuadrados)
numeros = [1, 2, 3, 4, 5]
cuadrados = {}
for x in numeros:
    cuadrados[x] = x ** 2
print(cuadrados)


# 29. Transformacion JSON (Keys y Values)
settings = {"vol": 80, "mute": False, "lang": "ES"}
print(list(settings.values()))
print(list(settings.keys()))


# 30. El reto Titan (Filtrado de Admins)
db_users = [
    {"user": "richard", "rol": "Admin"},
    {"user": "pepe", "rol": "User"}, 
    {"user": "marta", "rol": "Admin"}
]
admins = {}

for user in db_users:
    if user["rol"] == "Admin":
        admins[user["user"]] = user["rol"]

print(admins)


