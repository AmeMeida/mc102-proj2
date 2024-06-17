from dataclasses import dataclass

def get_extremes(extremes: tuple[int, int] | None, tile: tuple[int, int] | None):
    """ Indica quais serão os novos extremos do tabuleiro após a jogada
    """

    side = 0

    if not tile:
        return extremes

    if not extremes or len(extremes) == 0:
        return tile, side

    if extremes[0] == tile[0]:
        new_extremes = (tile[1], extremes[1])
    elif extremes[0] == tile[1]:
        new_extremes = (tile[0], extremes[1])
    elif extremes[1] == tile[0]:
        new_extremes = (tile[1], extremes[0])
        side = 1
    elif extremes[1] == tile[1]:
        new_extremes = (tile[0], extremes[0])
        side = 1

    return new_extremes, side

@dataclass
class Normal:
    tile: tuple[int, int]
    side: 0 | 1
    responses: list[tuple[int, int]]
    extremes: tuple[int, int] 

    @property
    def score(self):
        if self.tile == None:
            return -1
        return self.tile[0] + self.tile[1]
    
    @property
    def will_skip(self):
        return len(self.responses) == 0

    @property
    def response_sums(self):
        if self.will_skip:
            return [0]

        return [response[0] + response[1] for response in self.responses]


def normalize(plays: list[tuple[int, int]], 
        responses: list[tuple[int, int]], extremes: tuple[int, int]) -> list[Normal]:
    """ 
    Representação formal de jogo de cada possibilidade de resposta
    a cada jogada feita.
    """

    normals: list[Normal] = []
    
    if len(plays) <= 0:
        possible_responses = [response for response in responses 
                              if response[0] in extremes
                              or response[1] in extremes]

        normals.append(Normal(None, 0, possible_responses, extremes))

    for tile in plays:
        new_extremes, side = get_extremes(extremes, tile)

        possible_responses = [response for response in responses 
                              if response[0] in new_extremes 
                              or response[1] in new_extremes]

        normals.append(Normal(tile, side, possible_responses, new_extremes))

    return normals
