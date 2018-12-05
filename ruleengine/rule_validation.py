import sys

from input_validation import ValidateInput
#from ValidateInput import validate_more, validate_less, validate_equal, validate_between

class ValidateRule(object):
	def __init__(self, rules_dict):
		self.rules = rules_dict
		self.key_words = None
		self.more_keywords = ["more", "rise", "beyond", "above", "after", "future"]
		self.less_keywords = ["less", "below", "under", "before", "past"]
		self.equal_keywords = ["equal", "is"]
		self.between_keywords = ["between", "in", "within"]
		self.negation_words = ["not", "never"]
		self.rule_book = {}
		
		for conditions in self.rules.values():
			lower_bound = None 
			upper_bound = None
			equal_value = None
			try:
				signal = conditions["signal"]
				operation = conditions["operation"]
			except KeyError as e:
				print "signal name or operation is not defined. Exiting..."
				sys.exit()
			if any (word in operation for word in self.more_keywords):
				lower_bound = conditions.get("lower_bound", None)
				upper_bound = conditions.get("upper_bound", None)
			if any (word in operation for word in self.less_keywords):
				lower_bound = conditions.get("lower_bound", None)
				upper_bound = conditions.get("upper_bound", None)
			if any (word in operation for word in self.between_keywords):
				lower_bound = conditions.get("lower_bound", None)
				upper_bound = conditions.get("upper_bound", None)
			if any (word in operation for word in self.equal_keywords):
				equal_value = conditions.get("equal_to", None)
				lower_bound = conditions.get("lower_bound", None)
				upper_bound = conditions.get("upper_bound", None)
			negation = False
			for word in self.negation_words:
				if word in operation:
					negation = True
					break
			rule_dict = {}
			if lower_bound and upper_bound:
				rule_dict['method'] = "validate_between"
				rule_dict['arguments'] = [lower_bound, upper_bound]
				rule_dict['negation'] = negation
			elif lower_bound:
				rule_dict['method'] = "validate_more"
				rule_dict['arguments'] = [lower_bound]
				rule_dict['negation'] = negation
			elif upper_bound:
				rule_dict['method'] = "validate_less"
				rule_dict['arguments'] = [upper_bound]
				rule_dict['negation'] = negation
			elif equal_value:
				rule_dict['method'] = "validate_equal"
				rule_dict['arguments'] = [equal_value]
				rule_dict['negation'] = negation

			if not rule_dict and conditions.get("equal_to", None):
				rule_dict['method'] = "validate_equal"
				rule_dict['arguments'] = [conditions.get("equal_to")]
				rule_dict['negation'] = negation
			if signal in self.rule_book.keys():
				self.rule_book[signal].append(rule_dict)
			else:
				self.rule_book[signal] = [rule_dict]

		print self.rule_book
