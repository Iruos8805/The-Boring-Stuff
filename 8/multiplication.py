import pyinputplus as pyip
import random
import time
import re

noqns = 10
attempt = 0
correct = 0

for question in range(noqns):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f"{question + 1}: {num1} x {num2}\n"
    correctRegex = re.compile(f'^{num1 * num2}$')
    start = int(time.time())
    
    attempt = 0  # Reset attempts for each new question
    
    while attempt < 3:
        end = int(time.time())
        elapsedTime = end - start
        
        if elapsedTime > 8:
            print("Out of time!")
            break
        user_answer = input(prompt)
        if correctRegex.search(user_answer) is None:
            print("Incorrect!")
            attempt += 1
            if attempt == 3:
                print("Out of tries!")
                break  # Move to the next question if attempts are exhausted
        else:
            print("Correct!")
            correct += 1
            break
    
    time.sleep(1)  # Add a delay before the next question

print(f'You got {correct} / {noqns} correct!')
