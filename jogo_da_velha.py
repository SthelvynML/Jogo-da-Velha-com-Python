import random
import os

class jogoDaVelha:
    def __init__(self):
        self.reset()    

    def print_board(self):
        print('')
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('-----------')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('-----------')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2])
        
    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.done = ''  # corrigido: string vazia ao invés de espaço
        
    def check_win_or_draw(self):
        dict_win = {}
        
        for i in ['X', 'O']:
            # Horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]
            
            # Verticais
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]
            
            # Diagonais
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]
        
        if dict_win['X']:
            self.done = 'x'
            print('X venceu!')
            return
        
        elif dict_win['O']:
            self.done = 'o'
            print('O venceu!')
            return
            
        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ':
                    c += 1

        if c == 9:
            self.done = 'd'        
            print('Empate!')
            return
    
    def get_player_move(self):
        invalid_mode = True
        
        while invalid_mode:
            try:
                print('Digite a linha do seu próximo lance (0 a 2):')
                x = int(input())
                
                print('Digite a coluna do seu próximo lance (0 a 2):')
                y = int(input())
                
                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Coordenadas inválidas!')
                    continue
                    
                if self.board[x][y] != ' ':
                    print('Posição já preenchida.')
                    continue
            except Exception as e:
                print('Erro:', e)
                continue
            
            invalid_mode = False
        self.board[x][y] = 'X'    
    
    def make_move(self):
        list_moves = []
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    list_moves.append((i, j))
        
        if list_moves:
            x, y = random.choice(list_moves)
            self.board[x][y] = 'O'

# Execução principal
jogo_da_velha = jogoDaVelha()    

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    jogo_da_velha.print_board()
    
    while jogo_da_velha.done == '':
        jogo_da_velha.get_player_move()
        jogo_da_velha.check_win_or_draw()
        if jogo_da_velha.done != '':
            break

        jogo_da_velha.make_move()
        jogo_da_velha.check_win_or_draw()

        os.system('cls' if os.name == 'nt' else 'clear')
        jogo_da_velha.print_board()
    
    print('Digite 1 para sair do jogo ou qualquer outra tecla para jogar novamente.')
    try:
        next = int(input())
        if next == 1:
            break
    except:
        pass
    
    jogo_da_velha.reset()
