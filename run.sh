#!/bin/bash

curdir=$PWD
inputdir="./input/complaints.csv"
outputdir="./output/report.csv" 
#echo $inputdir $outputdir
python ./src/consumer_complaints.py $inputdir $outputdir
   
