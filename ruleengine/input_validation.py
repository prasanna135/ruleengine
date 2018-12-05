import sys
from datetime import datetime


class ValidateInput(object):
	def __init__(self, signal_dict):
		self.signal = signal_dict.get("signal", None)
		self.value = signal_dict.get("value", None)
		self.date_keywords = ["past", "future", "today"]

	def validate_more(self, *args):
		print "pass"
	
	def validate_less(self, *args):
		print "less"

	def validate_equal(self, *args):
		print "equal"

	def validate_between(self, *args):
		print "between"

class ValidateIntInput(ValidateInput):
	def validate_more(self, *args):
		lower_bound = args[0][0]
		negation = args[1]
		if not (isinstance(lower_bound, int) or isinstance(lower_bound, float)):
			return
		if negation:
			if float(self.value) <= lower_bound:
				return self.signal
		else:
			if float(self.value) > lower_bound:
				return self.signal
		
	def validate_less(self, *args):
		upper_bound = args[0][0]
		negation = args[1]

		if not (isinstance(upper_bound, int) or isinstance(upper_bound, float)):
			return
		if negation:
			if float(self.value) >= upper_bound:
				return self.signal
		else:
			if float(self.value) < upper_bound:
				return self.signal

	def validate_equal(self, *args):
		equal_value = args[0][0]
		negation = args[1]

		if not (isinstance(equal_value, int) or isinstance(equal_value, float)):
			return
		if negation:
			if float(self.value) != equal_value:
				return self.signal
		else:
			if float(self.value) == equal_value:
				return self.signal

	def validate_between(self, *args):
		lower_bound = args[0][0]
		upper_bound = args[0][1]
		negation = args[1]

		if not (isinstance(upper_bound, int) or isinstance(upper_bound, float)):
			return
		if not (isinstance(lower_bound, int) or isinstance(lower_bound, float)):
			return
		if negation:
			if float(self.value) >= upper_bound and float(self.value) <= lower_bound:
				return self.signal
		else:
			if float(self.value) < upper_bound and float(self.value) > lower_bound:
				return self.signal

class ValidateStrInput(ValidateInput):
	def validate_equal(self, *args):
		equal_value = args[0][0]
		negation = args[1]
		str_values = ["high", "low"]

		if not (isinstance(equal_value, str) or isinstance(equal_value, str)):
			return
		if negation:
			if (self.value.lower() != equal_value.lower() and equal_value.lower() in str_values):
				return self.signal
		else:
			if self.value.lower() == equal_value.lower():
				return self.signal

	def validate_between(self, *args):
		pass

class ValidateDateInput(ValidateInput):
	def validate_more(self, *args):
		lower_bound = args[0][0]
		negation = args[1]
		date_value = datetime.strptime(self.value, "%Y-%m-%d %H:%M:%S")
		if not (isinstance(lower_bound, datetime) or lower_bound in self.date_keywords):
			print "define the rule with proper values"
			return
		if lower_bound in ["past", "future"]:
			print "ambiguous rule."
			return
		if isinstance(lower_bound, datetime):
			if negation:
				if date_value <= lower_bound:
					return self.signal
			else:
				if date_value > lower_bound:
					return self.signal
		elif lower_bound in ["today"]:
			today = datetime.today()
			if negation:
				if date_value <= today: return self.value
			else:
				if date_value > today: return self.value

	def validate_less(self, *args):
		upper_bound = args[0][0]
		negation = args[1]
		date_value = datetime.strptime(self.value, "%Y-%m-%d %H:%M:%S")
		if not (isinstance(upper_bound, datetime) or upper_bound in self.date_keywords):
			print "define the rule with proper values"
			return
		if upper_bound in ["past", "future"]:
			print "ambiguous rule."
			return
		if isinstance(upper_bound, datetime):
			if negation:
				if date_value >= upper_bound:
					return self.signal
			else:
				if date_value < upper_bound:
					return self.signal
		elif upper_bound in ["today"]:
			today = datetime.today()
			if negation:
				if date_value >= today: return self.value
			else:
				if date_value < today: return self.value		

	def validate_equal(self, *args):
		date_value = datetime.strptime(self.value, "%Y-%m-%d %H:%M:%S")
		today = datetime.today()
		date = args[0][0]
		negation = args[1]
		if negation:
			if date.lower() == "future":
				if date_value < today:
					return self.signal
			elif date.lower() == "past":
				if date_value > today:
					return self.signal
			elif date.lower() == "today":
				if date_value.date() != today.date():
					return self.signal
			else:
				try:
					date = datetime.strptime(args[0][0], "%Y-%m-%d %H:%M:%S")
				except ValueError as e:
					return
				if date_value != date:
					return self.signal
		else:
			if date.lower() == "future":
				if date_value > today:
					return self.signal
			elif date.lower() == "past":
				if date_value < today:
					return self.signal
			elif date.lower() == "today":
				if date_value.date() == today.date():
					return self.signal
			else:
				try:
					date = datetime.strptime(args[0][0], "%Y-%m-%d %H:%M:%S")
				except ValueError as e:
					#print (str(e))
					return
				if date_value == date:
					return self.signal


	def validate_between(self, *args):
		date_value = datetime.strptime(self.value, "%Y-%m-%d %H:%M:%S")
		today = datetime.today()
		try:
			lower_bound = datetime.strptime(args[0][0], "%Y-%m-%d %H:%M:%S")
			upper_bound = datetime.strptime(args[0][0], "%Y-%m-%d %H:%M:%S")
		except ValueError as e:
			#print str(e)
			return
		negation = args[1]
		if negation:
			if (date_value < lower_bound and date_value > upper_bound):
				return self.signal
		else:
			if (date_value > lower_bound and date_value < upper_bound):
				return self.signal
