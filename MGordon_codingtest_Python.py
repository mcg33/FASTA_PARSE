print("Matthew Gordon coding test (Python) \n") 

#============================================ Task 1 ===================================================
# genelist.txt info to subset the GeneCounts info
print("Task 1 - DONE, subset genes in both files")

Genelist_data = open("genelist.txt")
Genelist_lines = Genelist_data.readlines()

print("GeneList information: DONE" + "\n")
for line in Genelist_lines:
    line = line.rstrip("\n") #Removes space between the columns 
    line = line.split("\t") # Splits elements using the tab    
    Gene_list_ID = line[0]  
    #print(Gene_list_ID) 

print("\n" + "GeneCount information: DONE" + "\n")
Genecount_data = open("GeneCounts.txt")
Genecount_lines = Genecount_data.readlines()

for lines in Genecount_lines:
    lines = lines.split("\t")
    del lines[1:]
    Gene_count_ID = lines[0]
    #print(Gene_count_ID)

Ans1 = [x for x in lines if x not in line]
Ans2 = [x for x in line if x not in lines]
print("In GeneCount but not Genelist - " + str(Ans1))
print("In Genelist but not GeneCount - " + str(Ans2))

#============================================ Task 2 ==================================================
#Removing all genes that have 0 counts for all samples
print("\n" + "Task 2 - Remove all genes with no counts in any sample " + "\n")

Genecount_data = open("GeneCounts.txt")
Genecount_lines = Genecount_data.readlines()[1:]

total_genes = 0
relevant_count = 0
for lines in Genecount_lines:
    lines = lines.rstrip("\n")
    lines = lines.split("\t")
    gene_ID = lines[0]
    sample_score = lines[1:]
    sample_score = list(map(int, sample_score))
    total = 0
    for ele in range(0, len(sample_score)):
        total = total + sample_score[ele]
    if total > 0:
        print(gene_ID)
        print("Total sample score: ", total)
        relevant_count += 1

    total_genes += 1

print("Total genes: " + str(total_genes))
print("Present genes ", relevant_count)
presence_percentage =(relevant_count/total_genes)*100
print("\n" + "Gene prescence: ", presence_percentage, "%")
