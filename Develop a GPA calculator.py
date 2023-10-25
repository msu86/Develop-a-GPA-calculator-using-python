#Import math library
bangla = int(input("Enter Mark For Bangla- "))
english = int(input("Enter Mark For English- "))
mathematics = int(input("Enter Mark For Math- "))
science = int(input("Enter Mark For Science- "))
import math
total_mark = bangla + english + mathematics + science
print("Total mark - ", total_mark)
avg_mark = math.ceil(total_mark / 4)
print("Average - ", avg_mark)

if avg_mark >= 91 and avg_mark <= 100:
    print("Grade - A+")
elif avg_mark >= 81 and avg_mark <= 90:
    print("Grade - A")
elif avg_mark >= 71 and avg_mark <= 80:
    print("Grade - B")
elif avg_mark >= 61 and avg_mark <= 70:
    print("Grade - C")
elif avg_mark >= 41 and avg_mark <= 60:
    print("Grade - D")
else:
    print("Grade - F")
