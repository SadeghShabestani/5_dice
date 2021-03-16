import termcolor2
import random

computer = random.randint(1, 6)
print(termcolor2.colored(f"Computer: {computer}", color="green"))
while computer == 6:
    computer = random.randint(1, 6)
    print(termcolor2.colored(f"Computer: {computer}", color="green"))
else:
    print(termcolor2.colored(f"TryAgain",color="red"))



