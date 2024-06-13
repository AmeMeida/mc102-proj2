from normalize import Normal, get_extremes, normalize

def least_choices(normals: list[Normal]):
    least_choices = min([(normal, len(normal.responses)) for normal in normals], key=lambda case: case[1])[1]
    return [normal for normal in normals if len(normal.responses) <= least_choices]

def most_choices(normals: list[Normal]):
    most_choices = max([(normal, len(normal.responses)) for normal in normals], key=lambda case: case[1])[1]
    return [normal for normal in normals if len(normal.responses) >= most_choices]

def minmax(normals: list[Normal]):
    maxes = [(normal, max(normal.response_sums)) for normal in normals]
    low_score = min(maxes, key=lambda case: case[1])[1]

    return [normal for (normal, score) in maxes if score <= low_score]

def maxmin(normals: list[Normal]):
    mins = [(normal, min(normal.response_sums)) for normal in normals]
    high_score = max(mins, key=lambda case: case[1])[1]

    return [normal for (normal, score) in mins if score <= high_score]

def isolate_doubles(normals: list[Normal]):
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
    high_score = max(normals, key=lambda normal: normal.score).score
    return [normal for normal in normals if normal.score <= high_score]

def friendly(normals: list[Normal], friend_tiles: list[tuple[int, int]]):
    for normal in normals:
        friend_normals = normalize(normal.responses, friend_tiles, normal.extremes)

def most_common(tiles: list[tuple[int, int]], 
                normals: list[Normal]):
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
