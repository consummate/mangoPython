def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'becon'
def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
bacon()
ham()
