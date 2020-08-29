# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

# ==========
# FRÅGA 1
# ==========
def movieTickets():
    tickets = -1
    # Använder while-loops för att validera användarens input ifall felaktig data matas in.
    # Om datan är felaktig frågas användaren igen.
    while (tickets <= 0):
        tickets = eval(input("Hur många biljetter vill du köpa? "))
        if tickets < 0:
            print("Välj minst 1 biljett.")

    below18 = tickets + 1
    while (below18 > tickets or below18 < 0):
        below18 = eval(input("Hur många av er är under 18 år? "))
        if below18 > tickets:
            print("Antal biljetter för personer under 18 år kan inte vara fler än det totala antalet personer.")
        elif below18 < 0:
            print("Välj inte negativt antal.")

    time = 25
    while (time > 24):
        time = eval(input("Vilken föreställning (ange klockslag i hela timmar)? "))
        if time > 24 or time < 0:
            print("Ange giltigt klockslag.")

    price = 100 * (tickets - below18)
    price += 50 * below18
    if time < 18:
        price *= 0.9

    print("Biljetterna kostar sammanlagt " + str(int(price)) + " kr.")



# ==========
# FRÅGA 2
# ==========
def pepLineLength(filename):
    lines = open(filename, 'r', encoding='utf8').readlines()
    countLongRows = 0

    for i in range(len(lines)):
        # Av någon anledning blir längden av varje avläst rad 1 karaktär för mycket,
        # därför tar jag - 1 för längden på varje avläst rad.
        lineLength = len(lines[i]) - 1
        if lineLength > 79:
            print("line " + str(i + 1) + " too long: " + str(lineLength))
            countLongRows += 1

    print(str(countLongRows) + " lines are too long")



# ==========
# FRÅGA 3
# ==========
class Tree:
    def __init__(self,node,trees):
        self.root = node
        self.subtrees = trees
    def getParts(self):
        return self.root, self.subtrees

royal = Tree("CarlGustaf", [Tree("Victoria", [Tree("Estelle", []), Tree("Oscar", [])]), Tree("CarlPhilip", [Tree("Alexander", [])]), Tree("Madeleine", [Tree("Leonore", []), Tree("Nicolas", [])])])

def preorder(tree):
    res = []
    res.append(tree.root)
    if tree.subtrees != []:
        for i in range(len(tree.subtrees)):
            res += preorder(tree.subtrees[i])

    return res

# Omvänd logik från preorder.
def postorder(tree):
    res = []
    
    if tree.subtrees != []:
        for i in range(0, len(tree.subtrees), 1):
            res += postorder(tree.subtrees[i])

    res.append(tree.root)
    return res



# ==========
movieTickets()
#pepLineLength("file.txt")
#print(preorder(royal))
#print(postorder(royal))