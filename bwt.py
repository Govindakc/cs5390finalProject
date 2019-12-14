# Burrows wheeler transform
import sys

class Bwt:
    # Constructor
    def __init__(self, s):
        self.s = s
    
    def rotations(self,s):
        s2 = self.s * 2
        return [ s2[i:i+len(self.s)] for i in range(len(self.s)) ]
    
    def sorted_list(self,s):
        return sorted(self.rotations(self.s))
    
    def bwtViaSorted_list(self):
        return ''.join(map(lambda x: x[-1], self.sorted_list(self.s)))
"""    
s = "mississippi$"
bwt = Bwt(s)
b=bwt.bwtViaSorted_list()
print("The BWT of ",s,"  is --> ", end="")
print(b)
print("_______________________and______________________")
"""
class invBWT:
    def __init__(self, bw):
        self.bw = bw
    def rankBwt(self):
        ''' Given BWT string bw, return parallel list of B-ranks.  Also
            returns tots: map from character to # times it appears. '''
        tots = dict()
        ranks = []
        for c in self.bw:
            if c not in tots:
                tots[c] = 0
            ranks.append(tots[c])
            tots[c] += 1
        return ranks, tots


    def firstCol(self, tots):
        ''' Return map from character to the range of rows prefixed by
            the character. '''
        first = {}
        totc = 0
        for c, count in sorted(tots.items()):
            first[c] = (totc, totc + count)
            totc += count
        return first


    def reverseBwt(self):
        ''' Make T from BWT(T) '''
        ranks, tots = self.rankBwt()
        first = self.firstCol(tots)
        rowi = 0 # start in first row
        t = '$' # start with rightmost character
        while self.bw[rowi] != '$':
            c = self.bw[rowi]
            t = c + t # prepend to answer
            # jump to row that starts with c of same rank
            rowi = first[c][0] + ranks[rowi]
        return t
"""
inv = invBWT(b)
c=inv.reverseBwt()
print("The reverse BWT of ",b,"  is --> ", end="")
print(c)
"""

# Implementation
def main():

    if len(sys.argv)>1:

        with open(sys.argv[1]) as f:
            sequence = f.readlines()
            sequence = sequence[0].strip()
            print ('\nSequence: ' + sequence)
            
            bwt = Bwt(sequence)
            b=bwt.bwtViaSorted_list()
            print("The BWT of ",sequence,"  is --> ", end="")
            print(b)
            print("_______________________and______________________")
            inv = invBWT(b)
            c=inv.reverseBwt()
            print("The reverse BWT of ",b,"  is --> ", end="")
            print(c)
    else:

        sequence = "MISSISSIPPI$"
        print ('\nSequence : ', sequence)
        bwt = Bwt(sequence)
        b=bwt.bwtViaSorted_list()
        print("The BWT of ",sequence,"  is --> ", end="")
        print(b)
        print("_______________________and______________________")
        inv = invBWT(b)
        c=inv.reverseBwt()
        print("The reverse BWT of ",b,"  is --> ", end="")
        print(c)


if __name__=="__main__":
    main()
