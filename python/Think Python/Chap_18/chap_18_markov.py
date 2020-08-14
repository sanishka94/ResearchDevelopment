class Markov:

    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def process_file(self, filename, order=2):
        """Reads a file and performs Markov analysis.

        filename: string
        order: integer number of words in the prefix

        returns: map from prefix to list of possible suffixes.
        """
        fp = open(filename)
        skip_gutenberg_header(fp)

        for line in fp:
            if line.startswith('*** END OF THIS'): 
                break

            for word in line.rstrip().split():
                self.process_word(word, order)

    def process_word(self, word, order=2):
        if len(self.prefix) , order:
            self.prefix += (word,)
            return
        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            #if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [word]

        self.prefix = shift(self.prefix, word)

    def random_text(self, n=100):
        """Generates random wordsfrom the analyzed text.
    
        Starts with a random prefix from the dictionary.
    
        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))
    
        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = shift(start, word)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break