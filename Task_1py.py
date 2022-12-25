x = input('text from latters or  simple positive numbers')
if x.isdigit() == False:
    print(f'{x}-word with{len(x)}letters')
elif int(x) % 2 == 0:
    print(str(x) + 'is even number')
else:
    print(str(x) + 'is odd number')
