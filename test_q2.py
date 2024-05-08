 #!/usr/bin/env python3


from exam4_q2 import get_geno_strings, all_substrings
import pytest

def test_k_zero_pt2():
  file = "sample.txt"
  k = 0
  CORRECT = {}
  assert all_substrings(file, k) == CORRECT
  
def test_empty_file():
  file = "empty.txt"
  k = 3
  all_substrings(file, k)
  CORRECT = {}
  assert all_substrings(file, k) == CORRECT

def test_missing_file():
  with pytest.raises(FileNotFoundError):
    file = "missing"
    k = 4
    all_substrings(file, k)
