import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

logging.debug('Start is Program')
def factorials(input):
    logging.debug('start of fact')
    total = 1
    for i in range (1, input + 1):
        total *= i
        logging.critical('i is %s toatal is %s' %(i,total))
    return total

print(factorials(5))

logging.debug('End of Program')