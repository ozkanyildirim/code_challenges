def minion_game(string):
    '''
    Both players are given the same string,S
    Both players have to make substrings using the letters of the string,S
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.     
    '''
    vowel = 'AEIOU'
    vowel_gamer  = 0
    consonant_gamer  = 0    
    for i in range(len(string)):
        if string[i] in vowel:
                vowel_gamer +=  len(string) - i      
        else:
                consonant_gamer  += len(string) - i

    if  consonant_gamer > vowel_gamer:        
        print(f'Stuart {consonant_gamer}')
    elif consonant_gamer < vowel_gamer: 
        print(f'Kevin {vowel_gamer}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
