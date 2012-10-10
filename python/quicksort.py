#!/usr/bin/env python

def quicksort(array, first, last):
  beginning = first
  end = last
  pivot = array[end]
  last -= 1

  while first < last:
    while array[first] <= pivot and first < end:
      first += 1
    while array[last] >= pivot and beginning < last:
      last -= 1

    tmp = array[first]
    array[first] = array[last]
    array[last] = tmp

  array[end] = array[last]
  array[last] = pivot

  quicksort(array, 0, last)
  quicksort(array, first, end)

