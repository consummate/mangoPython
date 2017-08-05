def eggs(someParameter):
    someParameter.append('hello')

spam=(1,2,3)
eggs(list(spam))
print(spam)

spam1=[1,2,3]
eggs(spam1)
print('spam1=',spam1)
