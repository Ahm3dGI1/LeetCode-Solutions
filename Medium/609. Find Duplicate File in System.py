class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = {}

        def findContent(f):
            i = 0
            while f[i] != '(':
                i+=1
            return f[:i], f[i+1:-1]

        for path in paths:
            d = path.split(" ")[0]
            fs = path.split(" ")[1:]

            for f in fs:
                name, content = findContent(f)
                if content not in m:
                    m[content] = []
                m[content].append(d+"/"+name)
        
        keys = list(m.keys())

        for key in keys:
            if len(m[key]) <= 1:
                del m[key]

        return list(m.values())