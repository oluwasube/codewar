'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
'''

def find_outlier(my_list):
    odd_int = []
    even_int = []
    for num in my_list:
        if num % 2 != 0:
            odd_int.append(num)
        if num % 2 == 0:
            even_int.append(num)
            
    if len(even_int) > len(odd_int):
        return odd_int[0]
    else:
        return even_int[0]
  

check = [2, 4, 0, 100, 4, 11, 2602, 36]
new_list = find_outlier(check)
print(new_list)

