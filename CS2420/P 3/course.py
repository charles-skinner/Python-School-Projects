"""
this file contains the course class
"""
class Course:
    """
    this is a docstring
    """
    def __init__(self,number = 0,name = "",credit_hr = 0.0,grade = 0.0):
        test1 = isinstance(number,int) and number>=0
        test2 = isinstance(name,str)
        test3 = isinstance(credit_hr,float) and credit_hr>=0.0
        test4 = isinstance(grade,float) and grade>=0.0
        if(test1 and test2 and test3 and test4):
            self.course_number = number
            self.course_name = name
            self.course_credit_hr = credit_hr
            self.course_grade = grade
            self.next = None
        else:
            raise ValueError


    def number(self):
        """
        this is a docstring
        """
        return self.course_number


    def name(self):
        """
        this is a docstring
        """
        return self.course_name


    def credit_hr(self):
        """
        this is a docstring
        """
        return self.course_credit_hr


    def grade(self):
        """
        this is a docstring
        """
        return self.course_grade
    

    def __str__(self):
        """
        this is a docstring
        """
        return f"cs{self.course_number} {self.course_name}:{self.course_grade} Credit Hours: {self.course_credit_hr}"