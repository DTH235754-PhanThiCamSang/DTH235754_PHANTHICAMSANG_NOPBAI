#oscillate
def oscillate(start, stop):
    for i in range(start, stop):
        if i == 0:
            yield 0
            yield 0
        else:
            yield i
            yield -i

# Kiểm tra kết quả
for n in oscillate(-3, 5):
    print(n, end=' ')
print()