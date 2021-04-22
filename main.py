g = lambda n:n**3
print (g(2))

e = lambda x: "Even" if x%2==0 else "Odd"
print(e(10))
print(e(9))


def average(x,y):
  h = lambda x, y: x * y / 2
  print(h(10,20))

average(10,20)

class Course: 
  def __init__(self, name, rating):
    self.name = name
    self.rating = rating

  def average(self):
    numberInList =  len(self.rating)
    average = sum(self.rating)/numberInList
    print("The average of ",self.name, "is: " , average)

c1 = Course("Domain Specific Language", [9,7,5,3])
# print(c1.name)
# print(c1.rating)
c1.average()

c2 = Course("C++", [5,6,1,3,7,7,5,3])
# print(c2.name)
# print(c2.rating)
c2.average()
