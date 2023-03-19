number = int(input("ввести число: "))

num_1= number % 10
num_2 = (number // 10) % 10
num_3 = (number // 100) % 10
num_4 = (number // 1000) % 10


reversed_number = num_1 * 1000 + num_2 * 100 + num_3 * 10 + num_4
print ("результат:", reversed_number)
