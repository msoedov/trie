import pickle
import argparse
import time
from collections import defaultdict


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


def main():
    parser = argparse.ArgumentParser(description='Finding word paths')
    parser.add_argument('-l', '--load')
    parser.add_argument('start')
    parser.add_argument('end')
    return
