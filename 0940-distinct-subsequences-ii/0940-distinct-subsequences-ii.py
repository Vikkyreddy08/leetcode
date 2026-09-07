
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1  # empty subsequence
        last = {}

        for c in s:
            old_dp = dp

            # Add new subsequences by appending c
            dp = 2 * dp

            # Remove duplicates created by previous c
            if c in last:
                dp -= last[c]

            dp %= MOD

            # Remember the old count before this c was processed
            last[c] = old_dp

        # Remove the empty subsequence
        return (dp - 1) % MOD

