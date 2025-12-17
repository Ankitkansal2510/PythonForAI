class Enemy:

    def __init__(self,atkl,atkh):#This is known as the constructor of this class
        self.atkl=atkl
        self.atkh=atkh


    def get_atk(self):
        print(self.atkl)

enemy1=Enemy(20,90)
enemy1.get_atk()

enemy2=Enemy(30,40)
enemy2.get_atk()