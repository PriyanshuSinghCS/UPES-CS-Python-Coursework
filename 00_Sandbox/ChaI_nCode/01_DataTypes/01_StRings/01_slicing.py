num_list = "0123456789"
a = num_list[:]
print(a)  # 0123456789

b = num_list[3:]
print(b)  # 3456789

c = num_list[:7]  
print(c)  # 0123456

d = num_list[0:7:2]  # hopping of 2 means skips a number
print(d)  #0246