"""
Rule Engine

Usage:
  run_ruleengine -r <rule_file> -j <input_file>
  run_ruleengine -h | --help

Options:
  -h --help                                   Show this screen.
  -r <rule_file> --rulefile <rule_file>      yaml file of rule list
  -j <input_file> --json <input_file>        json input file
"""
import docopt

from ruleengine.run import run

if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    run(args)