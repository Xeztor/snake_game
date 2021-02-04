from pygame.rect import Rect


class Snake(Rect):
    food_eaten = 1

    def eat(self):
        self.food_eaten += 1

    def __len__(self):
        return self.food_eaten




