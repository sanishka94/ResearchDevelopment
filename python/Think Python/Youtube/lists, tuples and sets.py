
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]

#Adding
#courses.append('Art')
#courses.extend(courses_2)
#courses.insert(0, 'Art')

#Removing
#courses.remove('Math')
#courses.pop()
popped = courses.pop(1)
print(popped)
print(courses)

#Sorting
#courses.reverse()
#courses.sort()
#nums.sort()
#courses.sort(reverse=True)
#nums.sort(reverse=True)
#sorted_courses = sorted(courses)
#print(sorted_courses)
#print(nums)

#Find
#print(courses.index('CompSci'))
#print('Art' in courses)

#print
#for index, course in enumerate(courses, start=1):
#	print(index, course)

#string - list
course_str = ', '.join(courses)
new_list = course_str.split(', ')
#print(course_str)
#print(new_list)