#!/usr/bin/python

DATA = [
        'apple',
        'banana',
        'pear',
        'watermelon',
        'cantaloupe',
        'peach',
    ]

def create_gen(fruit_basket, exclude):
    """
    Create generator of items excluding the items listed in exclude
    """
    return (fruit for fruit in fruit_basket if fruit not in exclude)


def main(exclude=[]):
    generate = create_gen(DATA, exclude)
    print "%s" % generate
    for fruit in generate:
        print fruit

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main()

