class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def multiply(set1, set2):
            result = set()

            for a in set1:
                for b in set2:
                    result.add(a + b)

            return result

        def parse(i):
            current = {""}
            union = set()

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    union |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)

                else:
                    # lowercase letter
                    current = multiply(current, {expression[i]})
                    i += 1

            union |= current

            return union, i + 1 if i < len(expression) and expression[i] == '}' else i

        result, _ = parse(0)

        return sorted(result)