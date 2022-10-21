
def create_matrix(key): 
    key = key.upper()   
    matrix = [[0 for i in range (5)] for j in range(5)]     #5*5 matrix
    letters_added = []    
    row = 0                 
    col = 0

    for letter in key:  
        if letter not in letters_added:     
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    
    var = ''.join(letters_added)
    return var

    


def separate_same_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=2   
    return message
    





if __name__=='__main__':

    print(create_matrix('fantastic'))
    print(separate_same_letters('committee'))
