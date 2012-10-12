#!/usr/bin/python

## {{{ http://code.activestate.com/recipes/252178/ (r1)
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]
## end of http://code.activestate.com/recipes/252178/ }}}


if __name__=='__main__':
    for perm in all_perms('abc'):
        print perm

