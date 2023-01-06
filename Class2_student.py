class Student(object):

    """This class represents a student"""

    def __init__(self, name, number):      # ('Kevin', 5)
        self.name = name

        self.scores = []

        for i in number:                    # kevin - [0, 0, 0, 0, 0]
            self.scores.append(0)

    def getName(self):
        """This method return name of studnet"""

        return self.name

    def getScores(self):
        return self.scores

    def getScore(self, index):

        return self.scores[index-1]

    def setScore(self, index, score):

        self.scores[index-1] = score # this will set score

    def setScores(self, scores):

        self.scores = scores

    

    
