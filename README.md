# crkd-problems

## Example Python Problem

```python
import json
import sys


def add_numbers(a: int, b: int):
    return a + b


if __name__ == "__main__":
    with open(f'./tests/public/{sys.argv[1]}', 'r') as f:
        case = json.load(f)
    result = add_numbers(*case['input'])
    sys.exit(0 if result == case['expected'] else 1)
```
