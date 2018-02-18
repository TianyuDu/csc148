if __name__ == '__main__':
	grades = [NumericGradeEntry('csc148', '87', 1.0),
	NumericGradeEntry('mat137', '76', 2.0),
	LetterGradeEntry('his450', 'B+', 1.0)]
	for g in grades:
	# Use appropriate ??? methods or attributes of g in format
		print("Weight: {}, grade: {}, points: {}".format(g.weight, g.grade, g.convert_to_gp()))
	# Use methods or attributes of g to compute weight times points
	total = sum( # sum of the list of...
	[g.weight * g.convert_to_gp() # methods or attributes of g
	for g in grades]) # using each g in grades
	# sum up the credits
	total_weight = sum([g.weight for g in grades])
	print("GPA = {}".format(total / total_weight))