class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        print(self.color)
    def show_cost(self):
        print(self.cost)

p1=Phone()
p1.set_color("blue")
p1.set_cost(1000)
p1.show_color()
p1.show_cost()