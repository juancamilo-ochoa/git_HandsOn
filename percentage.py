s = input()
t = s.upper()

print(s.count("C"))
print(s.count("A"))
print(s.count("G"))
print(s.count("T"))


print("The percentage of C is")
print(100*t.count("C")/len(t))
print("The percentage of A is")
print(100*t.count("A")/len(t))
print("The percentage of G is")
print(100*t.count("G")/len(t))
print("The percentage of T is")
print(100*t.count("T")/len(t))
