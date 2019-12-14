import sys
from numpy import zeros

class EditDistance:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # This method uses dynamic programming and returns the edit distance
    def edDistDp(self):
        
        D = zeros((len(self.x)+1, len(self.y)+1), dtype=int)
        D[0, 1:] = range(1, len(self.y)+1)
        D[1:, 0] = range(1, len(self.x)+1)
        for i in range(1, len(self.x)+1):
            for j in range(1, len(self.y)+1):
                delt = 1 if self.x[i-1] != self.y[j-1] else 0
                D[i, j] = min(D[i-1, j-1]+delt, D[i-1, j]+1, D[i, j-1]+1)
        return D[len(self.x), len(self.y)]

# Implementation
def main():
    
    if len(sys.argv)>1:
    
        with open(sys.argv[1]) as f:
            sequences = f.readlines()
        for i in range(len(sequences))[1::2]:
            print ('\nSequence 1: ' + sequences[i-1].rstrip())
            print ('Sequence 2: ' + sequences[i].rstrip() + '\n')
            seq1 = sequences[i-1].rstrip()
            seq2 = sequences[i].rstrip()
    
            edit = EditDistance(seq1, seq2)
            
            m = edit.edDistDp()
            print("Edit distance is: ", m)
            
    else:

        seq1 = 'TTACTGTGTTT'
        seq2 = 'CACCCCTGTG'  
        print ('\nSequence 1: ', seq1)
        print('Seqquence 2: ', seq2)
        edit = EditDistance(seq1, seq2)

        m = edit.edDistDp()
        print("Edit distance is: ",m)

if __name__=="__main__":
    main()
