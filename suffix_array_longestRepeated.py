import operator, sys
class SuffixArray:
    def __init__(self, seq):
        self.seq = seq
    # Returns the suffix array
    def suffix_array(self):
        return [t[1] for t in sorted((self.seq[i:],i) for i in range(len(self.seq)))]
    
    # Computes the longest common prefix between the suffixes
    def computeLCP(self):
        sa = self.suffix_array()
        m = len(self.seq)
        lcp = [0 for i in range(m)]
        for i in range(1,m):
            u = sa[i-1]
            v = sa[i]
            n = 0
            while self.seq[u] == self.seq[v]:
                n += 1
                u += 1
                v += 1
                if (u >= m) or (v >=m):
                    break
            lcp[i] = n
        return sa,lcp
    
    # Prints the results with suffix array, LCP, suffixes, and longest repeated substring.
    def print_func(self):
        saa,lcp = self.computeLCP()
        dictn={}
        
        print("SA,LCP,Suffix")
        for i, j in enumerate(saa):
            n = self.seq[j:]
            l = lcp[i]
            dictn[n[:l]]=lcp[i]
            print("%2d: %2d %s" % (j, lcp[i], self.seq[j:]))
        keyMax = max(dictn.items(), key = operator.itemgetter(1))[0]
        print('Longest repeated substring is: ', end = "")
        print(keyMax)
 


def main():
    
    if len(sys.argv)>1:
        
        with open(sys.argv[1]) as f:
            sequence = f.readlines()
            sequence = sequence[0].strip()
            print ('\nSequence: ' + sequence)
        
            SA2 = SuffixArray(sequence)
            SA2.print_func()
    else:

        sequence = "ATCGATCGA"
        print ('\nSequence : ', sequence)
        SA2 = SuffixArray(sequence)
        SA2.print_func()
        
        
if __name__=="__main__":
    main()
