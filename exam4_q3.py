#!/usr/bin/env python3


import sys #This lets us type arguments on the command line and have it be used in the code 

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

def all_substrings(file, k): #new function using the old function for any file
  """
  This function uses the first function (get_geno_strings) to read sequences from a file to identify all possible substrings and their subsequent substrings for each sequence.
  
  Arguments:
    file (filename/path to filename (string)) : The path to the file to read the sequences from. 
    k (int): The size of the kmers being analyzed
    
  Returns:
    new_substrings: The new unique substrings and their subsequent substrings from the file. 
  """
  
  new_substrings={} #makes a dictionary of all the new functions
  with open(file, 'r') as file: #When the file (argument ) is put in, opened, and read it will loop through every line in the file
    for line in file: #the looping through every line in the file part. 
      s = line.strip() #takes away any blank spaces or extra characters that aren't the sequence
      unique_substring = get_geno_string(s, k) #the previous output from the first function
      new_substrings[s] = unique_substring #Adding the two together so new substrings has all of the unique substrings as well. 
    
  return (new_substrings) #This will give us only the unique kmer substrings and all possible unique subsequent substrings


def find_smallest_k(file):
  
    """
    This function finds the smallest value for k where each substring only has one possibility for subsequent substrings.

    Argument:
    file (filename/ path to file (string)): The path to the file to read the sequences from.

    Returns:
    k (int): The smallest value of k where k is the size of the kmer. 
    """
    
    # Start with k=1 and increase by one until all of the substrings only have one subsequent substring possible. 
    k = 1 #starting with the lowest kmer possible, k=1
    while True: #This makes the loop continue until something that fits the parameters is returned. 
        new_substrings = all_substrings(file, k) #This is looking through the previous function. 
        uniq_subseq_counts = [len(substrings) for substrings in new_substrings.values()] #This looks through the dictionary created earlier for throughout the length of substrings for substrings and finds the subsequent substrings and makes it into a list. 
        if min(uniq_subseq_counts) == 1: #This tests to see if the minimum value in the list is equal to one. 
            return k #gives us the smallest value of k back if
        k += 1 #The loop continues if there isn't one possible subsequent substring until it is possible

if __name__ == "__main__": #The overall command that lets us use the command line. 
  file = (sys.argv[2]) #The argument for file that we can put on the command line.
  k = (int(sys.argv[1])) #The argument for k that we can put on the command line.
  new_substrings = all_substrings(file, k) #defines new_substrings
  smallest_k = find_smallest_k(file) #defines smallest_k
  print (smallest_k) #prints the smallest number for k

#The answer to question 7 is k=1 
