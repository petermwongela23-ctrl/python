students=["Alice","Bob","Charlie","Diana"]
for index,students in enumerate(students,start=1):
    print(f"{index}. {students}")


products=["Laptop","Mouse","Keyboard"]
prices=[1200,25,75]
for products,prices in zip(products,prices):
        print(f" the {products} price is  {prices}")


DivisibleBy3=[x for x in range(1,30) if x%3==0]
print(f" {DivisibleBy3} Are Divisibe by 3  ")



# keys=["id","username"]
# values=[101,"coder-pro"]
# my_dict={k:v for k,v in zip (keys,values)}
# print(my_dict)


keys = ["name", "role", "level"]
values = ["Alex", "Developer", "Senior"]
my_dict={k:v for k,v in  zip(keys,values)}
print(my_dict)


numbers=[1,2,3,4,5]
cube=lambda x: x**3
cubes=[cube(n) for n in numbers]
print(cubes)
