from basic_players import Player
from normalize import normalize

all_tiles = set()

for i in range(0, 10):
    for j in range(0, 10):
        if (j, i) not in all_tiles:
            all_tiles.add((i, j))

# Implemente neste arquivo seus jogadores

# Jogador que não faz nada. Subsitua esta classe pela(s) sua(s), ela(s) deve(m) herdar da classe Player
class MinMaxPlyer(Player):
    opponent_tiles: set[tuple[int, int]]

    def __init__(self):
        self.opponent_tiles = all_tiles
        super().__init__(0, "Ninguém")

    def play(self, board_extremes, play_hist):
        if len(board_extremes) == 0:
            return self.tiles[0]

        if len(play_hist) <= 3:
            self.opponent_tiles -= set(self.tiles)
        elif play_hist[-3][-1] == None:
            extremes = play_hist[-3][1]

            for tile in list(self.opponent_tiles):
                if extremes[0] in tile or extremes[1] in tile:
                    self.opponent_tiles.remove(tile)

        self.opponent_tiles -= {tile[-1] for tile in play_hist}
        
        playable_tiles = [tile for tile in self.tiles if tile[0] in board_extremes or tile[1] in board_extremes]

        if len(playable_tiles) == 0:
            return 1, None

        normal = normalize(playable_tiles, list(self.opponent_tiles), board_extremes)

        maxes = [(play, score, max(responses)) if len(responses) > 0
                  else (play, score, -1)
                  for play, score, responses in normal]
        
        best_play = min(maxes, key=lambda case: case[2])

        return 1, best_play[0]
		
# Função que define o nome da dupla:
def pair_name():
    return "algum nome" # Defina aqui o nome da sua dupla

# Função que cria a dupla:
def create_pair():
    return (MinMaxPlyer(), MinMaxPlyer()) # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.	
