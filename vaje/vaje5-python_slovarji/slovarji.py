from pomozne import ps


sl = {1: "tvoja mama", 2: "adafg"}
sl.get(1)

print("---items---")
[print(item) for item in sl.items()]
print("---keys---")
[print(item) for item in sl.keys()]
print("---values---")
[print(item) for item in sl.values()]

sl[420] = "zaza"
print("---dodal zaza---")
[print(item) for item in sl.items()]

sl.pop(1)
print("---odstranil key 1---")
[print(item) for item in sl.items()]

sl.pop(2)
print("---odstranil key 2---")
[print(item) for item in sl.items()]

print("---nov slovarcek---")
sa = {x: x*x for x in range(5)}
ps(sa)