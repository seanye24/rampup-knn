#!/bin/bash

echo "number of index vectors: 10"
echo "number of query vectors: 5"
echo "k: 4"
for i in {3..20}; do
  ./generate-input.sh 10 5 $((2 ** i))
  echo -n "dimensions: $((2 ** i)), "
  python ../main.py ../csv/index.csv ../csv/query.csv l2 4 ../csv/output.csv --verbose
  echo
done
