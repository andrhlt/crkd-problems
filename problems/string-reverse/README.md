# Reverse a String

Write a function that reverses a string.

## What to implement

Create a solution that reads `input.txt` and writes the reversed string to `output.txt`.

## Expected files
- Input: `input.txt` (a string to reverse)
- Output: `output.txt` (the reversed string)

## Example

**input.txt:**
```
hello world
```

**output.txt:**
```
dlrow olleh
```

## Setup

This problem uses TypeScript:

```bash
crkd setup  # Installs tsx and typescript
```

## Testing
```bash
crkd test  # Runs: npx tsx solution.ts (defined in problem.yaml)
```

## Implementation

Create a `solution.ts` file that:
1. Reads from `input.txt`
2. Reverses the string
3. Writes to `output.txt`