import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number+=1

def sum_primes(start_num,end_num):
    total=2
    for next_prime in get_primes(start_num):       
        if next_prime>end_num:
            break
        total+=next_prime
    print(total)
    return
        
            


if __name__ == '__main__':
    sum_primes(3,20)
        


    
    
