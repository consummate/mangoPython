import logging
#logging.disable(logging.CRITICAL)
#logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='programLog.txt', level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, 1+n):
        total *= i
        logging.debug('i is '+str(i)+', total is '+str(total))
    logging.debug('End of fatorial(%s)' %(n))
    return total

print(factorial(5))
logging.debug('End of program')
