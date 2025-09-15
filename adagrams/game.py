from random import randint

def draw_letters():
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    #make a new list named pool_list
    pool_list=[]
    for key, value in LETTER_POOL.items():
        for i in range(0,value):
            pool_list.append(key)
    

    #draw ten times from pool_list randomly and remove the tile from
    #the pool_list
    drawn_list=[]
    total_index=len(pool_list)
    draw_time=10
    for i in range(0,draw_time):
        index=randint(0,total_index-1)
        element=pool_list.pop(index)
        drawn_list.append(element)
        total_index-=1
    
    #check the frequency of letter that is more than that in LETTER_POOL
    letter_freq = {}
    for letter in drawn_list:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1

    
    return drawn_list    

    
    



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass