def guess_the_number():
    print("Think about a number in range 0-1000. I will guess it in not more than 10 attempts.")
    min_number = 0
    max_number = 1000
    while True:
        guess = int((max_number - min_number) / 2) + min_number
        while True:
            print(f"I guess {guess}")
            answers = {"too high": False, "too little": False, "guessed": False}

            for item in answers:
                answers[item] = True if input("Is the number " + item + " (y/n)? ") == 'y' else False

            if answers["guessed"]:
                exit("I won!")

            elif answers["too high"]:
                max_number = guess
                break

            elif answers["too little"]:
                min_number = guess
                break

            else:
                print("Don't cheat!")


if __name__ == '__main__':
    guess_the_number()
