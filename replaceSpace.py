#!/usr/bin/python

def replaceSpace(string):
  new_string = ''
  for char in string:
    if char == ' ':
      new_string = new_string + '%20'
    else:
      new_string = new_string + char
  return new_string

