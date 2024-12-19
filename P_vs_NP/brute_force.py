#Exercise in verifying P vs NP solutions
##Basically using factorials to brute force a password

def get_num_guesses(length):

    previous_number = []
    
    for char in range(1, length + 1):
        previous_number.append(26 ** char)
    
    final_number = sum(previous_number)

    return final_number  


#Alt - clean
def get_num_guesses(length):
    total = 0
    for i in range(length):
        total += 26 ** (i + 1)
    return total