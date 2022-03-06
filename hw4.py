#6
import math
def my_log(lst: list) -> list:
   return[math.log(x) if x > 0 else None for x in lst]
print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))

#17
import statistics
lst = [2,3,-21,-4,44,6,100,5]
maxim = lst.index(max(lst))
minim = lst.index(min(lst))
if minim < maxim:
    print(statistics.mean(lst[minim+1:maxim]))
else:
    print(statistics.median([max(lst),min(lst)]))

#19
import statistics
l = [1, 5, 6.3, 6, None, 2.0, -4, None]
l_new = [0 if x == None else x for x in l]
print([statistics.mean(l_new) if x == None else x for x in l])

#11
text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
text_new = text.split()
for x in text_new:
    if len(x) <= 3:
        text_new.remove(x)
print(text_new)
