   #name = input("What is your name? ")
       #print("Hello " + name)

#birth_year = input("What is your birth year? ")
#age = 2023 - int(birth_year)
#print(age)


#my first calculator code I wrote by myself!!!!!!


#first_number = input("First Number: ")
#second_number = input("Second Number: ")
#sum = float(first_number) + float(second_number)
#print("Sum: " + str(sum))

#another method:

#first_number = float(input("First Number: "))
#second_number = float(input("Second Number: "))
#sum = first_number + second_number
#print("Sum: " + str(sum))



#course = "Python for beginners"
#print(course.upper())


#course = "Python for beginners"
#print(course.find('y'))



#course = "Python for beginners"
#print(course.replace('for','4'))


#course = "Python for beginners"
#print("Python" in course)


#x = 10
#x = x + 3
#print(x)

#x = 10
#x += 3
#print(x)

#x = 10
#x *= 3
#print(x)


#x = 10
#x -= 3
#print(x)


#x = 10
#x %= 3
#print(x)


#x = 10
#x /= 3
#print(x)


#x = 10
#x //= 3
#print(x)

#x = (10+3)*2
#print(x)



#price = 10
#print(not price > 20) or (price < 30)

#temperature = 5
#if temperature > 30:
 #print("It's a sunny day")
 #print("Drink a lot of water")
#elif temperature > 20:
 #print("It's a nice day")
#elif temperature > 10:
 #print("It's a cold day")
#else:
 #print("it's cold.")
#print("Done")


### my attempt on the exercise
#weight = input("Weight: ")
#pounds = 0.453592
#kilogram = 2.2046
#measure = input(float("(K)g or (L)g: "))
#if measure == kilogram:
  #  print("Weight in Kg: " (weight * kilogram))
#else:
 #   print("Weight is Lbs: " (weight * pounds))


#mosh's solution


#weight = int(input("Weight: "))
#unit = input("(K)g or (L)bs: ")
#if unit.upper() == "K":
#    converted = (weight / 0.45)
 #   print("Weight in Kg: " + str(converted))
#else:
 #   converted = (weight * 0.45)
  #  print("Weight in Lbs: " + str(converted))




#while loops:
#i = 1
#while i <= 1000:
 #   print(i)
  #  i = i + 1





#i = 1
#while i <= 1000:
    #print(i * "*")
    #i = i + 1



#list:

#names = ["John","Bob","Mosh","Sam","Mary"]
#names[0] = "Jon"
#print(names[0:3])
#print(names)


#list methods:


#numbers = [1,2,3,4,5]
#numbers.append(6)
#print(numbers)




#numbers = [1,2,3,4,5]
#numbers.insert(0, -1)
#print(numbers)


#numbers = [1,2,3,4,5]
#numbers.remove(3)
#print(numbers)



# numbers = [1,2,3,4,5]
#numbers.clear()
#print(numbers)


#checking if 1 is in the list:


#numbers = [1,2,3,4,5]
#print(1 in numbers)


#numbers = [1,2,3,4,5]
#print(10 in numbers)

#to check the number of items in a list:
#numbers = [1,2,3,4,5]
#print(len(numbers))


#to print list in seperate lines using for loop:

#numbers = [1,2,3,4,5]
#for item in numbers:
 #   print(item)

#printing lists in seperate line using while loop:
#numbers = [1,2,3,4,5]
#i = 0
#while i < len(numbers):
 #   print(numbers[i])
  #  i = i+1


#range fuction:

#numbers = range(5)
#for number in numbers:
 #   print(number)

#giving two values in range will start from the first number but will conclude one number before the second value
#umbers = range(5, 10)
#or number in numbers:
  # print(number)

#giving a three values will make the third value to be a as step that is if 2 is the third value then the output will be 2 step above like 5,7,9:



#umbers = range(5, 10, 2)
#or number in numbers:
 #  print(number)
