class student:
    
    def __init__(self,name,std,roll):
        self.name=name
        self.std=std
        self.roll=roll
        
    
    def section(self):
        if(self.roll>=20):
            print("section B")
        else:
            print("section A")