class Solution:
    def removeInvalidParentheses(self, s):
        # Find minimum number of removals needed
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, path, balance, left_remove, right_remove):
            # Invalid prefix
            if balance < 0:
                return

            # End of string
            if index == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Remove current parenthesis
            if ch == '(' and left_remove > 0:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_remove - 1,
                    right_remove
                )

            elif ch == ')' and right_remove > 0:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_remove,
                    right_remove - 1
                )

            # Keep current character
            if ch == '(':
                path.append(ch)
                backtrack(
                    index + 1,
                    path,
                    balance + 1,
                    left_remove,
                    right_remove
                )
                path.pop()

            elif ch == ')':
                if balance > 0:
                    path.append(ch)
                    backtrack(
                        index + 1,
                        path,
                        balance - 1,
                        left_remove,
                        right_remove
                    )
                    path.pop()

            else:
                # Letter
                path.append(ch)
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_remove,
                    right_remove
                )
                path.pop()

        backtrack(0, [], 0, left_remove, right_remove)

        return list(result)