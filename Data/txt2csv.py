# Navio2 .TXT to .CSV 
# Date Created: 12/28/2019
# Created by Paul Klappa
'''
Important: 
    Used with the Navio2 flight controller for the Parachute and Aerial 
    Vehicles (PAVS) lab at the University of Missouri - Kansas City
'''
import os
import pandas as pd

# Global Variables
comb_list = []

def main():
    print("Starting Main...")
    for file in os.listdir("/Users/Paul/Desktop/Injection_p2/paulData/"):
        if file.endswith(".txt"):
            
            # Grab the 'about' data of each file (First row)
            a = list(pd.read_csv(file, header = 0, sep = ' '))
            about = ' '.join(a) # Combine about list
    
            # Grab headers from Navio2 .txt files
            h = list(pd.read_csv(file, skiprows = 1, delim_whitespace = True))

            # Use h as column headers and then skip rows 1 and 2
            temp = pd.read_csv(file, sep = ',', names = h, skiprows = [0,1]) 

            # Final file push
            name = file
            csvfile = name.replace('.txt','.csv')
            temp.to_csv(csvfile)        
            
            # Create an output README file that displays every file and the tags
            # associated with it (time and location)   
            combine = name + ': ' + about + '; ' # Combined About section with file name
            comb_list.append(combine)
            #print('iteration {}'.format(len(comb_list)))
            
    # Writes one list
            with open("README.txt", mode ="a") as text_file:
                    text_file.write(combine + '\n')
    
if __name__== "__main__":
    main()