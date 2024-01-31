import arcade
import time

RIGHT_FACING = 0
LEFT_FACING = 1

# arcade.load_texture("env/23",)
def load_texture_pair(filename, x, y, width, height):
    return [arcade.load_texture(filename, x, y, width, height),
            arcade.load_texture(filename, x, y, width, height, flipped_horizontally=True)]


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(scale=3)
        self.person_face_direction = RIGHT_FACING
        self.run_texture = []
        for i in range(10):
            texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Run.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.run_texture.append(texture)
        self.current_texture = 0
        self.idle_texture = []
        self.jump_texture = []
        self.current_textureJump = 0
        for i in range(10):
            texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Idle.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.idle_texture.append(texture)
        for i in range(3):
            texture = load_texture_pair(f"env/sprite/Colour1/Outline/120x80_PNGSheets/_Jump.png", x=i * 120, y=0,
                                        width=120, height=80)
            self.jump_texture.append(texture)

        self.texture = self.idle_texture[0][self.person_face_direction]
        self.start = time.time()

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x < 0 and self.person_face_direction == RIGHT_FACING:
            self.person_face_direction = LEFT_FACING
        if self.change_x > 0 and self.person_face_direction == LEFT_FACING:
            self.person_face_direction = RIGHT_FACING
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture[self.current_texture][self.person_face_direction]
        elif self.change_y > 0:
            self.texture = self.jump_texture[self.current_textureJump][self.person_face_direction]
        else:
            self.texture = self.run_texture[self.current_texture][self.person_face_direction]
        # print(time.time() - self.start)
        if time.time() - self.start > 0.05:
            self.current_texture += 1
            self.current_textureJump += 1
            self.start = time.time()
        if self.current_textureJump >= 3:
            self.current_textureJump = 0
        if self.current_texture >= 10:
            self.current_texture = 0
