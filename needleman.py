import sys
class NeedleMan:
    def __init__(self, match_award, mismatch_penalty, gap_penalty):
        self.match_award = match_award
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
    
    def print_matrix(self,mat):
        # Loop over all rows
        for i in range(0, len(mat)):
            print("[", end = "")
            # Loop over each column in row i
            for j in range(0, len(mat[i])):
                # Print out the value in row i, column j
                print(mat[i][j], end = "")
                # Only add a tab if we're not in the last column
                if j != len(mat[i]) - 1:
                    print("\t", end = "")
            print("]\n")
            
    def zeros(self, rows, cols):
    # Define an empty list
        retval = []
        # Set up the rows of the matrix
        for x in range(rows):
            # For each row, add an empty list
            retval.append([])
            # Set up the columns in each row
            for y in range(cols):
                # Add a zero to each column in each row
                retval[-1].append(0)
        # Return the matrix of zeros
        return retval
    
    def match_score(self,alpha, beta):
        if alpha == beta:
            return self.match_award
        elif alpha == '-' or beta == '-':
            return self.gap_penalty
        else:
            return self.mismatch_penalty
        
    def needleman_wunsch(self, seq1, seq2):
    
        # length of two sequences
        n = len(seq1)
        m = len(seq2)  

        # Generate matrix of zeros to store scores
        score = self.zeros(m+1, n+1)

        # Fill out first column
        for i in range(0, m + 1):
            score[i][0] = self.gap_penalty * i

        # Fill out first row
        for j in range(0, n + 1):
            score[0][j] = self.gap_penalty * j

        # Fill out all other values in the score matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the score by checking the top, left, and diagonal cells
                match = score[i - 1][j - 1] + self.match_score(seq1[j-1], seq2[i-1])
                delete = score[i - 1][j] + self.gap_penalty
                insert = score[i][j - 1] + self.gap_penalty
                # Record the maximum score from the three possible scores calculated above
                score[i][j] = max(match, delete, insert)

        self.print_matrix(score)
        print("Optimal Global alignment score is: ", score[-1][-1])
        align1 = ""
        align2 = ""

        # Start from the bottom right cell in matrix
        i = m
        j = n

        # We'll use i and j to keep track of where we are in the matrix, just like above
        while i > 0 and j > 0: # end touching the top or the left edge
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]

            # Check to figure out which cell the current score was calculated from,
            # then update i and j to correspond to that cell.
            if score_current == score_diagonal + self.match_score(seq1[j-1], seq2[i-1]):
                align1 += seq1[j-1]
                align2 += seq2[i-1]
                i -= 1
                j -= 1
            elif score_current == score_up + self.gap_penalty:
                align1 += seq1[j-1]
                align2 += '-'
                j -= 1
            elif score_current == score_left + self.gap_penalty:
                align1 += '-'
                align2 += seq2[i-1]
                i -= 1

        # Finish tracing up to the top left cell
        while j > 0:
            align1 += seq1[j-1]
            align2 += '-'
            j -= 1
        while i > 0:
            align1 += '-'
            align2 += seq2[i-1]
            i -= 1

        # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
        # These two lines reverse the order of the characters in each sequence.
        align1 = align1[::-1]
        align2 = align2[::-1]

        return (align1, align2)
    

def main():

    if len(sys.argv)>1:

        with open(sys.argv[1]) as f:
            sequences = f.readlines()
        for i in range(len(sequences))[1::2]:
            print ('\nSequence 1: ' + sequences[i-1].rstrip())
            print ('Sequence 2: ' + sequences[i].rstrip() + '\n')
            seq1 = sequences[i-1].rstrip()
            seq2 = sequences[i].rstrip()

            needm = NeedleMan(5, -1, -0.5)
            
            output1, output2 = needm.needleman_wunsch(seq1, seq2)
            print(output1 + "\n" + output2)

    else:

        seq1 = 'TTACTGTGTTT'
        seq2 = 'CACCCCTGTG'
        print ('\nSequence 1: ', seq1)
        print('Seqquence 2: ', seq2)
        needm = NeedleMan(5, -1, -0.5)
        output1, output2 = needm.needleman_wunsch(seq1, seq2)
        print(output1 + "\n" + output2)
    
if __name__=="__main__":
    main()

