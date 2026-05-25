# SE CREAR EL ARCHIVO, LISTO PARA SER USADO EN EL PROYECTO
#CONSIGNA 1: PARTE B
#DECLARAMOS VARIABLES   
A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]

# USAMOS FUNCION PARA CLASIFICAR USUARIOS CRITICOS Y NO CRITICOS
def clasificar_usuario(A,B,C):
    usuarios_al_menos_una_plataforma = []
    for usuario in A:
        usuarios_al_menos_una_plataforma.append(usuario)
    for usuario in B:
        if usuario not in usuarios_al_menos_una_plataforma:
            usuarios_al_menos_una_plataforma.append(usuario)

    for u in usuarios_al_menos_una_plataforma:
        p = u in A
        q = u in B
        r = u in C

        if (p or q) and r:
            print(u, "-> Crítico")
        else:
            print(u, "-> No crítico")
# LLAMAMOS FUNCION
print("#CONSIGNA 1: PARTE B")
print("CLASIFICACIÓN DE USUARIOS:")
clasificar_usuario(A,B,C)
#CONSIGNA 2: PARTE B
print("#CONSIGNA 2: PARTE B")
#Creamos las funciones matemáticas:
def A(x):
    return 40 * x + 200

def B(x):
    return 70 * x + 50

def C(x):
    return -2 * x**2 + 80 * x + 100

#Evaluamos funciones
print("Evaluación de funciones para diferentes valores de x:")

x = [0, 5, 10, 15, 20, 25, 30, 40, 50]
for val in x:
    print(f"x={val}: A(x)={A(val)}, B(x)={B(val)}, C(x)={C(val)}")      

#8. Crear una función en python que determine el plan más económico para un valor de x
print("Plan más económico:")
def plan_mas_economico(x):
    costo_A = A(x)
    costo_B = B(x)
    costo_C = C(x)
    plan_economico = "A"
    costo_minimo = costo_A
    if costo_B < costo_minimo:
        plan_economico = "B"
        costo_minimo = costo_B
    if costo_C < costo_minimo:
        plan_economico = "C"
        costo_minimo = costo_C
    return plan_economico, costo_minimo
for val in x:
    plan, costo = plan_mas_economico(val)
    print(f"x={val}: Plan más económico: {plan} con costo {costo}")

# CONSIGNA 3: PARTE B
print("#CONSIGNA 3: PARTE B")
M = [
    [120, 150, 100],   # Función 1
    [200, 180, 220],   # Función 2
    [90, 110, 95]      # Función 3
]

#Calcular promedio por función (filas)
print("Promedio por función:")
for i in range(len(M)):  
    suma = 0
    contador = 0
    for j in range(len(M[i])):  
        suma = suma + M[i][j]
        contador = contador + 1
    promedio = suma / contador
    print("Función", i+1, "-> Promedio:", promedio, "ms")

#Calcular promedio por servidor (columnas)
print("Promedio por servidor:")
for j in range(len(M[0])):  
    suma = 0
    contador = 0
    for i in range(len(M)):  
        suma = suma + M[i][j]
        contador = contador + 1
    promedio = suma / contador
    print("Servidor", j+1, "-> Promedio:", promedio, "ms")

#4. Calcular la matriz transpuesta de M y explicar qué representa en este contexto.
M_transpuesta = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
print("Matriz transpuesta de M:")
for fila in M_transpuesta:
    print(fila)