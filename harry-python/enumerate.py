l = [1,45,57,135,6]

ind = 0
for item in l:
    print(f"item num at index {ind} is {item}")
    ind += 1

print('using enumerate')
# using enumerate
for ind,item in enumerate(l):
    print(f"item num at index {ind} is {item}")