import abc

class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class IntroToPython:
    def lesson(self):
        return f"""
            Hello {self.student}. define two variables,
            an integer named a with value 1
            and a string named b with value 'hello'
        """
    def check(self, code):
        return code == "a = 1\nb = 'hello'"


class Statistics(Assignment):
    def lesson(self):
        return (
            "Good work so far, "
            + self.student
            + ". Now calculate the average of the numbers "
            + " 1, 5, 18, -3 and assign to a variable named 'avg'"
        )
    def check(self, code):
        import statistics
        code = "import statistics\n" + code
        local_vars = {}
        global_vars = {}
        exec(code, global_vars, local_vars)
        return local_vars.get("avg") == statistics.mean([1, 5, 18, -3])


class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0
    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1
        return result
    def lesson(self):
        return self.assignment.lesson()


import uuid
class Grader:
    
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}
    
    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the right methods"
            )
        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id