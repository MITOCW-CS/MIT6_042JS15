"""
    MIT6_042JS15: Mathematics for Computer Science
    Simple set operators
"""

class Set(object):

    def __init__(self):
        """
        Initiate empty set
        """
        self.set = []

    def insert(self, e):
        """
        if set don't have value e do insert item e in set
        else cause exception
        """
        if e not in self.set:
            self.set.append(e)

    def remove(self, e):
        """
        If element e in set remove it
        """
        try:
            self.set.remove(e)
        except ValueError:
            print('Error ', e, 'not found!')

    def union(self, other):
        """
        Union elements of two sets
        """
        for e in other.set:
            self.insert(e)

    def intersect(self, other):
        """
        Intersect elements of two sets
        """
        # print('DEBUG SELF = ', self.set)
        # print('DEBUG OTHER = ', self.set)
        for e in self.set:
            if e in other.set:
                print(e, end=' ')

    def __sub__(self, other):
        for e in self.set:
            if e not in other.set:
                self.remove(e)
    def __str__(self):
        return str(self.set)

    def __eq__(self, other):
        return self.set == other.set


mSet1 = Set()
mSet1.insert(1)
mSet1.insert(3)
mSet2 = Set()
mSet2.insert(2)
mSet2.insert(1)
mSet2.insert(3)

print('set1 = ', mSet1)
print('set2 = ', mSet2)
print(mSet2 - mSet1)
print(' --------------- ')
print('intersection s1 and s2:', end=' ')
mSet1.intersect(mSet2)
print()
print('union set1 and set2: ', end=' ')
mSet1.union(mSet2)
print(mSet1)
