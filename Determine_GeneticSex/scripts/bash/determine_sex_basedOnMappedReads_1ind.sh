#!/bin/bash

usage()
{
echo 'The goal of this script is to take a bam file and to output whether the individual is a male or a female based on read depth.
Here is how to use the script:
./determine_sex_basedOnReadDepth.sh Name BamFile OutputDir BamDir'
exit
}
if [ "$#" -le 1 ]
then
  usage
fi

inputDogID=$1
inputFile=$2
outputDir=$3
bamDir=$4

cd $bamDir
samtools idxstats $inputFile > $outputDir/${inputDogID}_chromDepths.txt

grep chrX $outputDir/${inputDogID}_chromDepths.txt > $outputDir/${inputDogID}_chrX_chromDepths.txt

for i in {01..38}
do
grep chr${i} $outputDir/${inputDogID}_chromDepths.txt >> ${outputDir}/${inputDogID}_autosomes_chromDepths.txt

done

Rscript /u/project/klohmuel/tanya_data/popgen_scripts/Determine_GeneticSex/scripts/R/compute_meanMappedReads.R  ${outputDir}/${inputDogID}_chrX_chromDepths.txt ${outputDir}/${inputDogID}_autosomes_chromDepths.txt > ${outputDir}/${inputDogID}_GeneticSexInfo.txt
