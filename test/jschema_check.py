# Copyright Rene Ferdinand Rivera Morell

import argparse
import json
from jsonschema.validators import validator_for

parser = argparse.ArgumentParser()
parser.add_argument("--negate",default=False,action='store_true')
parser.add_argument("--schema")
parser.add_argument("--input")

def run():
	args = parser.parse_args()
	print(args)
	with open(args.schema, "r") as f:
		schema = json.load(f)
	with open(args.input, "r") as f:
		input = json.load(f)
	Validator = validator_for(schema)
	Validator.check_schema(schema)
	validator = Validator(schema)
	# is_valid = validator.is_valid(input)
	is_valid = True
	for error in validator.iter_errors(input):
		is_valid = False
		print(error)
	if is_valid:
		print("valid")
		return not args.negate
	else:
		print("invalid")
		return args.negate

exit(0 if run() else 1)
