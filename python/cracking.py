#!/usr/bin/python

def count_twos(n=5):
    """
    Count the number of 2s between 0 and n
    """
    count = 0
    for num in xrange(int(n)):
        for letter in str(num):
            if str(2) == letter:
                count += 1
    print count


if __name__=='__main__':
    import sys
    try:
        count_twos(sys.argv[1])
    except IndexError:
        count_twos()

