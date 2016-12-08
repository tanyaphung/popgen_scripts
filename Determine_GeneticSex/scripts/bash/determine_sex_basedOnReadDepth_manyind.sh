#!/bin/bash

infile="/u/project/klohmuel/tanya_data/Canines_Project_Data/Canines_Sample_Info/Dogs_SampleName_small"

declare -a NameArray

while IFS='' read -r line || [[ -n "$line" ]]; do NameArray+=("$line"); done < $infile

for i in "${NameArray[@]}"
do
./determine_sex_basedOnReadDepth_1ind.sh $i /u/project/klohmuel/share_folder/bams_for_diego/canines_bams/Dog/11_${i}_SORTED_mergednodupmaptrim.bam /u/home/p/phung428/tanya_data_storage/Canines_Project_Data/GeneticsSex_Info /u/home/p/phung428/share_storage/share_folder/bams_for_diego/canines_bams/Dog
done
