# extract_contigs_YASRA.py
# This script is to extract contigs and to create SAM files with headers for each of them after running YASRA.
# YASRA creates a SAM file without header after alignments.
# This can be executed by running: $ python extract_contigs_YASRA.py [SAMPLE_NAME], for example:
# $ python extract_contigs_YASRA.py SRR8528336
# Made by: Elfy Ly
# Date: 7 May 2020

import sys
import os
import re
import fnmatch
from zipfile import ZipFile

SAMPLE_NAME = sys.argv[1]
path_to_YASRA_fSAM = sys.argv[2]
path_to_final_assembly = sys.argv[3]
mapped_contigs = sys.argv[4]
samfiles = sys.argv[5]
num_rc= sys.argv[6]


N_TABS = 10

# creates a list of mapped contigs and their start and end position
def create_mapped_contig_list(path_to_final_assembly, path_to_mapped_contigs):
    f = open(path_to_mapped_contigs, "w+")
    print("New text file created: contig_files.txt")

    with open(path_to_final_assembly, 'rt') as myfile:
        for myline in myfile:
            if myline.startswith('>'):
                contig_name, ref_name, contig_start, contig_end = myline.split('_')
                symbol, contig_name = contig_name.split('>')
                f.write(contig_name + "\t" + contig_start + "\t" + contig_end)
    f.close()

def create_new_fSAM(contig_number, reference_genome, contig, contig_length, myline):
    f = open(contig_number + "_" + reference_genome + ".sam", "w+")
    print("New text file created: " + contig_number + "_" + reference_genome)
    f.write("@HD\tVN:1.3\n@SQ\tSN:" + contig + "\tLN:" + str(contig_length) + "\n" + myline)
    f.close()

def write_to_fSAM(contig_number, reference_genome, myline):
    f = open(contig_number + "_" + reference_genome + ".sam", "a+")
    f.write(myline)
    f.close()  

def count_save_stats(nreads, ncontigs):
    f = open(num_rc, "w+")
    f.write("Number of reads: " + str(nreads) + "\nNumber of contigs: " + str(ncontigs) + "\n")
    f.close()

'''Code starts here'''

# Creates assembled contig list and dictionary for start and end position
path_to_fmapped_contigs = mapped_contigs #Menco

create_mapped_contig_list(path_to_final_assembly, path_to_fmapped_contigs)

# write new SAM files for every contig after YASRA
nreads = 0
ncontigs = 0
contig_name_temporary = " "
files = []
with open(path_to_YASRA_fSAM, 'rt') as myfile:
    for myline in myfile:
        if myline.startswith('>'):
            # checkt of er nog een '>' in line zit
            ntabs = 0
            for char in myline:
                if char == "\t":
                    ntabs += 1
            if ntabs == N_TABS:
                nreads += 1
                qname, flag, contig, pos, mapq, cigar, rnext, pnext, tlen, read, phred = myline.split("\t")

                contig_number, reference_genome, contig_start, contig_end = contig.split("_")
                contig_length = int(contig_end) - int(contig_start) + 1

                if contig != contig_name_temporary:
                    create_new_fSAM(contig_number, reference_genome, contig, contig_length, myline)
                    h = str(contig_number) + "_" + reference_genome + ".sam"
                    files.append(h)
                    ncontigs +=1
                    contig_name_temporary = contig
                elif contig == contig_name_temporary:
                    write_to_fSAM(contig_number, reference_genome, myline)                 

    count_save_stats(nreads, ncontigs)
with ZipFile(samfiles, "w") as myzip:
    for name in files:
        myzip.write(name)
    myzip.close()

