import os
import socket
import sys
import random

# Quotes about not giving up
giveup = ["Success is not final, failure is not fatal: It is the courage to continue that counts.",
          "It always seems impossible until it is done.",
          "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.",
          "Never give up, for that is just the place and time that the tide will turn.",
          "You may encounter many defeats, but you must not be defeated."]

# Quotes about creativity
creativity = ["Creativity is intelligence having fun.",
              "Every artist was first an amateur.",
              "The chief enemy of creativity is good sense.",
              "Creativity takes courage.",
              "You can't use up creativity. The more you use, the more you have."]

# More quotes can be added here;

print(f'Hello {socket.gethostname()}!')
status = input('How are you?\n> ')
if any(keyword in status.lower() for keyword in ['go', 'per', 'y']):
    os.system('cls')
    print(f'> {status}')
    print('WoW! Good to hear, do you even need motivation?')
    motivation = input('> ')
    if any(keyword in motivation.lower() for keyword in ['y', 'yes', 'ya', 'yy']):
        print('We currently only have 2 category of quotes, which do you think would suit your mood right now?')
        a = input('A quote about not giving up or a quote about creativity?\n> ')
        if any(keyword in a.lower() for keyword in ['givin', 'give']):
            os.system('cls')
            print(random.choice(giveup))
            input(' ')
        if any(keyword in a.lower() for keyword in ['creat']):
            os.system('cls')
            print(random.choice(creativity))
            input(' ')
        else:
            os.system('cls')
            print('Whoops, this was not an option! I still think you need one, take that!')
            print(random.choice(random.choice([giveup, creativity])))
            input(' ')
    else:
        print("Oh WoW! You're actually strong! I guess you dont need my help, have a good day!")
        sys.exit(None)
else:
    os.system('cls')
    print('Oh crapppp! Here, we currently only have 2 category of quotes, which do you think would suit your mood right now?')
    a = input('A quote about not giving up or a quote about creativity?\n> ')
    if any(keyword in a.lower() for keyword in ['givin', 'give']):
        os.system('cls')
        print(random.choice(giveup))
        input(' ')
    if any(keyword in a.lower() for keyword in ['creat']):
        os.system('cls')
        print(random.choice(creativity))
        input(' ')
    else:
        os.system('cls')
        print('Whoops, this was not an option! I still think you need one, take that!')
        print(random.choice(random.choice([giveup, creativity])))
        input(' ')
