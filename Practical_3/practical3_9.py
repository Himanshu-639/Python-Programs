#Que.9:

t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
half_length = len(t1)//2
print("First half : ", t1[:half_length])
print("second half : ", t1[half_length :])

even_num=tuple(filter(lambda x: x%2==0, t1))
print("The tuple of Even numbers is : ", even_num)

t2=(11, 13, 15)
concatenated_tuple = t1+t2
print("The concatenated tuple is : ", concatenated_tuple)

max_val= max(concatenated_tuple)
min_val= min(concatenated_tuple)
print("The maximum value is : ", max_val)
print("The minimum value is : ", min_val)