from normalize import Normal, get_extremes

def least_choices(normals: list[Normal]):
    least_choices = min([(normal, len(normal.responses)) for normal in normals], key=lambda case: case[1])[1]
    return [normal for normal in normals if len(normal.responses) <= least_choices]

def minmax(normals: list[Normal]):
    maxes = [(normal, max(normal.response_sums)) for normal in normals]
    low_score = min(maxes, key=lambda case: case[1])[1]

    return [normal for (normal, score) in maxes if score <= low_score]

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
    return max(normals, key=lambda normal: normal.score)

def most_common(tiles: list[tuple[int, int]], 
                playable_tiles: list[Normal],
                extremes: tuple[int, int]):
    numbers = {}

    for tile in tiles:
        numbers[tile[0]] = numbers.get(tile[0], 0)

        if tile[0] != tile[1]:
            numbers[tile[1]] = numbers.get(tile[1], 0)

    max_frequency = max(numbers.keys())
    most_frequent = [number for number in numbers if numbers[number] >= max_frequency]

    best_normals = []

    for normal in playable_tiles:
        tile = normal.tile
        if tile == None:
            continue

        for number in most_frequent:
            if number in tile:
                best_normals.append(normal)

    if len(best_normals) == 0:
        best_normals = playable_tiles

    return best_normals
