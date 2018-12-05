Requirements:
This requires docopt and pyyaml libraries. They can be installed with pip.

Run Command:
python run_ruleengine.py -r tests/rulerepo/rules.yaml -j tests/datastream/input.json

Assumptions:
1. Single rule contains only one signal name and one value to compare with.
2. It is assumed that rule and inputs are in same timezone.
4. Time in 24 hour notation.
5. Verification for int and float both done when input value_type is integer.

Future Roadmap:
1. More keywords can be added to decode the rules.
2. The code works for finite number of input. If the input size increases, performance issues will increase. To avoid that, multithreading will be introduced.
3. Logging will be done properly.
