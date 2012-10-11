#!/usr/bin/python

def main():
    """
    File Events

    Output recorded actions into user friendly notifications
    """
    events = []
    actions = input("How many lines of events? ")
    for i in xrange(actions):
        try:
            act, f, iden = raw_input("Action %s: " % (int(i)+1)).split()
            events.append((act, f, iden))
        except ValueError, e:
            print 'Error has occured ->', e
    events.sort(key=lambda x:x[-1]) # reorder by unique identifier
    print events


if __name__=='__main__':
    main()

