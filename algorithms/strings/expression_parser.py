from abc import ABC, abstractmethod
				
class Node(ABC):
		def __init__(self, value):
				self.value = value

		@abstractmethod
		def evaluate(self):
				pass

		@staticmethod
		def parse_string_type(str):
			counter = 0
			str = str.strip()
			print(str)
			for ch in str:
				if ch == '(':
					counter += 1
				elif ch == ')':
					counter -= 1
				elif ch in '+-*/' and counter == 0:
					return CompositeExpression(str)
	
			if str[0] == '(':
				return Expression(str)
			else:
				return Literal(str)
		
		
		
class Literal(Node):
		def evaluate(self):
				return float(self.value)

class Expression(Node):
		def evaluate(self):
				return self.parse_string_type(self.value[1:-1]).evaluate()

class CompositeExpression(Node):
		def evaluate(self):
			idx = self.value.find('+')
			if idx != -1:
				return self.parse_string_type(self.value[0:idx]).evaluate() + self.parse_string_type(self.value[idx + 1:]).evaluate()
			idx = self.value.find('-')
			if idx != -1:
				return self.parse_string_type(self.value[0:idx]).evaluate() - self.parse_string_type(self.value[idx + 1:]).evaluate()
			idx = self.value.find('*')
			if idx != -1:
				return self.parse_string_type(self.value[0:idx]).evaluate() * self.parse_string_type(self.value[idx + 1:]).evaluate()
			idx = self.value.find('/')
			if idx != -1:
				return self.parse_string_type(self.value[0:idx]).evaluate() / self.parse_string_type(self.value[idx + 1:]).evaluate()

str = '3 + 2'
print(Node.parse_string_type(str).evaluate())
print(Node.parse_string_type('3 + 8 + (12 / 3)').evaluate())
print(Node.parse_string_type('(58)').evaluate())
