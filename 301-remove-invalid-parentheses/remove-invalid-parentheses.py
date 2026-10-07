class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        res = set()

        def dfs(i, l, r, open_count, path):
            if i == len(s):
                if l == 0 and r == 0 and open_count == 0:
                    res.add("".join(path))
                return
            c = s[i]
            if c == '(' and l > 0:
                dfs(i + 1, l - 1, r, open_count, path)
            elif c == ')' and r > 0:
                dfs(i + 1, l, r - 1, open_count, path)
            path.append(c)
            if c == '(':
                dfs(i + 1, l, r, open_count + 1, path)
            elif c == ')':
                if open_count > 0:
                    dfs(i + 1, l, r, open_count - 1, path)
            else:
                dfs(i + 1, l, r, open_count, path)
            path.pop()

        dfs(0, left, right, 0, [])
        return list(res)