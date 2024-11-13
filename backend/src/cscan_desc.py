def cscan_desc(init, queries, tracks = -1, debug = False):
    ans = 0
    
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
    checked[prev-1] = True
    print("bajando", ans, checked)
    # subir solo si tiene que hacerlo
    
    if not checked[-1]:
        ans += queries[-1]-prevValue  # Sumar la distancia desde arriba a abajo
    prevValue = queries[-1]

    print("bajando", ans, checked)

    # Bajar
    for prev in range(len(queries)-1, 0, -1):
        if not checked[prev-1]:
            
            checked[prev-1] = True
            ans += abs(prevValue - queries[prev - 1])
            prevValue = queries[prev - 1]
            print("add", prev, ans, checked)

    if debug: print(f"Inicia: {init}")
    if debug: print(f"Resultado: {ans}")
    return ans

cscan_desc(8, [2,3,4,6,8,9, 10], 15, True)
