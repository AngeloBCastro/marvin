def fizzbuzz(num1,num2):
    while num1 <= num2:
        if (num1 %3 == 0 and num1 %5 ==0):
            print(str(num1) + (" FizzBuzz"))
            num1 +=1
        elif num1 %3 == 0:
            print(str(num1) + (" Fizz"))
            num1 += 1
        elif num1 %5 == 0:
            print(str(num1) + ("Buzz"))
            num1 += 1
        else:
            print(num1)
            num1 += 1