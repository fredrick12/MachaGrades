science_grades = [50, 40, 30, 14, 90, 100, 100, 100, 80]
science_avg = 0
for g in science_grades:
  science_avg += g
science_avg /= len(science_grades)
print("Frederick's science average is: %.2f" % science_avg)

math_grades = [100, 100, 100, 14, 90, 100, 100, 100, 80]
math_avg = 0
for g in math_grades:
  math_avg += g
math_avg /= len(math_grades)
print("Frederick's math average is: %.2f" % math_avg)

