from basic_players import Player
from normalize import normalize, get_extremes
import strategies as s

all_tiles = set()

for i in range(0, 10):
    for j in range(i, 10):
        all_tiles.add((i, j))

# Implemente neste arquivo seus jogadores
class MinMaxPlyer(Player):
    opponent_tiles: set[tuple[int, int]]

    def __init__(self, ra=0, name="Ninguém", image_path="img/none.jpg"):
        self.opponent_tiles = None
        super().__init__(ra, name, image_path)

    def play(self, board_extremes, play_hist):
        # caso base. como o construtor não é chamado, 
        # reseta as informações da classe
        if len(play_hist) <= 3:
            self.opponent_tiles = all_tiles.copy() - set(self.tiles)

        if len(play_hist) >= 3 and play_hist[-3][-1] == None:
            extremes = play_hist[-3][1]

            for tile in list(self.opponent_tiles):
                if extremes[0] in tile or extremes[1] in tile:
                    self.opponent_tiles.remove(tile)

        self.opponent_tiles -= {tile[-1] for tile in play_hist}

        playable_tiles = \
            [tile for tile in self.tiles 
             if tile[0] in board_extremes 
             or tile[1] in board_extremes] \
            if len(board_extremes) > 0 else self.tiles

        if len(playable_tiles) == 0:
            return 1, None
        
        normals = normalize(playable_tiles, list(self.opponent_tiles),
                            board_extremes)

        normals = s.isolate_doubles(normals)
        normals = s.least_choices(normals)
        normals = s.minmax(normals)

        normals = s.most_common(self.tiles, normals)
        normals = s.greedy(normals)

        best_play = normals[0]
        return best_play.side, best_play.tile

# Função que define o nome da dupla:
def pair_name():
    return "gabriela planas fa clube" # Defina aqui o nome da sua dupla

# Função que cria a dupla:
def create_pair():
    return (MinMaxPlyer(0, "Metang", "img/Metang.webp"), MinMaxPlyer(1, "Bulbasaur", "img/Bulbasaur.png")) # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.	
