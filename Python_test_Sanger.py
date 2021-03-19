print("Sanger coding test \n")

import re
import Bio
from Bio import SeqIO

#=============== Part 1 ===============
#Check each of the 3 files has 4 lines - Is a proper FASTQ
#FASTQ quality determination function
print("Part 1: DONE")

def realFASTQ(fastq_open):
    read_fastq = fastq_open.readlines()
    size = len(read_fastq)
    
    line_count = 0
    for line in read_fastq:
        if re.search("@HS32_14736*", str(line)):
            line_count +=1

    if (size/line_count ==4):
        checkStatement = "TRUE"
    else:
        checkStatement = "FALSE"
    
    return("Total number of record lines: " + str(size) + "\n" + "Quality assured: " + checkStatement)

#example_1.fastq

with open("example_1.fastq") as fastq:
    ex1_check = realFASTQ(fastq)
    print("example_1.fastq: ")
    print(ex1_check)

#example_2.fastq

with open("example_2.fastq") as fastq:
    ex2_check = realFASTQ(fastq)
    print("example_2.fastq: ")
    print(ex2_check)

#example_t.fastq

with open("example_t.fastq") as fastq:
    ext_check = realFASTQ(fastq)
    print("example_t.fastq: ")
    print(ext_check)

#=============== Part 2 ===============
print("\n")
print("Part 2: DONE-ish, pretty sure this works not 100%")
# Find the frequency of individual barcodes from example_t in example_1 & example_2

def barcode_freq(fastq_ex1, fastq_ex2, fastq_ext):
    record_ex1 = list(SeqIO.parse(fastq_ex1, "fastq"))             
    read_fastq_ext = fastq_ext.readlines()

    Seq_count = 0
    Bar_count = 1
    Bar_occurance = 0
    
    while Seq_count in range(0,10):
        print("Sequence number: " + str(Seq_count + 1)) 
        ex1_seq = str(record_ex1[Seq_count].seq)
        ext_seq = read_fastq_ext[Bar_count]
        ext_seq = str(ext_seq)
        print("example_1 sequence: ", ex1_seq)
        print("example_t barcode: ", ext_seq)
        Bar_match = ex1_seq.count(ext_seq)
        print("Barcode matches: " + str(Bar_match) + "\n")
        if Bar_match > 0:
            Bar_occurance += 1  
        Seq_count +=1
        Bar_count +=4
   

    Answer = "Number of barcoded samples: " + str(Bar_occurance)      

    return(Answer)

#Using example files
with open("example_1.fastq") as fastq_ex1, open("example_2.fastq") as fastq_ex2, open("example_t.fastq") as fastq_ext:
    equal = barcode_freq(fastq_ex1, fastq_ex2, fastq_ext)
    print(equal)

#=============== Part 3 ===============
print("\n")
print("Part 3: DONE - Still need to learn how to parse 2 simulatneous FASTQ's using Biopython" + "\n")
# Lane1.tag Alter FASTQ identifiers adding "#" before "/" for both example_1 & example_t

def ID_change(fastq_ex1, fastq_ext):
    record_ex1 = list(SeqIO.parse(fastq_ex1, "fastq"))
    record_ext = fastq_ext.readlines()             
    
    # Adding for example_1
    print("example_1 altered: " + "\n")
    rec_num = 0
    hash_num = 1  
    while rec_num in range(0,10):
        record_ID = str(record_ex1[rec_num].id)
        record_ID = record_ID[:-2] + "#" + str(hash_num) + record_ID[-2:]
        print(record_ID)          
        hash_num += 1
        rec_num += 1
    print("\n")

    # Adding for example_t - could integrate once done
    print("example_t altered: " + "\n")    
    ext_ID_count = 0
    hash_num_2 = 1
    for line in record_ext:
        line = line.rsplit("\t")
        while ext_ID_count in range(0,38):
            ext_ID = record_ext[ext_ID_count]
            ext_ID = ext_ID[1:]
            ext_ID = ext_ID[:-3] + "#" + str(hash_num_2) + ext_ID[-3:]  
            ext_ID = str(ext_ID)
            print(ext_ID)
            ext_ID_count += 4 
            hash_num_2 += 1   


with open("example_1.fastq") as fastq_ex1, open("example_t.fastq") as fastq_ext:
    new_ID = ID_change(fastq_ex1,  fastq_ext)
    print(new_ID)

#=============== Part 4 ===============
# Extra Q: Do this but allow for single base error in indexing the sequence
