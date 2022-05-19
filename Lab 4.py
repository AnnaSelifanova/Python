class Hotel:

def __init__(self, num_rooms,s):
self._rooms = {'SGL': [[0 for _ in range(num_rooms[0])],s[0]],
'DBL':[[0 for _ in range(num_rooms[1])],s[1]],
'Junior Suite': [[0 for _ in range(num_rooms[2])],s[2]],
'Suite':[[0 for _ in range(num_rooms[3])],s[3]]}


def occypy(self, t, room_n):
if self._rooms[t][0][room_n]==0:
self._rooms[t][0][room_n] = 1 
else:
raise RuntimeError("Номер занят")

def free(self,t, room_n):
self._rooms[t][0][room_n] = 0 


def __str__(self):
a = "
for i in self._rooms:
for r in range(len(self._rooms[i][0])):
if self._rooms[i][0][r]==0:
a+='Номер '+ i+ " № " +str(r+1)+ " свободен\n"
else:
a+='Номер '+ i+ ' № ' +str(r+1)+ " занят\n"
return a


def all_occypy(self):
for i in self._rooms:
for r in range(len(self._rooms[i][0])):
self._rooms[i][0][r] = 1


def all_free(self):
for i in self._rooms:
for r in range(len(self._rooms[i][0])):
self._rooms[i][0][r] = 0


def occupy_rate(self):
summa=0
count=0
for i in self._rooms:
summa+=sum(self._rooms[i][0])
count+=len(self._rooms[i][0])*100
d=round(summa*100/count,2)
return f"{d} %"


def gain(self):
summa=0
for i in self._rooms:
summa+=sum(self._rooms[i][0])*self._rooms[i][1]
return f"Выручка {summa} у.е."

