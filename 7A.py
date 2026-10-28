class Stud:
    m1 = int(input("Enter the mark1: "))
    m2 = int(input("Enter the mark2: "))
    m3 = int(input("Enter the mark3: "))
    m4 = int(input("Enter the mark4: "))
    m5 = int(input("Enter the mark5: "))

    Tot = m1 + m2 + m3 + m4 + m5
    avg = Tot / 5

    def firstgrade(self):
        if self.avg >= 90 and self.avg <=100:
            print("1st Grade")
        elif self.avg >= 75 and self.avg <= 89:
            print("2n Grade:")
        elif self.avg >= 60 and self.avg <= 75:
            print("3rd Grade")
        elif self.avg >= 50 and self.avg <= 60:
            print("4th Grade")
        else:
            print("5th Grade")


s = Stud()
s.firstgrade()
