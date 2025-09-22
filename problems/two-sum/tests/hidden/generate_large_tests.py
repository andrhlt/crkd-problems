import json
import os
from typing import List, Tuple

# filename, size, target, first_value, second_value
CASES: List[Tuple[str, int, int, int, int]] = [
    ("case1.json", 10, 1_000_123, 1_000_000, 123),
    ("case7.json", 100, 1_200_500, 1_200_000, 500),
    ("case8.json", 1_000, 1_500_110, 1_500_000, 110),
    ("case9.json", 10_000, 1_800_888, 1_800_000, 888),
    ("case10.json", 100_000, 2_100_999, 2_100_000, 999),
]


def build_numbers(size: int, first: int, second: int) -> List[int]:
    """Create a list where exactly one pair (first, second) sums to the target."""
    numbers = [first]
    # Fill with distinct negative numbers to avoid unintended complements.
    numbers.extend(-i for i in range(1, size - 1))
    numbers.append(second)
    return numbers


def validate_unique_solution(nums: List[int], target: int, expected: Tuple[int, int]) -> None:
    """Ensure there is exactly one valid pair matching the expected indices."""
    seen: dict[int, List[int]] = {}
    expected_sorted = tuple(sorted(expected))
    pair_count = 0
    for idx, value in enumerate(nums):
        comp = target - value
        if comp in seen:
            for comp_idx in seen[comp]:
                pair = tuple(sorted((comp_idx, idx)))
                if pair != expected_sorted:
                    raise ValueError("Unexpected pair identified")
                pair_count += 1
                if pair_count > 1:
                    raise ValueError("Multiple valid pairs found")
        seen.setdefault(value, []).append(idx)
    if pair_count != 1:
        raise ValueError("Failed to find the expected pair")


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for filename, size, target, first, second in CASES:
        if first + second != target:
            raise ValueError(f"Target mismatch for {filename}")
        numbers = build_numbers(size, first, second)
        expected = (0, size - 1)
        validate_unique_solution(numbers, target, expected)
        payload = {
            "args": [numbers, target],
            "expected": list(expected),
            "size": size,
        }
        out_path = os.path.join(base_dir, filename)
        with open(out_path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")


if __name__ == "__main__":
    main()
