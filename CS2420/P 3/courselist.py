"""
this file contains the class for making the courselist
using a linked list structure
"""


class CourseList:
    """
    this is a docstring
    """
    def __init__(self):
        """
        this is a docstring
        """
        self.head = None
        self.current = None


    def insert(self, new_course):
        """
        this is a docstring
        """
        if self.head is None:  
            self.head = new_course
        elif new_course.course_number < self.head.course_number:
            new_course.next = self.head
            self.head = new_course
        else:
            current = self.head
            while current.next:
                if new_course.course_number > current.next.course_number:
                    current = current.next
                else:
                    new_course.next = current.next
                    current.next = new_course
                    break
            current.next = new_course
    

    def remove(self,number):
        """
        this is a docstring
        """
        if self.head.course_number == number:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.course_number == number:
                    current.next = current.next.next
                    break
                current = current.next


    def remove_all(self,number):
        """
        this is a docstring
        """
        while self.find(number) != -1:
            self.remove(number)


    def find(self,number):
        """
        this is a docstring
        """
        current = self.head
        while current:
            if current.course_number == number:
                return current
            current = current.next
        return -1


    def size(self):
        """
        this is a docstring
        """
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size


    def calculate_gpa(self):
        """
        this is a docstring
        """
        if self.head is None:
            return 0.0
        current = self.head
        grades = 0.0
        hrs = 0.0
        while current:
            grades += current.course_grade * current.course_credit_hr
            hrs += current.course_credit_hr
            current = current.next
        return grades/hrs


    def is_sorted(self):
        """
        this is a docstring
        """
        course_numbers = []
        current = self.head
        while current:
            course_numbers.append(current.course_number)
            current = current.next
        if course_numbers == sorted(course_numbers):
            return True
        return False


    def __str__(self):
        """
        this is a docstring
        """
        current = self.head
        string = ""
        while current:
            string += (f"cs{current.course_number} {current.course_name}:{current.course_grade} Credit Hours: {current.course_credit_hr}\n")
            current = current.next
        return string


    def __iter__(self):
        """
        this is a docstring
        """
        return self


    def __next__(self):
        """
        this is a docstring
        """
        if self.current is None:
            if self.head is None:
                raise StopIteration
            else:
                self.current = self.head
            return self.head
        elif self.current.next is None:
            self.current = None
            raise StopIteration
        else:
            self.current = self.current.next
            return self.current