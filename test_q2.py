 #!/usr/bin/env python3


from exam4_q2 import get_geno_strings, all_substrings
import pytest

def test_k_zero_pt2(): #Testing what would happen if k was 0. 
  file = "sample.txt" #The sample text to use.
  k = 0 #the input for k
  CORRECT = {'AGTCGTGCAGTCAGTG': {'': {''}}, 'GTACGTACGATCACGAGAG': {'': {''}}, 'ACGGAC': {'': {''}}} #The output that is expected when k = 0
  assert all_substrings(file, k) == CORRECT #If this matches the function passes. 
  
def test_empty_file(): #Testing what would happen if an empty file was given. 
  file = "empty.txt" #The file is empty, but it exists.
  k = 3 #A value for k
  CORRECT = {'': {}} #What the expected outcome is
  assert all_substrings(file, k) == CORRECT #If this matches the function passes. 

def test_missing_file(): #Testing what would happen if there was no file given
  with pytest.raises(FileNotFoundError): #An error would come up saying file is not found. 
    file = "missing.txt" #The missing file!
    k = 4 #A value for k
    all_substrings(file, k) #the function. 
