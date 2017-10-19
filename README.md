# Population Genetics Scripts
This repository contains scripts that I often use when analyzing data (mainly for population genetics purposes). 

# compute_diversity
* This directory contains scripts used to compute genetic diversity (defined as average pairwise differences) in each window of the genome. 
* The main script is `main_compute_diversity.py`. Usage is:
```
python main_compute_diversity.py -h                     
usage: main_compute_diversity.py [-h] --windows_bed WINDOWS_BED --targets_bed
                                 TARGETS_BED --variants VARIANTS --numAllele
                                 NUMALLELE --outfile OUTFILE

This script computes pairwise diversity.

optional arguments:
  -h, --help            show this help message and exit
  --windows_bed WINDOWS_BED
                        REQUIRED. BED file for Xkb window.
  --targets_bed TARGETS_BED
                        REQUIRED. BED file specifying the regions to be
                        partitioned into Xkb window. For example, give the
                        path for the bed file where regions represent neutral
                        region
  --variants VARIANTS   REQUIRED. Variant file. The format should be CHROM POS
                        ind1 ind2 etc. Should be tab delimit. Because of VCF
                        format, it is 1-based
  --numAllele NUMALLELE
                        REQUIRED. Indicate the number of alleles, which is
                        equal to the number of individuals in your sample
                        times 2.
  --outfile OUTFILE     REQUIRED. Name of output file.
```
* Several notes:
1. The target bed file should represent the region that includes both variant and invariant sites. For instance, let's consider a 100kb window. If this is a simulation, then you should expect all 100,000 sites to be sequenced. However, in reality, not every site in this 100kb window is callable. Therefoere, before computing diversity, one should already determine the regions of the genome that are callable. 
2. For the variant file, note that this is not a VCF file. One should use tools such as VCFtool to extract out the GT information for each individual. Alternatively, one can rewrite this part so that the script also accept the VCF format. However, I found that the script runs faster this way. 
3. In the `compute_AF.py` script, note that my genotypes are not phased (represented by a dash such as 0/0). If your genotypes are phased (represented by a pipe such as 0|0), then you should change this script. 
