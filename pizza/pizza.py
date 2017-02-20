from gcode17 import parse


class Pizza:

    def __init__(self, width, height, ing, size, array):
        self.width = width
        self.height = height
        self.ing = ing
        self.size = size
        self.array = array

    def subset(self, r1, c1, r2, c2):
        return map(lambda x: x[c1:c2 + 1], self.array[r1:r2 + 1])

    def valid_subset(self, r1, c1, r2, c2):
        count = {'T': 0, 'M': 0}
        s = self.subset(r1, c1, r2, c2)
        for r in s:
            for elem in r:
                count[elem] += 1
        return count['T'] >= self.ing and count['M'] >= self.ing


class Portion:

    def __init__(self, r1, c1, r2, c2):
        self.c1 = c1
        self.r1 = r1
        self.c2 = c2
        self.r2 = r2
        self.area = (c2 - c1 + 1) * (r2 - r1 + 1)

    def __str__(self):
        return "%d %d %d %d\n" % (self.r1, self.c1, self.r2, self.c2)

    def valid(self, pizza):
        return self.area <= pizza.size and pizza.valid_subset(self.r1, self.c1, self.r2, self.c2) or self.area < 2

    def really(self, pizza):
        return pizza.valid_subset(self.c1, self.r1, self.c2, self.r2)

    def part(self):
        if self.c2 - self.c1 < self.r2 - self.r1:
            return (Portion(self.r1, self.c1, (self.r1 + self.r2) / 2, self.c2), Portion((self.r1 + self.r2) / 2 + 1, self.c1, self.r2, self.c2))
        else:
            return (Portion(self.r1, self.c1, self.r2, (self.c1 + self.c2) / 2), Portion(self.r1, (self.c1 + self.c2) / 2 + 1, self.r2, self.c2))

# Nombre del fichero a parsear
namefile = "big"
filein = "pizza/in/%s.in" % namefile
fileout = "pizza/out/%s.out" % namefile

# Estructura para parsear
s = """
Main = Int Int Int Int -> *Line | Pizza
Line = String
"""

# Parsear
pizza = parse(filein, s, globals())

# Resolver
ps = [Portion(0, 0, pizza.width - 1, pizza.height - 1)]
valid = False
while not valid:
    valid = True
    qs = []
    for p in ps:
        if not p.valid(pizza):
            valid = False
            p1, p2 = p.part()
            qs.append(p1)
            qs.append(p2)
        else:
            qs.append(p)
    ps = qs
ps = filter(lambda x: x.really(pizza), ps)

# Escribir
f = open(fileout, 'w')
f.write(str(len(ps)) + "\n")
for p in ps:
    f.write(str(p))
f.close()
