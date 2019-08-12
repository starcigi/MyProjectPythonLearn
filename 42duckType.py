class Duck:
    def quack(self):
        print('嘎嘎嘎')
    def feathers(self):
        print('这是一只白皮鸭子')

class Person:
    def quack(self):
        print('我不是鸭子!')
    def feathers(self):
        print('我是人类！')

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()
