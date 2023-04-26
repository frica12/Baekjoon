def isPrime(n):
    if(n == 2 or n == 3):
        return True
    
    elif(n % 2 == 0):
        return False
    
    for i in range(3, int(n/2)):
        if(n % i == 0):
            return False
    return True

while True:
    num = int(input())
    
    if(num == -1):
        break

    elif(num < 2):
        print("잘못 입력하였습니다. 2 이상의 값을 입력하여 주십시오.")
        continue

    else:
        if(isPrime(num)):
            print("소수입니다.")
        else:
            print("소수가 아닙니다.") 