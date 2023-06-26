#Decimal to Binary
print("Decimal to binary converter")
decimal = None
while decimal != int:
    try:
        decimal = int(input("Decimal:"))
    except:
        continue
    else:
        break
d = decimal
r = int(d%2)
q = int(d/2)
binrev = [r]
while d != 1:
        d = int(d/2)
        r = int(d%2)
        binrev.append(r)
binrev.reverse()
binary = ""
for i in binrev:
    binary = binary +str(i)

print ("Binary:",binary)