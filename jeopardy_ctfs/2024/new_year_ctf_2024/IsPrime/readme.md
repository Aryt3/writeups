# IsPrime

## Description
```
Remember what numbers are called prime?

In this problem, everything is also simple - you receive a number as input and say whether it is prime or not.

Connect and decide. 50 rounds - and the flag is yours!

nc ctf.mf.grsu.by 9000
```

## Writeup

Connecting to the service I obtained the format in which the prime number is being send to us. <br/>
```sh
kali@kali nc ctf.mf.grsu.by 9000
Помните, какие числа называются **простыми** ?
В этой задаче тоже все просто - получаете на вход число и говорите, является оно простым или нет.
50 раундов - и флаг ваш  ...
Время на ответ - не больше 5 секунд.
Ваш ответ: YES или NO

Раунд 1/50
761

```

Having the format I wrote a simple python script to connect to the socket and solve the challenge. <br/>
```py
import socket

# Function to check if num is prime-num
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Connection function
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("ctf.mf.grsu.by", 9000))
        found_flag = False 

        while True:
            data = s.recv(1024).decode()
            print(data) 

            if "grodno{" in data:
                found_flag = True
                break

            if not found_flag:                
                if data.split()[-1] != 'YES' and data.split()[-1] != 'NO':
                    number = int(data.split()[-1])
                    result = "YES" if is_prime(number) else "NO"

                    s.send(f"{result}\n".encode()) 

if __name__ == "__main__":
    main()
```

Using the script I solved the challenge and obtained the flag `grodno{417710pr!m3_numb3r_!s_d!v!s!b13_0n1y_by_1_4nd_by_!+s31fdf182a}` which concludes this writeup.