
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    # Cannot use the same copy twice
                    if i == j or j == k or i == k:
                        continue

                    # Hundreds digit cannot be 0
                    if digits[i] == 0:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]

                    numbers.add(number)

        return len(numbers)

