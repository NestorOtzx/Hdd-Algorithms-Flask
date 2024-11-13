def cscan_asc(init, queries, tracks = -1, debug = False):
    ans = 0
    
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

    # Bajar solo si tiene que bajar
    prevValue = 0
    if not checked[0]:
        ans += queries[-1]  # Sumar la distancia desde arriba a abajo

    # Subir nuevamente
    for prev in range(len(queries)):
        if not checked[prev]:
            checked[prev] = True
            ans += queries[prev] - prevValue
            prevValue = queries[prev]

    if debug: print(f"Inicia: {init}")
    if debug: print(f"Resultado: {ans}")
    return ans

cscan_asc(8, [2,3,4,6,8,9, 10], 15, True)
