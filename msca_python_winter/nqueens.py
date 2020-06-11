class raf_nq:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        return self.solutions

    def put_queen(self, positions, target_row):
        if target_row == self.size:
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                return False
        return True
#am i supposed to make a change to this? because I just did
#borrowing code from previous class
class dog:
    
    def __init__(self, color, breed, name):
        self.color = color
        self.breed = breed
        self.name = name
        self.__distance = 0
        
    def walk(self, distance):
        assert distance > 0, "Dude.. don't be lazy!!"
        self.__distance += distance
    
    def get_distance(self):
        print(self.__distance)
    
    def peemeter(self):
        pee = 1 -  self.__distance/50
        print("Pee Probability is ", pee)