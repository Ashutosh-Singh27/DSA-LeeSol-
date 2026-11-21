class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        newp = parent[:]
        last = [-1] * 26
        saved = [-1] * n
        order = []
        stack = [0]

        while stack:
            x = stack.pop()
            if x >= 0:
                c = ord(s[x]) - 97
                if last[c] != -1:
                    newp[x] = last[c]
                saved[x] = last[c]
                last[c] = x
                order.append(x)
                stack.append(~x)          # exit marker
                stack.extend(children[x])
            else:
                x = ~x
                last[ord(s[x]) - 97] = saved[x]   # restore

        size = [1] * n
        for x in reversed(order):
            if x != 0:
                size[newp[x]] += size[x]
        return size