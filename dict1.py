dict={
    23:"sonu",45:"lalit","sonu":56
}
dict2={
    21:"aj",56:"ffo",23:"sonu",45:"lal"
}
print(dict.keys())
print(dict.values())
print(dict)
dict.update(dict2)
print(dict)
for i in dict:
    print(i)
    