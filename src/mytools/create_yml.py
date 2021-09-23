import sys
import os
import re
import fnmatch
from zipfile import ZipFile

SAMPLE_NAME = sys.argv[1]
zipf = sys.argv[2]
yaml = sys.argv[3]


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def sample_exist(path):
    fYAML = open(path, "rt")
    for line in fYAML:
        if SAMPLE_NAME in line:
            return True

def append_YAML(path, sorted_list_contigs):
    fYAML = open(path, "a+")
    fYAML.write(SAMPLE_NAME + ":\n")
    pattern = "*.sam"
    for file in sorted_list_contigs:
        if fnmatch.fnmatch(file, pattern):
            contig_fsam = file
            contig_name, ref = contig_fsam.split("_")
            contig, contig_nr = contig_name.split("Contig")
            fYAML.write("    - " + str(contig_nr) + "\n")
    fYAML.close()

# Creates YAML environment for all contigs per sample

#path_to_sam_dir = zipf
with ZipFile(zipf, 'r') as myzip:
    list_contigs = myzip.namelist()
    sorted_list_contigs = natural_sort(list_contigs)

path_to_contig_env = yaml
if not sample_exist(path_to_contig_env):
    append_YAML(path_to_contig_env, sorted_list_contigs)
