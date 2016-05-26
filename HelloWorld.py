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
