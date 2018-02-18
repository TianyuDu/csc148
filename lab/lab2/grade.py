class GradeEntry():
	'''
	'''
	course_code: str
	grade: str
	weight: float

	NUM_TO_GP: dict
	LET_TO_GP: dict

	NUM_TO_GP = {
			range(90, 100+1): 4.0,
			range(85, 89+1): 4.0,
			range(80, 84+1): 3.7,
			range(77, 79+1): 3.3,
			range(73, 76+1): 3.0,
			range(70, 72+1): 2.7,
			range(67, 69+1): 2.3,
			range(63, 66+1): 2.0,
			range(60, 62+1): 1.7,
			range(57, 59+1): 1.3,
			range(53, 56+1): 1.0,
			range(50, 52+1): 0.7,
			range(0, 49+1): 0.0
			}

	LET_TO_GP = {
			'A+': 4.0,	
			'A': 4.0,
			'A-': 3.7,
			'B+': 3.3,
			'B': 3.0,
			'B-': 2.7,
			'C+': 2.3,
			'C': 2.0,
			'C-': 1.7,
			'D+': 1.3,
			'D': 1.0,
			'D-': 0.7,
			'F': 0.0
			}

	def __init__(self, course_code: str, grade: str, weight: float):
		self.course_code = course_code
		assert grade in self.LET_TO_GP.keys() or int(grade) in range(101)
		self.grade = grade.upper()
		assert weight in [1.0, 2.0]
		self.weight = weight

	def __eq__(self, other):
		return (
			type(self) == type(other),
			self.grade == other.grade,
			self.course_code == other.course_code.
			self.weight == other.weight
			)
	
	def __str__(self):
		raise NotImplementedError("Subclass needed.")

	def convert_to_gp(self):
		raise NotImplementedError("Subclass needed.")

	def __convert(self):
		try:
			num_grade = int(self.grade)
			for key in self.NUM_TO_GP.keys():
				if num_grade in key:
					return self.NUM_TO_GP[key]
		except ValueError:
			return self.LET_TO_GP[self.grade]

	def __setattr__(self, name, value):
		self.__invarient()
		self.__dict__[name] = value

	def __invarient(self):
		if 'grade' in self.__dict__.keys():
			assert grade in self.LET_TO_GP.keys() or int(grade) in range(101)
		if 'weight' in self.__dict__.keys():
			assert weight in [1.0, 2.0]


class NumericGradeEntry(GradeEntry):
	def convert_to_gp(self) -> int:
		return GradeEntry.__convert(self)

	def __str__(self) -> str:
		return "The course code is: {0},\
		 the numeric grade for this course is {1},\
		 the corresponding grade point is {2}".format(
		 											self.course_code,
		 											self.grade,
		 											self.convert_to_gp()
		 											)

class LetterGradeEntry(GradeEntry):

	def convert_to_gp(self):
		return GradeEntry.__convert(self)

	def __str__(self) -> str:
		return "The course code is: {0},\
		 the numeric grade for this course is {1},\
		 the corresponding grade point is {2}".format(
		 											self.course_code,
		 											self.grade,
		 											self.convert_to_gp()
		 											)
# ========= Exec. =========
if __name__ == '__main__':
	'''
	ge = GradeEntry('CSC108', '84', 1.0)
	nge = NumericGradeEntry('CSC148', '80', 1.0)
	nge.convert_to_gp()'''
# ========= Draft =========







	