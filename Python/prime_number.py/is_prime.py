def is_prime(num):
    flag = True

    if num == 1:
        flag = True
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
    else:
        flag = True
    
    if flag == False:
        return False
    else:
        return True