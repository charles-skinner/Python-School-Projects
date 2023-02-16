from course import Course
from courselist import CourseList
"""
this is main
"""

def main():
    """
    this is a docstring
    """
    f = open("data.txt","r")
    content = f.readlines()
    cl = CourseList()
    for line in content:
        line = line.strip("\n").split(",")
        cl.insert(Course(int(line[0]),line[1],float(line[2]),float(line[3])))

    print(f"Current List({cl.size()})")
    print(cl)
    print(2*"\n")
    print(f"Cumulative GPA: {round(cl.calculate_gpa(),3)}")
    print("\n")


if __name__ == "__main__":
    main()