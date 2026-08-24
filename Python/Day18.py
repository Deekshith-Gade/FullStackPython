# def simple_generator():
#     print("Start")
#     yield 1
#     yield 2
#     yield 3
# print("End")

# gen = simple_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen)) 
# print(next(gen))

squares = [x * x for x in range(6)]
print(squares)


numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)

names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)


products = ["laptop", "phone", "tablet", "monitor"]
upper_products = [p.upper() for p in products]
print(upper_products)

prices = [1000, 800, 450, 300]
discounted = [price * 0.9 for price in prices]
print(discounted)


in_stock = [True, False, True, False]
available = [i for i, stock in enumerate(in_stock) if stock]
print(available)


product_info = [("Laptop", 1000), ("Phone", 800), ("Tablet",
450)]
expensive = [name for name, price in product_info if price >
700]
print(expensive)