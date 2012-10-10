#!/usr/bin/python

def isUniqueString(string):
  ascii_list = [False]*256

  for char in string:
    val = ord(char)
    if ascii_list[val]:
      return False
    ascii_list[val] = True
  return True

