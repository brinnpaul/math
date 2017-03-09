import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        d = self.dimension
        new_coor = [self.coordinates[j]+v.coordinates[j] for j in range(0,d)]
        self.coordinates = tuple(new_coor)
        return self.coordinates

    def subtract(self, v):
        d = self.dimension
        new_coor = [self.coordinates[j]-v.coordinates[j] for j in range(0,d)]
        self.coordinates = tuple(new_coor)
        return self.coordinates

    def multiply(self, v):
        d = self.dimension
        new_coor = [self.coordinates[j]*v for j in range(0,d)]
        self.coordinates = tuple(new_coor)
        return self.coordinates

    @staticmethod
    def multi(v, scalar):
        d = v.dimension
        new_coor = [v.coordinates[j]*scalar for j in range(0,d)]
        return tuple(new_coor)

    def magnitude(self):
        d = self.dimension
        count = 0
        for j in range(0,d):
            count += self.coordinates[j]**2
        return count**0.5

    @staticmethod
    def mag(v):
        d = v.dimension
        count = 0
        for j in range(0,d):
            count += v.coordinates[j]**2
        return count**0.5

    def normalize(self):
        m = self.magnitude()
        d = self.dimension
        new_coor = [(self.coordinates[j]*(1/m)) for j in range(0,d)]
        return tuple(new_coor)

    @staticmethod
    def norm(v):
        m = v.magnitude()
        d = v.dimension
        new_coor = [(v.coordinates[j]*(1/m)) for j in range(0,d)]
        return tuple(new_coor)


    def dot(self, v):
        count = 0
        d = self.dimension
        for j in range(0,d):
            count += self.coordinates[j]*v.coordinates[j]
        return count

    @staticmethod
    def dot_static(v1, v2):
        count = 0
        d = v1.dimension
        for j in range(0,d):
            count += v1.coordinates[j]*v2.coordinates[j]
        return count

    def inner(self, v):
        dot = self.dot(v)
        return dot/(self.mag(self)*self.mag(v))

    def angle(self, v):
        radians = math.acos(self.inner(v))
        degrees = math.degrees(radians)

        return {'radians':radians, 'degrees':degrees}

    def check_if_parallel(self, v):
        d = self.dimension
        try:
            over = [round(self.coordinates[j]/v.coordinates[j], 3) for j in range(0,d)]
        except ZeroDivisionError:
            print('Trying inverse')
        finally:
            over = [round(v.coordinates[j]/self.coordinates[j], 3) for j in range(0,d)]
        equal = True
        for c in over:
            if c != over[0]:
                equal = False
        return equal

    def check_if_orthagonal(self, v):
        dot = self.dot_static(self, v)
        return round(dot, 3) == 0

    def project(self, v1, v2):




    @staticmethod
    def test_vector(v):
        try:
            if not v.coordinates:
                raise ValueError
        except:
            raise ValueError('Must Use Vector.')

    @staticmethod
    def test_dimension(v1, v2):
        try:
            if v1.dimension != v2.dimension:
                raise ValueError
        except:
            raise ValueError('Vectors must be of same dimension')




v1 = Vector([-7.579,-7.88])
v2 = Vector([22.737, 23.64])

v3 = Vector([-2.029, 9.97, 4.172])
v4 = Vector([-9.231, -6.639, -7.245])

v5 = Vector([-2.328, -7.284, -1.214])
v6 = Vector([-1.821, 1.072, -2.94])

v7 = Vector([2.118, 4.827])
v8 = Vector([0, 0])

print ('V1 on V2')
print (v1.check_if_parallel(v2))
print (v1.check_if_orthagonal(v2))

print ('V3 on V4')
print (v3.check_if_parallel(v4))
print (v3.check_if_orthagonal(v4))

print ('V5 on V6')
print (v5.check_if_parallel(v6))
print (v5.check_if_orthagonal(v6))

print ('V7 on V8')
print (v7.check_if_parallel(v8))
print (v7.check_if_orthagonal(v8))
