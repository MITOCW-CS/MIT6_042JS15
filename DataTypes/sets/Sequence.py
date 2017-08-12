"""
    Sequence implementation by Python
"""


class Sequence(object):

    def __init__(self, seq):
        self.seq = seq

    def insert(self, v):
        self.seq.append(v)

    def remove(self, v):
        try:
            self.seq.remove(v)
        except ValueError:
            print('Error: ', v, 'not found!')

    def find(self, v):
        return v in self.seq

    def union(self, other):
        for e in other.seq:
            self.seq.append(e)
        return Sequence(self.seq)

    def intersection(self, other):
        se = Sequence([])
        for e in self.seq:
            if e in other.seq:
                se.seq.append(e)
        return se

    def __str__(self):
        s = ''
        for e in self.seq:
            s += str(e) + ' '
        return s


seq1 = Sequence([])
seq1.insert(0)
seq1.insert(2)
seq1.insert(-9)
seq1.insert(-12)
print('Sequence 1: ', seq1)

seq2 = Sequence([])
seq2.insert(-32)
seq2.insert(0)
seq2.insert(-9)
seq2.insert(23)
seq2.remove(-1)
print('Sequence 2: ', seq2)

print()
print('Seq 1 intersect Seq 2: ', seq1.intersection(seq2))
print('Seq 1 unite Seq 2: ', seq1.union(seq2))