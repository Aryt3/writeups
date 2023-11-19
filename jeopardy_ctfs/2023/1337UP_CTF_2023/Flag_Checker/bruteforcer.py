import subprocess
import time

binary_path = "/home/kali/Desktop/flagchecker"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()?_*#"

start_time = time.time()

for first_char in characters:
    for second_char in characters:
        for third_char in characters:
            flag = f"INTIGRITI{{tHr33_{first_char}_{second_char}T{third_char}}}"
            
            command = [binary_path]

            try:
                result = subprocess.run(command, input=flag, text=True, capture_output=True, check=True)

                print(f"Trying flag: {flag}", end='\r')

                if "Wrong flag" not in result.stdout:
                    print(f"Found the correct flag: {flag}")

                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    print(f"\nTotal time taken: {elapsed_time:.2f} seconds")
                    exit() 

            except subprocess.CalledProcessError as e:
                print(f"Error executing with flag {flag}: {e}")
