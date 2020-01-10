# Smith-Waterman
import numpy as np
import sys
class SmithWaterman:
    # Constructor
    def __init__(self, s1, s2, mt, ms, gap):
        self.s1 = s1
        self.s2 = s2
        self.mt = mt
        self.ms = ms
        self.gap = gap
        
    #  This method returns the scores.
    def score_fun(self,ch1, ch2):
        if ch1 == ch2:
            return self.mt
        elif ch1 == '-' or ch2 == '-':
            return self.gap
        else:
            return self.ms
    # This method is used to loop over the spaces in the matrix
    # and use the score function to give the correct value.
    def waterman(self):
        m, n = len(self.s1), len(self.s2)
        H = np.zeros((m+1, n+1))    
        T = np.zeros((m+1, n+1))
        max_score = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diag = H[i-1][j-1] + self.score_fun(self.s1[i-1], self.s2[j-1])
                up = H[i][j-1] + self.gap
                left = H[i-1][j] + self.gap
                H[i][j] = max(0,left, up, diag)
                if H[i][j] == 0: T[i][j] = 0
                if H[i][j] == left: T[i][j] = 1
                if H[i][j] == up: T[i][j] = 2
                if H[i][j] == diag: T[i][j] = 3
                if H[i][j] >= max_score:
                    max_i = i
                    max_j = j
                    max_score = H[i][j]
        
        print('M=\n',H,'\n')
        print('Optimal alignment score= ', max_score, '\n')
        
     #Storing the trackback in the form of matrix
        print('1 - means we came here from up')
        print('2 - means we came here from the left')
        print('3 - means we came here from the diagonal')
        print('T=\n',T,'\n')
         
        align1, align2 = '', ''
        i,j = max_i,max_j
        
        #Traceback
        while T[i][j] != 0:
            if T[i][j] == 3:
                a1 = self.s1[i-1]
                a2 = self.s2[j-1]
                i -= 1
                j -= 1
            elif T[i][j] == 2:
                a1 = '-'
                a2 = self.s2[j-1]
                j -= 1
            elif T[i][j] == 1:
                a1 = self.s1[i-1]
                a2 = '-'
                i -= 1
            align1 += a1
            align2 += a2
    
        align1 = align1[::-1]
        align2 = align2[::-1]
        
        iden = 0
        for i in range(len(align1)):
            a1 = align1[i]
            a2 = align2[i]
            if a1 == a2:                
                iden += 1
            

        identity = iden / len(align1) * 100
        print('Identity = %f percent' % identity)
        print(align1)
        print(align2)                  
    

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
        
            smithw = SmithWaterman(seq1, seq2, 5,-1,-0.5)
        
            smithw.waterman()
    else:

        seq1 = 'TTACTGTGTTT'
        seq2 = 'CACCCCTGTG'  
        print ('\nSequence 1: ', seq1)
        print('Seqquence 2: ', seq2)
        smithw = SmithWaterman(seq1, seq2, 5,-1,-0.5)
        smithw.waterman()
        
        
if __name__=="__main__":
    main()
