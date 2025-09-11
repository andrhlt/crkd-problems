import { readFileSync } from 'fs';

function reverseString(a: number, b: number): number {
  return a + b;
}

const testCase = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const result = (reverseString as any)(...testCase.args);
process.exit(JSON.stringify(result) === JSON.stringify(testCase.expected) ? 0 : 1);

