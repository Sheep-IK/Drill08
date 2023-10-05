import random
from pico2d import *


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint( 100, 700)
        self.frame = 1
        self.image = load_image('ball41x41.png')
    def update(self):
        self.frame = 1
        if self.y > 70:
            self.y -= 5
        else:
            self.y = 70

    def draw(self):
        self.image.clip_draw(self.frame*0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




def reset_world():
    global running
    global grass
    global team
    global world
    global balls
    global bwd
    global swd

    running = True
    world = []
    bwd = []
    swd = []

    grass = Grass() # 클래스를 이용해 객체를 찍어냄.
    world.append(grass)
    bwd.append(grass)
    swd.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    balls = [BigBall() for i in range(20)]
    bwd += balls





def update_world():
    for o in world:
        o.update()
    for o in bwd:
        o.update()


def render_world():
    clear_canvas()
    for o in team:
     o.draw()
    for o in balls:
        o.draw()
    update_canvas()






open_canvas()

reset_world()

# game main loop code
while running:
    handle_events()
    update_world() #객체들 상호작용 결과 업데이트
    render_world()
    delay(0.05)

# finalization code

close_canvas()
