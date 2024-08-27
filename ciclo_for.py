def generador():
   number = 0
   while True:
    number+= 1
    yield number
           

a = generador()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
