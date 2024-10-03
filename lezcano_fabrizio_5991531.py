print('TEMA 1')
N =  int(input("ingrese la cantidad de valores: "))
LISTA = []
VALORES = []
FRECUENCIA = []
CARGAR = 0 
#CARGAR VALORES EN LISTA
for K in range (N):
    print("ingrese el valor numero", K+1)
    CARGAR = int(input())
    LISTA.append(CARGAR)
for J in range (N):
    for I in range (N-J-1):
        if LISTA[I] > LISTA[I+1]:
            LISTA[I],LISTA[I+1] = LISTA[I+1],LISTA[I]
ULTIMO = LISTA[0]
ULTIMO_CONT = 1
#SELECCIONAR VALORES REPETIDOS
VALORES.append(ULTIMO)
for L in range (1,N,1):
    if ULTIMO != LISTA[L]:
        ULTIMO = LISTA[L]
        VALORES.append(ULTIMO)
        FRECUENCIA.append(ULTIMO_CONT)
        ULTIMO_CONT = 1
    else:
        ULTIMO_CONT = ULTIMO_CONT + 1
FRECUENCIA.append(ULTIMO_CONT)
print(LISTA)
print(VALORES)
print(FRECUENCIA)

# En for L in range (1,N-1,1): el rango deberia ser N, no N-1
    