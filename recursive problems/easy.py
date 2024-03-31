def decimalToBinary(number , result):
    if number == 1 :
        return '1'+result
    result = str(number % 2) + result
    return decimalToBinary(number//2 , result)


def sumOfNNaturalNums(n):
    if n==1:
        return n 
    return n+sumOfNNaturalNums(n-1)
    

def fibonaci(n):
    def fibonacci(n):
        if n ==1 :
            return 1 
        if n==0:
            return 0
        return fibonacci(n-1)+fibonacci(n-2)
    for i in range(n):
        print(fibonacci(i))
fibonaci(10)