from normalize import Normal, get_extremes, normalize

def least_choices(normals: list[Normal]):
    """ Seleciona a opção mais provável de forçar que o oponente passe"""
    least_choices = min([(normal, len(normal.responses)) for normal in normals], key=lambda case: case[1])[1]
    return [normal for normal in normals if len(normal.responses) <= least_choices]

def minmax(normals: list[Normal]):
    """ Seleciona a opção com o menor ganho máximo para o oponente"""
    maxes = [(normal, max(normal.response_sums)) for normal in normals]
    low_score = min(maxes, key=lambda case: case[1])[1]

    return [normal for (normal, score) in maxes if score <= low_score]

def isolate_doubles(normals: list[Normal]):
    """ Se houver carroça (peça dupla), seleciona somente elas. 
    Senão, não faz nada."""

    has_double = False

    for normal in list(normals):
        tile = normal.tile
        if tile == None:
            continue

        if tile[0] == tile[1]:
            if not has_double:
                normals = []
                has_double = True

            normals.append(normal)

    return normals

def greedy(normals: list[Normal]):
    """ Seleciona as peças com valor somado mais alto."""
    high_score = max(normals, key=lambda normal: normal.score).score
    return [normal for normal in normals if normal.score <= high_score]

def most_common(tiles: list[tuple[int, int]], 
                normals: list[Normal]):
    """ Seleciona a peça que resulta na combinação mais comum 
    dentre suas próprias peças."""

    numbers = {}

    for tile in tiles:
        numbers[tile[0]] = numbers.get(tile[0], 0) + 1

        if tile[0] != tile[1]:
            numbers[tile[1]] = numbers.get(tile[1], 0) + 1

    max_frequency = max(numbers.keys())
    most_frequent = [number for number in numbers 
                     if numbers[number] >= max_frequency]

    best_normals = [normal for normal in normals 
                    if normal.tile != None
                    and normal.extremes[0] in most_frequent 
                    or normal.extremes[1] in most_frequent]

    if len(best_normals) == 0:
        best_normals = normals

    return best_normals
