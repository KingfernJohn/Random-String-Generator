import string, random
print()
length = int(input("Length >>>  "))
rows = int(input("Rows >>>  "))
data = open("output.txt","w+")
for i in range(rows):
    def id_generator(chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))
    data.write(id_generator())
    data.write("\n")
data.close()
print("\nSaved as 'output.txt'\n\n")
quit()