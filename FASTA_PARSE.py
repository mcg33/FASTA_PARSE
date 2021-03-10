from Bio import SeqIO
print('FASTA file paser program')

#Show FASTA sequence ID - Method I
for record in SeqIO.parse("Ubiquitin_C.fasta", "fasta"):
    print(record.id)

#Show FASTA sequence ID - Method II
with open("Ubiquitin_C.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)

#List makes multi-FASTA files readable
records = list(SeqIO.parse("Ubiquitin_multi.fasta", "fasta"))
print(records[0].id) #First record ID
print(records[1].id) #Second record ID

#Writing records to a file
First_seq = records[0]
Second_seq = records[1]
SeqIO.write(First_seq, "Ubiquitin_seq_1.fasta", "fasta")
print("First FASTA sequence saved as: Ubiquitin_seq.fasta")
SeqIO.write(Second_seq, "Ubiquitin_seq_2.fasta", "fasta")
print("Second FASTA sequence saved as: Ubiquitin_seq.fasta")

#Index records by identifier
record_dict = SeqIO.index("Ubiquitin_multi.fasta", "fasta")
print(record_dict["sp|P0CG48|UBC_HUMAN"])  #Gives name, ID, Desc, Seq