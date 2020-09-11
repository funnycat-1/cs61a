# print numeric expressions
print(2020)
print(2000 + 20)

# functions
print(abs(-2))

# print strings
print("Go Bears")

# dealing with file object
shakes = open('shakespeare.txt')
text = shakes.read().split()
print(len(text))
print(text[:25])
print(text.count('the'))
print(text.count('ha'))
print(text.count('we'))
print(text.count(','))

# dealing with sets
words = set(text)
print(len(words))

# dealing with combinations
print('draw'[0])
print({w[0] for w in words})

# dealing with data
print('draw'[::-1]) # reverse string
print({w for w in words if w == w[::-1] and len(w) > 4})
print({w for w in words if w[::-1] in words and len(w) == 4})
print({w for w in words if w[::-1] in words and len(w) > 6})
