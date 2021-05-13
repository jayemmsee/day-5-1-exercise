# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
counter = 0
for h in student_heights:
 counter += h
 #print(f"The total height of the students is {counter}")

 number_of_heights = 0
 for n in student_heights:
   number_of_heights += 1
   #print(f"The number of heights collected is {number_of_heights}")

average_height = counter / number_of_heights
print(average_height)
  


