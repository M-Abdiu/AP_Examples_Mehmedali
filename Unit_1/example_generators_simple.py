def square_counter(max):
    count = 1
    while count <= max:
        yield count ** 2
        count += 1

# test with
ctr = square_counter(5)
for n in ctr:
    print(n)

ctr2 = square_counter(4)
# or use next()
print(next(ctr2))
print(next(ctr2))
