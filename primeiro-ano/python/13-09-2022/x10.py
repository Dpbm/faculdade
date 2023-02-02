def count_number(number, total=0):
    if(number == None):
        return total
    
    if(number <= 9):
        return count_number(None, total + 1)  
    
    return count_number(int(str(number)[:len(str(number))-1]), total + 1)


print(count_number(13120))