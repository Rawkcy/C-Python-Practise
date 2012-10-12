#!/usr/bin/python

LETTER_MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
words = []

def recur_wordify(string, digits):
    """
    recursively find the possible words
    """
    letters = LETTER_MAP[int(digits[0])]
    if len(digits) == 1:
        # we're at the last number
        for i in xrange(len(letters)):
            # if we were to check if it was an english word
            #word = string + letters[i]
            #if is_word(word):
            #    words.append(word)
            words.append(string + letters[i])
        return
    for i in xrange(len(letters)):
        recur_wordify(string + letters[i], digits[1:])

def iter_wordify(digits):
    """
    iteratively find the possible words
    """
    positions = [0]*len(digits)
    caps = [len(letters) for letters in digits]
    def inc_lst(lst):
        """
        lst -> num; increment; num -> lst
        TODO::
            need to cap each position's incrementation
        """
        lst[-1] = lst[-1] + 1
        for num, pos in enumerate(lst):
            if num >= caps[pos] and pos != len(lst) - 1:
                lst[pos] = 0
                lst[pos-1] = lst[pos-1] + 1
        #incremented_num = int(''.join(map(str, lst))) + 1
        #new_lst = [int(i) for i in str(incremented_num)]
        ## incrementing the number loses leading 0s
        #if len(new_lst) != len(lst):
        #    new_lst = [0]*(len(lst)-len(new_lst)) + new_lst
        #return new_lst
        return lst

    def get_word(digits, positions):
        """
        helper function to get the current word
        """
        string = ""
        #NOTE: digits and position arrays must match up
        for digit, position in zip(digits, positions):
            import ipdb;ipdb.set_trace()
            string += LETTER_MAP[int(digit)][int(position)]
        return string

    num_combos = 1
    for digit in digits:
        # how many possible words do we have?
        num_combos *= len(LETTER_MAP[int(digit)])
    for i in xrange(num_combos):
        words.append(get_word(digits, positions))
        positions = inc_lst(positions)


def main(calc_type, digits):
    """
    Given an input of digits, return all possible formed words

    NOTE::
        we do not perform check for number 0 or 1 which have no
        corresponding letters attached
        moreover, we do not check if the word belongs in the dictionary
        before appending it to the list that is returned
    """
    if calc_type == 'recursive':
        recur_wordify("", digits)
    elif calc_type == 'iterative':
        iter_wordify(digits)
    print words


if __name__=='__main__':
    """
    HOW TO USE::
        python lookout.py <recursive> <298>
    """
    import sys
    if len(sys.argv) > 2:
        calc_type = sys.argv[1]
        digits = sys.argv[2]
        main(calc_type, digits)
    else:
        print 'Example: python lookout.py <recursive> <298>'

