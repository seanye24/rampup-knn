#!/bin/bash

echo "number of query vectors: 5"
echo "dimensions: 5"
echo "k: 4"
for i in {3..20}; do
  sh ./generate-input.sh $((2 ** i)) 5 5
  echo -n "number of index vectors: $((2 ** i)), "
  python main.py index.csv query.csv l2 4 output.csv
  echo
done
