"""A little playground for emergent behaviour (boids and such)"""
import pygame
import random

SCREEN_SIZE = (1536, 864)
CENTER = tuple((i//2 for i in SCREEN_SIZE))
FRAME_RATE = 60
NUM_BOIDS = 100


class boid:
    def __init__(self, target=pygame.mouse, position = 'random', velocity=(.01, .01)):
        if position == 'random':
            self.pos = [random.random() * i for i in SCREEN_SIZE]
        else:
            self.pos = position
        self.vel = pygame.Vector2(velocity)
        self.acel = pygame.Vector2(0, 0)
        self.width = 2
        self.acceleration = pygame.Vector2(0, 0)
        self.position_error = 0
        self.target_position = (0, 0)
        self.target = target
        # gains
        self.p = .01  # proportional
        self.i = 0  # integral
        self.d = .1  # derivative
        #s curve
        self.max_vel = 10
        self.max_acel = 2

    def __repr__(self):
        return f"boid: position= {self.pos}, target= {type(self.target)}"

    def __type__(self):
        return "boid"

    def randomize(self):
        self.max_vel += (random.random() - .5) * 2
        self.max_acel += (random.random() - .5) * .75
        self.p += (random.random() -.5) * .005
        self.d += (random.random() -.5) * .1

    def get_pos(self):
        return self.pos

    def getSprite(self) -> list:
        tip = self.pos
        try:
            left = self.pos - self.vel + (self.width * self.vel.normalize().rotate(90))
            right = self.pos - self.vel + (self.width * self.vel.normalize().rotate(-90))
        except ValueError:
            left = self.pos
            right = self.pos
        return (tip, left, right)

    def setTarget(self, other):
        self.target = other

    def update(self) -> None:
        self.pos += self.vel
        self.vel += self.acel * self.p
        if self.vel.magnitude() > self.max_vel:
            self.vel.scale_to_length(self.max_vel)
        if self.acel.magnitude() > self.max_acel:
            self.acel.scale_to_length(self.max_acel)
        self.target_position = self.target.get_pos()
        self.position_error = (self.target_position-self.pos).magnitude()
        self.acel = (self.target_position - self.pos) * self.d
        # print(f"position= {self.pos}, velocity= {self.vel}, acceleration= {self.acel}")
        # self.acel = self.pos-(pygame.Vector2(pygame.mouse.get_pos())*.001)



def make_boids(layer_size_sequence=range(10,100,10)):
    boids = []
    curr_layer = []
    
    center_boid = boid()
    center_boid.pos = (CENTER)
    center_boid.max_vel=0
    
    prev_layer=[center_boid]
    for layer in layer_size_sequence:
        for boi in range(layer):
            curr_layer.append(boid())
            curr_layer[-1].target = prev_layer[boi % len(prev_layer)]
        boids += curr_layer
        prev_layer=curr_layer
        curr_layer=[]
    return boids
        




pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
buffer = pygame.Surface(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
dt = 0



boids = make_boids(range(10,1000,10))

for boid in boids:
    boid.randomize()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(FRAME_RATE) / 1000
    pygame.draw.rect(buffer, (0, 0, 0, 10), pygame.Rect((0, 0), SCREEN_SIZE))
    for boid in boids:
        pygame.draw.aalines(buffer, "red", True, boid.getSprite())
        boid.update()
    screen.blit(buffer, (0,0))
    pygame.display.flip()

pygame.quit()
