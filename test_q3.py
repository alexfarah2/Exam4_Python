#!/usr/bin/env python3

from exam4_q3 import find_smallest_k, all_substrings, get_geno_strings
import pytest

def test_empty_file():
  file = "empty.txt"
  assert find_smallest_k(file) == NO K
  
def test_error_no_file():
  with pytest.raises(FileNotFoundError)
    file = "missing.txt"
    find_smallest_k(file)
    
def not_sequences_just_words():
  file = "nosequence.txt"
  assert find_smallest_k(file) == NO SEQUENCE
  
