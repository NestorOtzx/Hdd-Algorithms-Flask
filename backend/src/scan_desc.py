def scan_desc(init, queries, tracks = -1, debug = False):
    ans = 0
    
    n = len(queries) 
    queries.sort()  # Ordenar las consultas
    if (tracks == -1):
        tracks = queries[-1]
    else:
        queries.append(tracks)
    checked = [False] * len(queries)  # Inicializar un arreglo de booleanos
    
    # Encontrar el índice inicial
    i = len(queries) - 1
    started = False
    while i >= 0 and not started:
        if queries[i] <= init:
            started = True
        i -= 1
    
    # Sumar el costo de moverse al primero
    prev = i + 1
    prevValue = queries[prev]
    ans += init - prevValue
    checked[prev] = True

    # Bajar
    for prev in range(i, 0, -1):
        checked[prev] = True
        ans += prevValue - queries[prev - 1]
        prevValue = queries[prev - 1]

    # Volver a cero
    ans += queries[0]
    prevValue = 0

    # Subir
    for prev in range(i, len(queries)):
        if not checked[prev]:
            checked[prev] = True
            ans += queries[prev] - prevValue
            prevValue = queries[prev]

    if debug: print(f"Inicia: {init}")
    if debug: print(ans)
    return ans / n

scan_desc(8, [2,3,4,6,8,9], 15, debug = True)