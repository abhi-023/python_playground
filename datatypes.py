a = 5
print("type of a:",type(a))
b = 2.3
print("type of b:",type(b))
c = 2 + 3j
print("type of c:",type(c))
string = "hey abhi"
print(string)
print(string[4])
List = []
List.append(1)
print(List)
List.append(2)
List.append(22)
List.insert(3,23)
List.insert(0,"abhi")
print(List)
List.remove(23)
print(List)
List.pop()
print(List)
Tuple1 = ()
print(Tuple1)
print(('abhi', 'ram'))
Tuple2 = ('raj', 'm')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)
print(Tuple3[-1])
print(type(True))
print(1>23)
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
set1.remove(5)
set1.remove(6)
print(set1)
set1.discard(8)
set1.discard(9)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
Dict = {}
Dict = {1: 'hey', 2: 'abhi', 3: 'hwru'}
print(Dict)
Dict = {5: 'anakk', 6: 'ammsaa', 7: 'xax',
        'A': {1: 'Gexas', 2: 'axor', 3: 'Gecaks'},
        }
Dict.pop(5)
print(Dict)
Dict.popitem()
print(Dict)