#!/usr/bin/env python3 

import sys #This lets us type arguments on the command line and have it be used in the code 

def all_substrings(file, k): #new function using the old function for any file
  new_substrings={} #makes a dictionary of all the new functions
  with open(file, 'r') as file: #unsure about this part
    for line in file:
      s = line.strip() #takes away any blank spaces or extra characters that aren't the sequence
      unique_substring = get_geno_string(s, k)
      new_substrings[s] = unique_substring
    
  return (new_substrings)

def get_geno_string(s, k): #Defining the function and its set of arguments
  
  """
  This function gives the unique genetic string where it will identify all substrings of size k, and all unique possible subsequent substrings of each substring.
  
  Arguments
  s (string): the sequence that is used to find all substrings
  k (int): the size of the kmer that is going to be analyzed
  
  Return
  unique_substring : the list of unique substrings and all subsequent substrings that are possible from the sequence
  """
  unique_substring = {} #This is allowing the code to make a dictionary of substrings
  for i in range (len(s)-(k-1)): #This loops through the length of "s" all the way to the end
    substring = s[i:i+k] #This is the set that says that we want all kmers of the length i to i+k of k length
    subseqsubstring = set()#This creates a set where it adds all the subsequent unique substrings to this set
    
    for j in range(i +1, len(s) -(k-1)): #This loops through the list of substrings we have through s to the end
      subseqsubstring.add(s[j:j+k]) #This says we want all kmers after the first kmer of length j to j+k of k length
      
      unique_substring[substring] = subseqsubstring #This takes each substring that was found and all of the unique substrings after it and makes sure they're combined to put in the dictionary as one whole substring so when you ask for one substring you can get that substring and all the possible unique ones after
  
  return unique_substring #This will give us only the unique kmer substrings and all possible unique subsequent substrings


if __name__ == "__main__": #The overall command that lets us use the command line. 
  file = (sys.argv[2])
  k = (int(sys.argv[1])) #The argument for k that we can put on the command line
  new_substrings = all_substrings(file, k) #defines new_substrings
  print (new_substrings) #prints the new_substrings

