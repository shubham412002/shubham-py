
i = 1
while i <= 4:
    print(i,"Shubh")
    i += 1

print('----------')

# while in reverse  
c  = 5
while i >= 1:
    print(i,"Shubh")
    i -= 1

print('----------')

# nested while
i = 1

while i <= 4:
    print(i,"Shubh ",end="")
    j = 1
    while j <= 4:
        print('rocks ',end="")
        j += 1
    i += 1
    print()
