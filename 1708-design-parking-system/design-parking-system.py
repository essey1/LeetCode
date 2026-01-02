class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.lot[0] != 0:
                self.lot[0] -= 1
                return True
            return False
        elif carType == 2:
            if self.lot[1] != 0:
                self.lot[1] -= 1
                return True
            return False
        elif carType == 3:
            if self.lot[2] != 0:
                self.lot[2] -= 1
                return True
            return False
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)