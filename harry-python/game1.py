import random

n = random.randint(1,50)

a = -1
guesses = 1

while(a != n):
    guesses += 1

    a = int(input('Guess the number:'))

    if(a > n):
        print('lower number please')
    elif(a < n):
        print('Higher number please')
    else:
        print('correct guess')

print(f'You have guessed the number {n} correctly in {guesses} attempts ')