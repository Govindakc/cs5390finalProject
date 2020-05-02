# CS5390FinalProject
Course Link: http://cs5390f19.deblasiolab.org/ <b>
Implementation of five different algorithms in computational biology: From sequence alignment to compression.
## Requirements:
* python==3.7.4
* numpy==1.17.2
## Setup
* brew install python3
* pip install numpy

## Usage:
```bash
python name_of_file.py input.txt
[for Needleman-Wunsch, Smith-Waterman, Edit Disatance]
python name_of_file.py input_bwt.txt
[for Burrows wheeler]
python name_of_file.py input_longest_repeated_sub.txt
[for Longest repeated substring]
Or python name_of_file.py (as file contains sample strings)
```
* For BWT, please insert $ at the end of the string.
