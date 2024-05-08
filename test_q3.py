#!/usr/bin/env python3

from exam4_q3 import find_smallest_k, all_substrings, get_geno_strings
import pytest

def test_empty_file(): #Testing if there was an empty file inserted what error would happen. 
  file = "empty.txt" #This file has an empty text
  k = 4 #a value for k
  assert find_smallest_k(file) == NONE #it should come back with nothing. If it matches this will pass
  
def test_error_no_file(): #Testing what would happen if there wasn't a file given
  with pytest.raises(FileNotFoundError): #an error should arise where there isn't a file found/possible
    file = "missing.txt" #The file is missing
    find_smallest_k(file) #The function
    
def not_sequences_just_words(): #Testing what would happen if the file had something in it, but not sequences
  file = "nosequence.txt" #This file has words in it, but not a sequence. It also has symbols. 
  k = 4 #a value for k
  assert find_smallest_k(file) == NONE #The result should be no value for k. If it matches this will pass. 
  
