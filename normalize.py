from dataclasses import dataclass

def get_extremes(extremes: tuple[int, int], tile: tuple[int, int]):
    side = 0
    new_extremes = None

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
    _score: int = 0

    @property
    def score(self):
        return self._score
    
    def __iadd__(self, score: int):
        self._score += score

    @property
    def tile_value(self):
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


def normalize(tiles: list[tuple[int, int]], 
        responses: list[tuple[int, int]], extremes: tuple[int, int]) -> list[Normal]:
    normals: list[Normal] = []
    
    # pass_responses = [response for response in responses 
    #                   if response[0] in extremes
    #                   or response[1] in extremes]
    
    # if len(pass_responses) <= 0:
    #     normals.append(Normal(None, 0, pass_responses))

    for tile in tiles:
        new_extremes, side = get_extremes(extremes, tile)

        possible_responses = [response for response in responses 
                              if response[0] in new_extremes 
                              or response[1] in new_extremes]

        normals.append(Normal(tile, side, possible_responses))

    return normals
