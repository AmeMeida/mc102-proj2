def normalize(plays: list[tuple[int, int]], 
        responses: list[tuple[int, int]], extremes: tuple[int, int]):
    normal: list[tuple[int, list[int]]] = []
    
    open("normal.local.txt", "w").close()
    file = open("normal.local.txt", "a")

    for play in plays:
        normal.append((play, (play[0] + play[1]), []))
        
        new_extremes = extremes

        if extremes[0] == play[0]:
            new_extremes = (play[1], extremes[1])
        elif extremes[0] == play[1]:
            new_extremes = (play[0], extremes[1])
        elif extremes[1] == play[0]:
            new_extremes = (play[1], extremes[0])
        elif extremes[1] == play[1]:
            new_extremes = (play[0], extremes[0])

        possible_responses = [response for response in responses 
                              if response[0] in new_extremes 
                              or response[1] in new_extremes]

        for response in possible_responses:
            normal[-1][2].append(response[0] + response[1])

        file.write(" ".join([str(value) for value in normal[-1]]) + "\n")

    file.close()
    return normal
