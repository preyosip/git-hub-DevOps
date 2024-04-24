def my_map(my_func , my_item):
   result = []
   for item in my_item:
      new_item = my_func(item)
      result.append(my_item)
   return result 
num = [2,3,4,5,6,7]

cubed = my_map(lambda x : x**3 , num)
print(cubed)
