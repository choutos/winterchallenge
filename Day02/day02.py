#!/usr/bin/env python

input = [line.rstrip('\n') for line in open('input.txt')]


def count_occurrences(line):
    count=dict()
    for letter in line:
        if letter not in count.keys():
            count[letter] = 1
        else:
            count[letter] += 1
    return count

times_two = 0
times_three = 0
for line in input:
    result = count_occurrences(line)
    if 2 in result.values():
        times_two += 1
    if 3 in result.values():
        times_three += 1
print(times_two * times_three)
