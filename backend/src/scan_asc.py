

def scan_asc(init, queries, tracks = -1, debug = False):
    ans = 0
    
    n = len(queries)
    queries.sort()  # Ordenar las consultas
    if (tracks == -1):
        tracks = queries[-1]
    else:
        queries.append(tracks)
    checked = [False] * len(queries)  # Inicializar un arreglo de booleanos
    
    
    # Encontrar el índice inicial
    i = 0
    started = False
    while i < len(queries) and not started:
        if queries[i] >= init:
            started = True
        i += 1

    # Sumar el costo de moverse al primero
    prev = i - 1
    prevValue = queries[prev]
    ans += prevValue - init
    checked[prev] = True
    
    # Subir
    for prev in range(i, len(queries)):
        checked[prev] = True
        ans += queries[prev] - prevValue
        prevValue = queries[prev]
    
    # Bajar
    for prev in range(len(queries) - 1, 0, -1):
        if not checked[prev]:
            checked[prev] = True
            ans += prevValue - queries[prev - 1]
            prevValue = queries[prev - 1]
    
    # Volver a cero
    ans += queries[0]
    
    if debug: print(f"Inicia: {init}")
    if debug: print(f"Tiempo: {ans}")
    return ans/n

scan_asc(8, [2,3,4,6,8,9, 10], 15,  debug = True)