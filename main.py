import random


def numberGenerator() -> int:
    num = random.randint(1, 100)
    return num


def displayIntro():
    print('''Welcome to the our mini-game
        Guess The Number, which is a simple guessing game where a user is supposed to guess a number 
        between 0 and 100 in a maximum of 10 attempts. 
        The game will end after 10 attempts and if you failed to guess the number, and then you lose the game!
          ''')


def displayEnd(result):
    if result:
        print('''________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________''')
    else:
        print(''' __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   

       ''')


def doYouWantToPlayAgain():
    x = str(input("Do you want to play again? "))
    if x == "yes":
        return True
    else:
        return False


def hint(num):
    if num % 2 == 0:
        print("Hint: The number is even")
        if num % 4 == 0:
            print("Hint: The number is divisible by 4")
        elif num % 6 == 0:
            print("Hint: The number is divisible by 6")
        elif num % 8 == 0:
            print("Hint: The number is divisible by 8")

    elif num % 2 != 0:
        print("Hint: The number is odd")
        if num % 3 == 0:
            print("Hint: The number is divisible by 3")
        elif num % 5 == 0:
            print("Hint: The number is divisible by 5")
        elif num % 7 == 0:
            print("Hint: The number is divisible by 7")
        elif num % 9 == 0:
            print("Hint: The number is divisible by 9")


def play():
    num = numberGenerator()
    guessW = int(input("Enter the number: "))

    while guessW > 100 or guessW < 0:
        guessW = int(input("Enter the number: "))
    state = 7
    while num != guessW and state > 0:
        if 0 < guessW - num <= 10:
            print("Your number is higher but near")
            state = state - 1
            guessW = int(input("Enter the number: "))

        elif guessW - num > 10:
            print("Your number is too high")
            state = state - 1
            hint(num)
            guessW = int(input("Enter the number: "))
        elif -10 <= guessW - num < 0:
            print("Your number is lower but near")
            state = state - 1
            guessW = int(input("Enter the number: "))

        elif guessW - num < - 10:
            print("Your number is too low")
            hint(num)
            state = state - 1
            guessW = int(input("Enter the number: "))
        if num == guessW:
            return guessW

    if state == 0:
        print("The number was ", num)


def guessTheNumber():
    whileCond = True
    while whileCond:
        displayIntro()
        result = play()
        displayEnd(result)
        whileCond = doYouWantToPlayAgain()


if __name__ == "__main__":
    guessTheNumber()
