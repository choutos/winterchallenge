#!/usr/bin/env python

#with open('input.txt') as f:
#    lines = f.readlines()

lines = [line.rstrip('\n') for line in open('input.txt')]



def frequency_adjuster(lines):
    count = 0
    freq = [0]
    #first_repeated = 0
    while True:
        for change in lines:
            if change[0]=='+':
                count += int(change[1:])
                if count in freq:
                    return count
                else:
                    freq.append(count)
            else:
                count -= int(change[1:])
                
                if count in freq:
                    return count
                else:
                    freq.append(count)
    return (freq)



print(frequency_adjuster(lines))