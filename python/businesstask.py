#!/usr/bin/python

class BusinessTasks(object):
    def getTask(self, todo, n):
        """
        Given list of tasks, return the task which the businessman chooses to execute
        """
        pos = n - 1
        del todo[pos]
        while(len(todo) > 1):
            pos = (pos + n) % len(todo)
            del todo[pos]
        return todo[0]

if __name__=='__main__':
    business = BusinessTasks()
    print business.getTask(['a','b','c','d'], 2)

