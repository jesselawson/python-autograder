
class Shark:

    # Class variables
    animal_type = "fish"
    location = "ocean"

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_health(self):
        return self.health

    def bite(self, target):
        target.health -= 25
        if target.health < 0:
            target.die()

    def die(self):
        self.health = 0




def main():
    shark1 = Shark("Shark1", 50)
    shark2 = Shark("Shark2", 25)

if __name__ == "__main__":
    main()