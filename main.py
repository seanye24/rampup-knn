import csv

def l2(p, q):
    ''' Takes two vectors, and calculates their distance in l2 space '''
    return sum(((pi - qi) ** 2 for pi, qi in zip(p, q))) ** 0.5

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
        results = [(iv, space_f(iv, query_vector)) for iv in self.__index_vectors]

        # select the k-nearest vectors
        nearest_vectors = []
        for _ in range(k):
            min_vector, min_vector_dist = results[0]
            for iv, iv_dist in results:
                if not iv in nearest_vectors and iv_dist < min_vector_dist:
                    min_vector, min_vector_dist = iv, iv_dist
            nearest_vectors.append(min_vector)
        return nearest_vectors

class IOReader:
    '''Reads data from csv and creates an Index'''

    def read_index(self, csv_path):
        with open(csv_path, newline='') as csvfile:
            vector_reader = csv.reader(csvfile)
            index_vectors = [tuple(vector) for vector in vector_reader]
            return Index(index_vectors)
