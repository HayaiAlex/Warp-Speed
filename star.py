from p5 import *
class star:
    r = 16

    def __init__(self):
        self.x = random_uniform(width/2, -width/2)
        self.y = random_uniform(height/2, -height/2)
        self.z = random_uniform(width, 0)
        self.pz = self.z
        self.px = self.x
        self.py = self.y

    def update(self, speed):
        self.z -= speed
        if self.z < 1:
            self.x = random_uniform(width/2, -width/2)
            self.y = random_uniform(height/2, -height/2)
            self.z = width
            self.pz = self.z
            self.px = self.x
            self.py = self.y



    def show(self):
        fill(255)
        no_stroke()

        sx = remap(self.x / self.z, (0, 1), (0, width))
        sy = remap(self.y / self.z, (0, 1), (0, height))
        sr = remap(self.z, (0, width), (self.r, 0))

        circle((sx, sy), sr)

        # px = remap(self.x / self.pz, (0, 1), (0, width))
        # py = remap(self.y / self.pz, (0, 1), (0, height))


        self.pz = self.z

        stroke(255)
        if sx != self.px:
            try:
                line((sx, sy), (self.px, self.py))
            except ValueError:
                print("Value Error:", self.px, sx) # px and sx are the same value. sx is the same value twice in a row breaking line

        self.px = sx
        self.py = sy
