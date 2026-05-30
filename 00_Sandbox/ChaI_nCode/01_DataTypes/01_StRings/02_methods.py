chai = "Masala Chai"
print(chai.lower())
print(chai.upper())
print(chai)  # String is immutable

chai1 = "    Masala Chai   "
print(chai1)
print(chai.strip())  # will remove space from start and end of the string


chai_2 = "Lemon Chai"
print(chai_2)
print(chai_2.replace("Lemon","Ginger"))

chai_3 = 'Lemon, Ginger, Mint'
print(chai_3)
print(chai_3.split())
print(chai_3.split(", "))

chai_4 = "Masala Chai"
print(chai_4.find("Chai"))  # tells from which position we get Chai

chai_5 = "Masala Chai Chai Chai"
print(chai_5.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I orderd {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))