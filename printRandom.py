import random,sys
for i in range(5):
    print(random.randint(1,10))

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('You typed11 '+response+'.')
        sys.exit()
    print('You typed '+response+'.')
    
