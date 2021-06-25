#!/bin/bash

num_index=$1
num_query=$2
dimensions=$3

rm -rf index.csv query.csv
python generate.py $num_index $dimensions > index.csv
python generate.py $num_query $dimensions > query.csv
