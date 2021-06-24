"""
Generate random datasets
 
(Use python 3)
python3 data_generator.py <number_of_vectors> <dimension> > x.csv
 
"""
 
import argparse
import random
 
 
def generate_random_vectors(num_vectors, dim):
    for _ in range(num_vectors):
        v = [str(random.uniform(0, 10_000)) for _ in range(dim)]
        print(",".join(v))
 
 
def main():
    parser = argparse.ArgumentParser(description='Create random dataset')
    parser.add_argument('num_vectors', type=int, help='number of vectors to generate')
    parser.add_argument('dim', type=int, help='dimension of vectors')
    args = parser.parse_args()
 
    num_vectors = args.num_vectors
    dim = args.dim
 
    generate_random_vectors(num_vectors, dim)
 
 
if __name__ == '__main__':
    main()
