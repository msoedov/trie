import argparse
import logging
import pickle
import sys
import time
from collections import defaultdict

log = logging.getLogger(__name__)

word_group = [set() for _ in range(30)]
graph = defaultdict(set)


def differs_by_one(first, seccond):
    """
    Checks whether the Hamming distance between two words is exactly 1
    >>> differs_by_one('word', 'wird')
    True
    >>> differs_by_one('word', 'wiud')
    False
    >>> differs_by_one('one', 'another')
    False
    """
    if len(first) != len(seccond):
        return False

    one = False
    for ch1, ch2 in zip(first, seccond):
        if ch1 != ch2:
            if one:
                return False
            else:
                one = True
    return one


def build_graph():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().split('\n')

    # Groups by word len
    word_group = [set() for _ in range(30)]

    for w in words:
        word_group[len(w)].add(w)

    graph = defaultdict(set)
    for group in word_group:
        for w in group:
            for v in group:
                if differs_by_one(w, v):
                    graph[w].add(v)
    pickle.dump(graph, open('graph.pcl', 'wb'))
    return graph


def load_graph():
    return pickle.load(open('graph.pcl', 'rb'))


def bfs(graph, start, goal):
    def bfs_paths(graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))
    return list(bfs_paths(graph, start, goal))


def get_cli_parser():
    """
    Returns command line argument parser
    # It should return Namespace object when all arguments are passed
    >>> get_cli_parser().parse_known_args(['bitt', 'meum', '-r', '-d'])[0]
    Namespace(debug=True, end='meum', rebuild=True, start='bitt')
    """
    parser = argparse.ArgumentParser(description='Solve word paths problem', version='0.1')
    parser.add_argument('start', help='Start word')
    parser.add_argument('end', help='End word')
    parser.add_argument('-r', '--rebuild',
                        help='Load and rebuild word graph(can take a while)', action='store_true')
    parser.add_argument('-d', '--debug',
                        help='Turn on debug stderr logger', action="store_true")
    return parser


if __name__ == '__main__':
    args = get_cli_parser().parse_args()
    if args.debug:
        log.setLevel(logging.DEBUG)
        log.addHandler(logging.StreamHandler(sys.stdout))
    ts = time.time()
    graph = load_graph()
    log.debug('Loaded in %s', time.time() - ts)
    paths = bfs(graph, args.start, args.end)
    log.debug('Here we go: %s', paths)
