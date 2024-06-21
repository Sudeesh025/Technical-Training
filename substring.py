def substring(s):
    ns = ""
    ns = str(ns)
    c = 0
    for i in ls:
        if(s in i):
            c = c + 1
    return c
n = int(input())
ls = set()
ns = " "
for i in range(n):
    n = int(input())
    if(n == 1):
        s = input()
        ls.add(s)
    elif(n == 2):
        s = input()
        print(s in ls)
    elif(n == 3):
        s = input()
        print(substring(s))
    elif(n == 4):
        s = input()
        ls.remove(s)class node:
    def __init__(self):
        self.d = {}
        self.flag = 0


class tries:
    def __init__(self):
        self.root = node()

    def insert(self, str):
        t= self.root
        for i in str:
            if i not in t.d:
                t.d[i] = node()
            t=t.d[i]
        t.flag = 1
    def  search(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return t.flag == 1
    def prefix(self,str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return True
    def _dfs(self, node, prefix):
        if node.flag == 1:
            ls.append(prefix)
        for char, next_node in node.d.items():
            self._dfs(next_node, prefix + char)
        return ls
    def print_prefix(self):
        prefix=input("Enter prefix: ")
        t = self.root
        for char in prefix:
            if char not in t.d:
                return
            t = t.d[char]
        return self._dfs(t, prefix)
ls = []
t1 = tries()
n=int(input())
for i in range(n):
    s = input()
    t1.insert(s)
print(t1.search('word'))
#print(t1.prefix('wo'))
print(max(t1.print_prefix()))