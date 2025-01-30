i=1
while i<=5:
    print(i)
    i=i+1
print("Done")


i=1
while i<=5:
    print('*'*i)
    i=i+1


secret_number = 9
guess_count = 1
guess_limt = 3
while guess_count<=guess_limt:
    guess_secret_number = int(input("Guess_secret_number : "))
    guess_count+=1
    if guess_secret_number==secret_number:
        print("Congratulations You Won!")
        break
else:
    print("Sorry maximum attempts completed,you failed to guess the secret number try for next time!")


