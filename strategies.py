from normalize import Normal, get_extremes

weights = {
    "choices": 7,
    "minmax": 3,
    "doubles": 400,
    "greedy": 3,
    "common": 4,
    "pass": -800
}

def least_choices(normals: list[Normal]):
    for normal in normals:
        normal += (55 - len(normal.responses)) * weights["choices"]

def minmax(normals: list[Normal]):
    for normal in normals:
        normal += (18 - max(normal.response_sums)) * weights["minmax"]

def doubles(normals: list[Normal]):
    for normal in normals:
        if normal.tile and normal.tile[0] == normal.tile[1]:
            normal += weights["doubles"]

def greedy(normals: list[Normal]):
    for normal in normals:
        normal += normal.score * weights["greedy"]

def isolate_max_score(normals: list[Normal]):
    best_score = max(normals, key=lambda normal: normal.score).score
    return [normal for normal in normals if normal.score <= best_score]

def may_pass(normals: list[Normal]):
    for normal in normals:
        if normal.tile != None:
            continue

        if len(normal.responses) != 0:
            continue

        normal += weights["pass"]

def most_common(tiles: list[tuple[int, int]], 
                normals: list[Normal],
                extremes: tuple[int, int]):
    numbers = {}

    for tile in tiles:
        numbers[tile[0]] = numbers.get(tile[0], 0) + 1

        if tile[0] != tile[1]:
            numbers[tile[1]] = numbers.get(tile[1], 0) + 1

    for normal in normals:
        if normal.tile:
            new_extremes, _ = get_extremes(extremes, normal.tile)
        else:
            new_extremes = extremes

        normal += (numbers.get(new_extremes[0], 0) + numbers.get(new_extremes[1], 0)) * weights["common"]
