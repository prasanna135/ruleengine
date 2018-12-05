import json
import sys
import yaml

from input_validation import ValidateIntInput, ValidateStrInput, ValidateDateInput
from rule_validation import ValidateRule

def run(args):
	rule_file = args['--rulefile']
	input_file = args['--json']
	rule_repo = decode_yaml(rule_file)
	sig_objs = stream_json(input_file)
	output_signals = []
	for sig_obj in sig_objs:
		if sig_obj.signal in rule_repo.rule_book.keys():
			rules = rule_repo.rule_book[sig_obj.signal]
			for rule in rules:
				signal = None
				val_method = rule['method']
				if val_method == "validate_between":
					signal = sig_obj.validate_between(rule['arguments'], rule['negation'])
				elif val_method == "validate_more":
					signal = sig_obj.validate_more(rule['arguments'], rule['negation'])
				elif val_method == "validate_less":
					signal = sig_obj.validate_less(rule['arguments'], rule['negation'])
				elif val_method == "validate_equal":
					signal = sig_obj.validate_equal(rule['arguments'], rule['negation'])
				else:
					print "Rule is not decoded properly"
				if signal:
					output_signals.append(signal)
	print output_signals

def decode_yaml(rule_file):
	f = open(rule_file, "r")
	rules = yaml.load(f)
	f.close()
	#print rules
	return ValidateRule(rules)

def stream_json(json_file):
	sig_objs = []
	with open(json_file) as f:
		input_data = json.load(f)

	int_sig = None
	for sig_input in input_data:
		if sig_input["value_type"].lower() == "integer":
			int_sig = ValidateIntInput(sig_input)
		elif sig_input["value_type"].lower() == "string":
			int_sig = ValidateStrInput(sig_input)
		elif sig_input["value_type"].lower() == "datetime":
			int_sig = ValidateDateInput(sig_input)
		else:
			print "value type is not mentioned. Exiting..."
			sys.exit()
		sig_objs.append(int_sig)
	return sig_objs




