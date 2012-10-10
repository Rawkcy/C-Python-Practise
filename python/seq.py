#!/usr/bin/python
"""
             1
            11
            21
          1211
        111221
        312211
      13112221
    1113213211
31131211131221
"""

def print_seq(seq):
    print seq

    # figure out the next entry
    prev_char = seq[0]
    count = 0
    new_seq = ''
    for char, index in enumerate(seq):
        if char == prev_char:
            count += 1
        else:
            new_seq += '%s%s' % (str(count), str(char))
            count = 0
            prev_char = char

    print_seq(seq)

if __name__=="__main__":
    print_seq(1)

