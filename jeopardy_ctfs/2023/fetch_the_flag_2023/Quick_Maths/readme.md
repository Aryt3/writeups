# Quick Maths

## Description
```
To try and get better grades in math, I made a program that gave me timed quizzes. Funny thing is that as I got better at the questions in this test, I got worse grades on my math tests.

NOTE: Float answers are rounded to 1 decimal points.


NOTE: And here's another twist... the answers to division questions depend on integer division or double division. I.e.,
3/5 = 0
3/5.0 = .6
```

## Writeup

Starting off a netcat command is provided to us. <br/>
```sh
kali@kali nc challenge.ctf.games 31113

Welcome! To be honest, I am a Computer Science major but I was never any good at math in school. I seemed to always get Cs.  

Note to self: Round all answers to 1 decimal point, where applicable.

Do you want to give it a chance? (Y/n): y
Awesome, good luck!
What is 57.6 - 25.6? 32
Too Slow!!!
Good bye :(
```

This basically means that we have to make a script to automatically reply with the correct result. <br/>
For things like this I personally prefer python and the `socket` library. <br/>
```py
import socket
import re

def extract_equation(text):
    match = re.search(r'What is (\d+(?:\.\d+)?) ([+\-*/]) (\d+(?:\.\d+)?)\?', text)
    if match:
        check = True
        num1_str = match.group(1)
        operator = match.group(2)
        num2_str = match.group(3)

        try:
            num1 = int(num1_str)
            num2 = int(num2_str)

        except ValueError:
            num1 = float(num1_str)
            num2 = float(num2_str)
            check = False

        if operator == "+":
            yeet = num1 + num2
            result = round(yeet, 1)
        elif operator == "-":
            yeet = num1 - num2
            result = round(yeet, 1)
        elif operator == '/':
            if check == True:
                result = num1 // num2
            else:
                yeet = num1 / num2
                decimal_part = str(yeet).split('.')[1]
                rounded_decimal = str(round(float("0." + decimal_part), 1))
                result = int(str(yeet).split('.')[0]) + float(rounded_decimal)

        elif operator == "*":
            yeet = num1 * num2
            result = round(yeet, 1)
        return result
    else:
        return None

def main():
    host = "challenge.ctf.games"
    port = 31113

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        found_flag = False 

        while True:
            data = s.recv(1024).decode()
            print(data) 

            if "flag{" in data:
                found_flag = True
                break

            if not found_flag:
                if "Do you want to give it a chance?" in data:
                    s.send("Y\n".encode())
                elif "What is" in data:
                    solve = extract_equation(data)
                    print(solve)
                    if solve is not None:
                        s.send(f"{solve}\n".encode()) 

if __name__ == "__main__":
    main()
```

After some adjustments I was able to create a workign script which implements the feature for checking for floating points. <br/>
```sh
python3 servicer.py 

Welcome! To be honest, I am a Computer Science major but I was never any good at math in school. I seemed to always get Cs.  

Note to self: Round all answers to 1 decimal point, where applicable.

Do you want to give it a chance? (Y/n): 
Awesome, good luck!

What is 99.3 - 57.3? 
42.0
Correct!

What is 32.6 * 84.4? 
2751.4
Correct!

---------------------------------

What is 22.9 - 79.7? 
-56.8
Correct!

Great job, you just answered 100 math problems! You might not fail the next math test. Here is your reward!!!
 flag{77ba0346d9565e77344b9fe40ecf1369}
```