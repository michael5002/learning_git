print('basit')
x = [1,2,3,4,5,6,7,8,9,0]
def game():

    input('enter number:')
    import random
    print('My number is:', random.choice(x))
    if input == random.choice(x):
     print('Correct!\n Welldone')
    else:
     print('Wrong')

name =input('Hello!, what is your name? ')
print('Hi,' + name)

gm = input('wanna play a game ' + name+'?')
# condition
if gm == 'yes':
    print('Terrific!\n So we are gonna play a guessing game\n i think of a number and guess which it is\n let us begin.')
    print(game())
else:
    quit()

qst = input('do you you wnt to continue? ')

if qst== 'yes':
    print('Great!')
    print(game())

else:
    quit()
