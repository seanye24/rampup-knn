#!/bin/bash

num_index=$1
num_query=$2
dimensions=$3

rm -rf index.csv query.csv
cd ..
python3 generate.py $num_index $dimensions > csv/index.csv
python3 generate.py $num_query $dimensions > csv/query.csv
