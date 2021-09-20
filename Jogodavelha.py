# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:45:58 2021

@author: thiago
"""

matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]



def cleanScreen() :
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')



def acess(row, col) :
    return matriz[row][col]

     

def moveController(row, col, player) :
 #Verifica se row e col são válidos e se a posição está livre e preenche a tabela   

    if  type(row) != int :
        return False
    
    if  type(col) != int :
        return False
    
    if row > 2 or row < 0 :
        return False
    
    if col > 2 or col < 0 :
        return False
    
    if acess(row, col) == ' ': 
        
        matriz[row][col] = player
        
        return True 
         
    else : return False 



def playerController(loop) :
# Verifica de quem é a vez, recebe a jogada, validação da jogada 
    
    player = 'X'
    
    if loop % 2 == 0 : player = 'O'
    
    print()
    print('Jogador ', player, " :")
    
    try :
        row = int(input('Escolha a linha: ')) 
        if row == 0 :
            return -1
        col = int(input('Escolha a coluna: '))  
        if col == 0 :
            return -1
    except : 
        print()
        print('Jogada inválida! Jogador ', player, ' refaça a jogada.')
        print()
        return False
    
    if moveController(row - 1, col - 1, player) == False :
        print()
        print('Jogada inválida! Jogador ', player, ' refaça a jogada.')
        print()
        return False
    else :  
        cleanScreen()
        return True


    
def winner(loop) :
    # verifica quem é o vencedor
    
    if loop % 2 == 0 : print('Vitória: O')
    else : print('Vitória: X')


    
def gameController(loop) :
    # Verifica se há vencedor
    
    
    # check row
    for l  in range( 3) :
        if matriz[l][0] == matriz[l][1] and matriz[l][1] == matriz[l][2] \
            and matriz[l][0] != ' ':
              winner(loop) 
              return False
    
    # check col
    for l in range (3) :
        if matriz[0][l] == matriz[1][l] and matriz[1][l] == matriz[2][l] \
            and matriz[0][l] != ' ':
              winner(loop)
              return False
    
    # check diag1
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] \
            and matriz[0][l] != ' ':
                winner(loop)
                return False
    
    # check diag2
    if matriz[2][0] == matriz[1][1] and matriz[1][1] == matriz[0][2] \
            and matriz[0][l] != ' ':
                winner(loop)
                return False
     
    if loop == 9 :
        print('Deu velha! Fim de jogo') 
        print()
        return False

    return True         

    

def display() :
    # Imprime jogo no console
    
    nc = 0
    print('Tecle "0" para sair')
    print('   1 2 3')
    print('  ------')
    
    for row in matriz:
        nc  = nc + 1
        print(nc, end="| ")
        
        for elem in row:
            print(elem,end=' ')
        
        print()
        
        if nc == 3 : nc = 0
   
    
def game() :   #Inicia o jogo
    
    permission = True #Controle do loop
    loop = 0
    moveStatus =  True
    
    display()
    
    while permission :
             
        loop += 1
        
        moveStatus = playerController(loop)
        
        if moveStatus == -1 : # Se for -1 encerra o jogo
            print()
            print('Jogo encerrado!')
            permission = False 
            continue
        
        if moveStatus == False : # Ser for False decrementa o loop
            loop -= 1            # para 
            
            
        permission = gameController(loop)        
        
        display()

game()



