import re
import sys


class Circuit:

    def __init__(self,name,skills):
        # (H,E,P)
        self.skills = (int(skills[0]),int(skills[1]),int(skills[2]))
        # ID
        self.name = name
        # Assigned Jugglers
        self.jugglers = []
        # Not Full
        self.free = True

    def score(self,juggler):
        (x1,y1,z1) = self.skills
        (x2,y2,z2) = juggler['skills']
        return x1*x2 + y1*y2 + z1*z2


class StableMatching:

    def __init__(self,circuits,jugglers):
        self.jugglers = jugglers
        self.circuits = circuits
        self.circuitSize = len(jugglers)/len(circuits)
        self.match()

    # Add juggler to circuit
    # If it fits then return None
    # If it doesnt fit return the juggler that is left off
    def addJuggler(self,juggler,circuit):

        # if circuit is not full addd juggler to list
        if circuit.free:
            circuit.jugglers.append(juggler)
            juggler['index'] += 1
            # if this juggler makes if full set free to false
            if len(circuit.jugglers) == self.circuitSize:
                circuit.free = False
            return None
        #Circuit is full
        else:
            # current juggler and score
            lowestJuggler = juggler
            lowestScore = circuit.score(juggler)

            # find lowest score and juggler of group
            for nextJuggler in circuit.jugglers:
                if circuit.score(nextJuggler) < lowestScore:
                    lowestJuggler = nextJuggler
                    lowestScore = circuit.score(nextJuggler)

            # if this juggler is the lowest do just up the index
            if lowestJuggler == juggler:
                juggler['index'] += 1
            else:
                circuit.jugglers.remove(lowestJuggler)
                circuit.jugglers.append(juggler)
            return lowestJuggler


    # find best match of juggler and circuit from lst
    def bestMatch(self,circuit, jugglerList):
        bestScore = -sys.maxsize -1
        bestMatch = None
        for juggler in jugglerList:
            if circuit.score(juggler) > bestScore:
                bestScore = circuit.score(juggler)
                bestMatch = juggler
        return bestMatch


    # assign left-over jugglers to free circuits based on best score
    def assignLost(self,lostJugglers):
        for circuit in self.circuits:
            while circuit.free:
                jugglerToAdd = self.bestMatch(circuit,lostJugglers)
                self.addJuggler(jugglerToAdd,circuit)
                lostJugglers.remove(jugglerToAdd)
                          
                

    # match all jugglers with circuits
    def match(self):
        LostJugglers = []
        while self.jugglers:
            nextJuggler = self.jugglers.pop(0)
            if nextJuggler['index'] == len(nextJuggler['prefs']):
                LostJugglers.append(nextJuggler)
            else:
                nextCircuit = self.circuits[nextJuggler['prefs'][nextJuggler['index']]]
                overflow = self.addJuggler(nextJuggler,nextCircuit)
                if overflow is not None:
                    self.jugglers.append(overflow)

        self.assignLost(LostJugglers)

    #String representation of a Juggler: J## C## C##...
    def jugglerString(self,juggler):
        s = 'J' + juggler['name'] + ' '
        for i in range(len(juggler['prefs'])):
            circuit = self.circuits[juggler['prefs'][i]]
            s += "C%s:%s "%(circuit.name,circuit.score(juggler))
        return s
    
    #String Representation of a Circuit: C## J## C## C##..., J## C## C##...,...
    def circuitString(self,circuit):
        circuit.jugglers.sort(key=circuit.score,reverse=True)
        s = 'C' + circuit.name + ' '

        for i in range(len(circuit.jugglers)):
            s += self.jugglerString(circuit.jugglers[i])
            s = s[:-1] + ', '
        print(s[:-2])
      


# Parse file
def parseFile(filename):
    circuits = []
    jugglers = []
    with open(filename) as f:
        for line in f:
            skills = re.findall(r':([0-9]*)', line)
            if (line[0] == 'C'):
                name = (re.findall(r'C([0-9]+)',line))[0]
                circuits.append(Circuit(name,skills))
            elif (line[0] == 'J'):
                name = (re.findall(r'J([0-9]+)',line))[0]
                prefs = re.findall(r'C([0-9]*)', line)
                prefs1 = []
                for i in range(0,len(prefs)):
                    prefs1.append(int(prefs[i]))
                jugglers.append(
                    {'name' : name,
                     'skills' : (int(skills[0]),int(skills[1]),int(skills[2])),
                     'prefs' : prefs1,
                     'index' : 0})
    return (jugglers,circuits)



#Run on input file

(jugglers,circuits) = parseFile(sys.argv[1])

stableMatching = StableMatching(circuits,jugglers)

total = 0

for juggler in stableMatching.circuits[1970].jugglers:
       total += int(juggler['name'])

print(total)

