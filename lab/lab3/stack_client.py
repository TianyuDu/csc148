from stack import *

def list_stack(list: list, stack: "Stack"):
	for item in list:
		stack.add(item)
	while not stack.is_empty():
		obj = stack.remove()
		if type(obj) == list:
			for item in obj:
				stack.add(item)
		else:
			print(obj)

if __name__ == "__main__":
	stack = Stack()
	str_received = str()
	while not str_received == "end":
		str_received = input(
			"String to be added to stack (type 'end' to terminate): "
			)
		stack.add(str_received)
	while not stack.is_empty():
		print(stack.remove())
