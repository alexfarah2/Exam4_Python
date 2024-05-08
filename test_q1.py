#!/usr/bin/env python3

from exam4_q1 import get_geno_strings 
import pytest 

def test_k_zero(): #Testing what happens if k is given a value of zero. 
  s = "ATGTCTGTCTGAA" #The argument for s
  k = 0 #The value of k
  CORRECT = {'': {''}} #What the expected output will be
  assert get_geno_strings(s, k) == CORRECT #If it matches, this will pass.

def test_same_letter(): #Testing what will happen if the string is just the same letter
  s = "GGGGGGGG" #The string
  k = 3 #The value for k
  CORRECT = {
    'GGGGGGGGG': {'GGG': {'GGG'}}
  } #What is expected
  assert get_geno_strings(s, k) == CORRECT #If the outputs match, this will pass.
  
def test_k_1(): #Testing what will happen if k = 1
  s = "ATGTCTGTCTGAA" #The string. 
  k = 1 #the value for k
  CORRECT = { 
    'A': {'A'},
    'T': {'G', 'A'},
    'G': {'A'},
    'C': {'T', 'G', 'A'}
  } #The expected outcome
  assert get_geno_strings(s, k) == CORRECT #If the outcome matches the expected outcome, this will pass. 

