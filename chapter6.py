class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def stateprofession(self):
        print("I have no profession!")
    
    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))
        print("My gender is " + self.gender)
	
    def ismale(self):
        if self.gender == 'male':
            return True
        else: 
            return False
'''       
author = Person("Maarten",30, "female")
author.introduceyourself()
'''

class Teacher(Person): #this class inherits the class above!
    def stateprofession(self):
        print("I am a teacher!")
        
 
''' 
author = Teacher("Maarten",30, "male")
author.introduceyourself()
author.stateprofession() 
'''



class Teacher(Person): #this class inherits the class above!
    def __init__(self, name, age, gender):
        self.courses = [] #initialise a new variable
        super().__init__(name,age, gender) #call the init of Person
        
    def stateprofession(self):
        print("I am a teacher!")        
    
    def introduceyourself(self):
        super().introduceyourself() #call the introduceyourself() of the Person
        self.stateprofession()
        print("I teach " + str(self.nrofcourses()) + " course(s)")
        for course in self.courses:
            print("I teach " + course)
      
        
    
    def addcourse(self, course):
        self.courses.append(course)
        
    def nrofcourses(self):
        return len(self.courses)
    
'''
author = Teacher("Maarten",30, 'male')
author.addcourse("Python")
author.introduceyourself()
'''

class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time 

    def __lt__(self, other):
        return self.time < other.time
	
    def __gt__(self, other):
        return self.time > other.time

    def __contains__(self, word):
        if word in self:
            return True



oldtweet = Tweet("this is an old tweet", 20)
newtweet = Tweet("this is a new tweet", 1000)
print(newtweet > oldtweet)

tweets = [newtweet,oldtweet]

for tweet in sorted(tweets):
    print(tweet.message)


