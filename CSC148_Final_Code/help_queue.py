from typing import List, Dict

class HelpQueueEntry:
    """
    A simple class to represent one entry in  the help queue  
    """

    def __init__ (self, name: str, number: int, course=''):
        """ Create this new HelpQueueEntry representing a student name, the queue position number, and an optional course.

        @param self   : this help queue entry
        @param name   : the name of the student
        @param number : the position in the queue
        @param course : the course to get help with
        """
        self.name, self.number, self.course = name, number, course

class HelpQueue:
    # Your implementation

    def __init__(self):
        self.queue = list()
        self.num = 0

    def process_swipe(self, name: str, course: str=''):
        for q in self.queue:
            if q.name == name:
                return q.number
        new = HelpQueueEntry(name, self.num, course)
        self.num += 1
        self.queue.append(new)

    def get_next_student(self, course: str=''): 
        for q in self.queue:
            if q.course = 


if __name__ == '__main__':
    hq = HelpQueue()
    assert hq.process_swipe('Amy', 'CSC108') == 0
    assert hq.process_swipe('Bo') == 1
    assert hq.process_swipe('Chen', 'CSC148') == 2
    assert hq.process_swipe('Amy') == 0
    assert hq.get_next_student('CSC148').number == 2
    assert hq.get_next_student('CSC148') is None
    assert hq.get_next_student('CSC165') is None
    assert hq.get_next_student().number == 0
    assert hq.get_next_student().number == 1
    assert hq.get_next_student() is None
    assert hq.get_next_student() is None
