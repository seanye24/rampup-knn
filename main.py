import argparse
import csv
import sys
import timeit

start_time = timeit.default_timer()

def l2(p, q):
    ''' Takes two vectors, and calculates their distance in l2 space '''
    return sum(((pi - qi)**2 for pi, qi in zip(p, q)))**0.5


class Index:
    '''Indexes a query vector among a set of index vectors.

    Attributes:
        search: Calculates the `k` nearest vectors to the query vector given a vector space
    '''
    def __init__(self, index_vectors):
        '''Initializes the index vectors. '''
        self.__index_vectors = index_vectors

    def search(self, query_vector, k, space):
        '''Returns the k-nearest neighbors of the query_vector.
        Args:
            query_vector: Vector to query the index_vectors against.
            k: Number of nearest neighbors.
            space: Vector space which specificies the distance function.
        '''
        spaces = {'l2': l2}
        space_f = spaces[space]
        results = [(i, space_f(iv, query_vector))
                   for i, iv in enumerate(self.__index_vectors)]

        # select the k-nearest vectors
        nearest_vectors = []
        min_i, min_dist = results[0]
        for _ in range(k):
            for i, dist in results:
                if not (i in nearest_vectors) and dist < min_dist:
                    min_i, min_dist = i, dist
            nearest_vectors.append(min_i)
            min_dist = sys.maxsize
        return nearest_vectors


class IOReader:
    '''Reads data from csv and return list of vectors'''
    def read_query(self, csv_path):
        with open(csv_path, newline='') as csvfile:
            vector_reader = csv.reader(csvfile)
            index_vectors = [tuple([float(i) for i in vector]) for vector in vector_reader]
            return index_vectors

    '''Reads data from csv and creates an Index'''

    def read_index(self, csv_path):
        return Index(self.read_query(csv_path))


class IOWriter:
    '''Reads results and outputs it to a csv'''
    def write_results(self, csv_path, results):
        with open(csv_path, 'w', newline='') as csvfile:
            vector_writer = csv.writer(csvfile)
            vector_writer.writerows(results)


# parse command line args
parser = argparse.ArgumentParser(description='Process command line arguments.')
parser.add_argument('index_path')
parser.add_argument('query_path')
parser.add_argument('space')
parser.add_argument('k', type=int)
parser.add_argument('results_path')
parser.add_argument('--verbose', action='store_true')
args = vars(parser.parse_args())

# convert args to python objects
reader = IOReader()
index_path = args['index_path']
query_path = args['query_path']
index_vectors = reader.read_index(index_path)
query_vectors = reader.read_query(query_path)
space = args['space']
k = args['k']
results_path = args['results_path']
is_verbose = args['verbose']

# write results to file
results = [index_vectors.search(q, k, space) for q in query_vectors]
writer = IOWriter()
writer.write_results(results_path, results)

end_time = timeit.default_timer()
time_elapsed = end_time - start_time
if is_verbose:
    print('time_elapsed: ', time_elapsed)
