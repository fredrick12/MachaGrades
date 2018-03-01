science_grades = [50, 40, 30, 14, 90, 100, 100, 100, 80]
science_avg = 0
for g in science_grades:
  science_avg += g
science_avg /= len(science_grades)
print("Frederick's science average is: %.2f" % science_avg)
