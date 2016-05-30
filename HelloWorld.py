__author__ = 'Administrator'
print("Hello World!")
string = "python"
print(string)
print(100 + 200)
print("""line1
line2
line3""")
print(True)
print(3 > 2)
print(True and False)
print(True or False)
v = 123
print(v)
v = "abc"
print(v)
print("Hi,%s,you have $%d" % ("yy", 1000))
classmates = ["yy", "cy", "ly"]
print(classmates)
print(len(classmates))
print(classmates[1])
print(classmates[-2])
classmates.append("yyp")
print(classmates)
classmates.insert(0, "zwq")
print(classmates)
classmates.pop()
print(classmates)
list1 = ["ABC", 100, True]
list2 = ["python", list1]
print(list1)
print(list2)
list3 = []
print(len(list3))
tuple1 = ("ABC", 100, True)
print(tuple1)
print(tuple1[0])
tuple2 = ()
print(tuple2)
tuple3 = (1,)
print(tuple3)
age = 18
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
for classmate in classmates:
    print(classmate)
print(list(range(10)))
s = 0
for x in range(101):
    s += x
print(s)

s = 0
n = 100
while n > 0:
    s += n
    n -= 1
print(s)
dic = {"A": 95, "B": 75, "C": 85}
print(dic["A"])
dic["D"] = 60
dic["E"] = 100
print(dic)
print("A" in dic)
print(dic.get("A"))
dic.pop("D")
print(dic)
s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
s.remove(2)
print(s)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(3))
print(my_abs(-3))
