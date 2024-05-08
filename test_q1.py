#!/usr/bin/env python3

from exam4_q1 import get_geno_strings 
import pytest 

def test_k_zero():
  s = "ATGTCTGTCTGAA"
  k = 0
  CORRECT = {'': {''}}
  assert get_geno_strings(s, k) == CORRECT 

def test_same_letter():
  s = "GGGGGGGG"
  k = 3
  CORRECT = {
    "GGG": {"GGG"} 
  }
  assert get_geno_strings(s, k) == CORRECT
  
def test_k_1():
  s = "ATGTCTGTCTGAA"
  k = 1
  CORRECT = {
    'A': {'A'},
    'T': {'G', 'A'},
    'G': {'A'},
    'C': {'T', 'G', 'A'}
  }
  assert get_geno_strings(s, k) == CORRECT

