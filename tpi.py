# SE CREAR EL ARCHIVO, LISTO PARA SER USADO EN EL PROYECTO
"""Se dispone de los siguientes datos:
A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
donde:
• A: usuarios que acceden a través de la API
• B: usuarios que acceden a través de la web
• C: usuarios que han generado errores
Definir:
• 𝑝: pertenece a A
• 𝑞: pertenece a B
• 𝑟: pertenece a C
Se define usuario crítico:
(𝑝 ∨𝑞)∧𝑟
6. Implementar una función en Python que evalúe la expresión.   

A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
P = [101, 102, 103, 104, 105, 106]
Q = [104, 105, 106, 107, 108]
R = [102, 105, 109] 
"""
#DECLARAMOS VARIABLES   
A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]

# USAMOS FUINCION PARA CLASIFICAR USUARIOS CRITICOS Y NO CRITICOS
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
clasificar_usuario(A,B,C)


