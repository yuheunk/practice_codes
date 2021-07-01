a, b = map(int, input().split())

sangsoo_a = int(str(a)[::-1])
sangsoo_b = int(str(b)[::-1])
if sangsoo_a > sangsoo_b:
    print(sangsoo_a)
else:
    print(sangsoo_b)