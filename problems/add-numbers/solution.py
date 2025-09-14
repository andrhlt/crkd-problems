import json
import sys


def add_numbers(a: int, b: int) -> int:
    # implement your solution here
    pass


if __name__ == "__main__":
    test_case = json.load(open(sys.argv[1], 'r'))
    result = add_numbers(*test_case['args'])
    if '--output' in sys.argv:
        print(json.dumps(result))
    else:
        sys.exit(0 if result == test_case['expected'] else 1)
