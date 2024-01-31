import random
import time
import webbrowser
import arcade
import arcade.gui
from player import Player
from serclient import *
import asyncio

LANGUAGE = "rus"

music = arcade.play_sound(arcade.load_sound("env/music/bgmusic.mp3"), looping=True, volume=0.4)
with open("env/data/user.txt", "r", encoding="utf-8") as file:
    for line in file:
        nick = line.strip()
mesto = getMesto(nick)


def resultata():
    with open("env/data/records.txt", "r", encoding="utf-8") as file:
        a = [int(line.strip()) for line in file]
        return [max(a), a[-1]]


# music.volume=0

class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        global mesto
        ans = resultata()
        self.result = ans[1]
        self.record = ans[0]
        self.mesto = mesto

        self.resultTexture = arcade.load_texture("env/buttons/result.png")
        self.recordTexture = arcade.load_texture("env/buttons/record.png")
        self.one = arcade.load_texture("env/parallax/Grassy-Meadow-Parallax-Background-v1/"
                                       "Grassy-Meadow-Parallax-Background-v1/Parallax Background/1-sky.png")
        self.two = arcade.load_texture("env/parallax/Grassy-Meadow-Parallax-Background-v1/"
                                       "Grassy-Meadow-Parallax-Background-v1/Parallax Background/2-clouds.png")
        self.three = arcade.load_texture("env/parallax/Grassy-Meadow-Parallax-Background-v1/"
                                         "Grassy-Meadow-Parallax-Background-v1/Parallax Background/3-hills.png")
        self.four = arcade.load_texture("env/parallax/Grassy-Meadow-Parallax-Background-v1/"
                                        "Grassy-Meadow-Parallax-Background-v1/Parallax Background/4-trees.png")
        self.five = arcade.load_texture("env/parallax/Grassy-Meadow-Parallax-Background-v1/"
                                        "Grassy-Meadow-Parallax-Background-v1/Parallax Background/5-bushes.png")
        self.six = arcade.load_texture("env/parallax/Grassy-Meadow-Parallax-Background-v1/"
                                       "Grassy-Meadow-Parallax-Background-v1/Parallax Background/6-grass.png")

        self.bg = []

        for i in range(1, 61):
            self.bg.append(arcade.load_texture(f"env/parallax/mainbg/full with noise{i}.jpg"))
        self.i = 0
        self.start = time.time()

        self.minTwo = 0
        self.minThree = 0
        self.minFour = 0
        self.minFive = 0
        self.minSix = 0

        arcade.load_font("env/fonts/yukari.ttf")
        self.nameOfGame = arcade.load_texture("env/buttons/name.png")
        self.startStatic = arcade.load_texture("env/buttons/startStatic.png")
        self.startDinamic = arcade.load_texture("env/buttons/startDinamic.png")
        self.rewardsStatic = arcade.load_texture("env/buttons/rewardsStatic.png")
        self.rewardsDinamic = arcade.load_texture("env/buttons/rewardsDinamic.png")
        self.topStatic = arcade.load_texture("env/buttons/topStatic.png")
        self.topDinamic = arcade.load_texture("env/buttons/topDinamic.png")
        self.exitStatic = arcade.load_texture("env/buttons/exitStatic.png")
        self.exitDinamic = arcade.load_texture("env/buttons/exitDinamic.png")
        self.generalStatic = arcade.load_texture("env/buttons/genStatic.png")
        self.generalDinamic = arcade.load_texture("env/buttons/genDinamic.png")
        self.fon = arcade.load_texture("env/bg/fon.png")

        self.angle = 0
        # self.
        # self.bg = arcade.load_texture("env/Default.png")
        # self.bg1 = arcade.load_texture("env/Default.png")
        # self.bgShadow = arcade.load_texture("env/Shadow.png")
        # self.bgChips = arcade.load_texture("env/chips.png")
        # self.exitTexture = arcade.load_texture("env/exit.png")
        # self.optinonsTexture = arcade.load_texture("env/options.png")
        # self.iconVk = arcade.load_texture("env/vk-logo.png")

        #     self.startButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=785, y=40,
        #                                            width=270, height=95)
        #     self.exitButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=1055, y=40,
        #                                           width=270, height=95)
        #     self.optinonsButton = arcade.load_texture("env/cartoon-crystal-ui-collection_52683-73194_1.png", x=785,
        #                                               y=40 + 95 * 3 + 10,
        #                                               width=270, height=95)
        #     self.quest = arcade.load_texture("env/question.png")
        #     self.scaleOfQuest = 0.1
        #     self.ButtonScale = 1.2
        #     self.z = 0
        self.huh = arcade.load_sound("env/music/huh.mp3")

    #     self.font = arcade.load_font("env/DischargePro.ttf")
    #     with open("env/user.txt", "r", encoding="utf-8") as file:
    #         for line in file:
    #             if line.strip() == "None":
    #                 self.manager = arcade.gui.UIManager()
    #                 self.manager.enable()
    #                 self.l = True
    #             else:
    #                 self.l = False
    #
    # def on_click_open(self):
    #     message_box = arcade.gui.UIMessageBox(
    #         width=300,
    #         height=200,
    #         message_text=(
    #             "Ты должен придумать себе ник в настройках"
    #         ),
    #         callback=self.on_message_box_close,
    #         buttons=["Ok"]
    #     )
    #
    #     self.manager.add(message_box)
    #
    # def on_message_box_close(self, button_text):
    #     print(f"User pressed {button_text}.")

    def on_show_view(self):
        global nick
        self.mesto = getMesto(nick)
        ans = resultata()
        self.result = ans[1]
        self.record = ans[0]

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bg[self.i])
        if time.time() - self.start > 1 / 9:
            self.i += 1
            self.start = time.time()
        if self.i >= 60:
            self.i = 0
        arcade.draw_lrwh_rectangle_textured(0, window.height / 1.4, self.nameOfGame.width * (0.6 / 1980 * window.width),
                                            self.nameOfGame.height * (0.6 / 1080 * window.height), self.nameOfGame)

        arcade.draw_lrwh_rectangle_textured(window.width / 35,
                                            window.height / 1.7,
                                            self.startDinamic.width * (0.23 / 1980 * window.width),
                                            self.startDinamic.height * (0.23 / 1080 * window.height), self.startStatic)
        if (window.width / 35 <= window._mouse_x <=
                window.width / 35 + self.startDinamic.width * (0.23 / 1980 * window.width) and
                window.height / 1.7 <= window._mouse_y <=
                window.height / 1.7 + self.startDinamic.height * (0.23 / 1080 * window.height)):
            arcade.draw_lrwh_rectangle_textured(window.width / 35,
                                                window.height / 1.7,
                                                self.startDinamic.width * (0.23 / 1980 * window.width),
                                                self.startDinamic.height * (0.23 / 1080 * window.height),
                                                self.startDinamic)

        arcade.draw_lrwh_rectangle_textured(window.width / 35, window.height / 2,
                                            self.rewardsStatic.width * (0.25 / 1980 * window.width),
                                            self.rewardsStatic.height * (0.25 / 1080 * window.height),
                                            self.rewardsStatic)
        if (window.width / 35 <= window._mouse_x <=
                window.width / 35 + self.rewardsStatic.width * (0.25 / 1980 * window.width) and
                window.height / 2 <= window._mouse_y <=
                window.height / 2 + self.rewardsStatic.height * (0.25 / 1080 * window.height)):
            arcade.draw_lrwh_rectangle_textured(window.width / 35, window.height / 2,
                                                self.rewardsStatic.width * (0.25 / 1980 * window.width),
                                                self.rewardsStatic.height * (0.25 / 1080 * window.height),
                                                self.rewardsDinamic)

        self.angle += 0.5

        arcade.draw_lrwh_rectangle_textured(window.width / 1.1, window.height / 1.3,
                                            self.generalStatic.width * (0.09 / 1980 * window.width),
                                            self.generalStatic.height * (0.09 / 1980 * window.width),
                                            self.generalStatic, self.angle)
        if (window.width / 1.1 <= window._mouse_x <=
                window.width / 1.1 + self.generalStatic.width * (0.09 / 1980 * window.width) and
                window.height / 1.3 <= window._mouse_y <=
                window.height / 1.3 + self.generalStatic.height * (0.09 / 1980 * window.width)):
            arcade.draw_lrwh_rectangle_textured(window.width / 1.1, window.height / 1.3,
                                                self.generalStatic.width * (0.09 / 1980 * window.width),
                                                self.generalStatic.height * (0.09 / 1980 * window.width),
                                                self.generalDinamic, self.angle)

        arcade.draw_lrwh_rectangle_textured(window.width / 35, window.height / 2.33,
                                            self.topStatic.width * (0.123 / 1980 * window.width),
                                            self.topStatic.height * (0.123 / 1080 * window.height), self.topStatic)
        if (window.width / 35 <= window._mouse_x <=
                window.width / 35 + self.topStatic.width * (0.123 / 1980 * window.width) and
                window.height / 2.33 <= window._mouse_y <=
                window.height / 2.33 + self.topStatic.height * (0.123 / 1080 * window.height)):
            arcade.draw_lrwh_rectangle_textured(window.width / 35, window.height / 2.33,
                                                self.topStatic.width * (0.123 / 1980 * window.width),
                                                self.topStatic.height * (0.123 / 1080 * window.height), self.topDinamic)

        arcade.draw_text(f"{self.mesto}", window.width / 35 + self.topStatic.width * (0.206 / 1980 * window.width),
                         window.height / 2.3 + self.topStatic.height * (0.011 / 1080 * window.height),
                         anchor_x="center",
                         color=(245, 148, 24), font_name="Yukarimobile", font_size=40 / 1980 * window.width)
        arcade.draw_text(f"{self.mesto}", window.width / 35 + self.topStatic.width * (0.2 / 1980 * window.width),
                         window.height / 2.3 + self.topStatic.height * (0.03 / 1080 * window.height), anchor_x="center",
                         color=arcade.color.WHITE, font_name="Yukarimobile", font_size=40 / 1980 * window.width)

        arcade.draw_text(f"{self.result}", window.width / 11.2, window.height / 3.3, anchor_x="center",
                         color=(245, 148, 24), font_name="Yukarimobile", font_size=50 / 1366 * window.width)
        arcade.draw_text(f"{self.result}", window.width / 11.7, window.height / 3.25, anchor_x="center",
                         color=arcade.color.WHITE, font_name="Yukarimobile", font_size=50 / 1366 * window.width)

        arcade.draw_text(f"{self.record}", window.width / 5.27, window.height / 3.3, anchor_x="center",
                         color=(245, 148, 24), font_name="Yukarimobile", font_size=50 / 1366 * window.width)
        arcade.draw_text(f"{self.record}", window.width / 5.35, window.height / 3.25, anchor_x="center",
                         color=arcade.color.WHITE, font_name="Yukarimobile", font_size=50 / 1366 * window.width)
        #
        # arcade.draw_line(window.width / 22 + (self.resultTexture.width * (0.13 / 1980 * window.width)) / 2, 0,
        #                  window.width / 22 + (self.resultTexture.width * (0.13 / 1980 * window.width)) / 2,
        #                  window.height, arcade.color.WHITE)
        # arcade.draw_line(window.width / 7 + (self.resultTexture.width * (0.13 / 1980 * window.width)) / 2, 0,
        #                  window.width / 7 + (self.resultTexture.width * (0.13 / 1980 * window.width)) / 2,
        #                  window.height, arcade.color.WHITE)
        # arcade.draw_line(0, window.height / 3, window.width, window.height / 3, arcade.color.WHITE)

        arcade.draw_lrwh_rectangle_textured(window.width / 22, window.height / 4.8,
                                            self.resultTexture.width * (0.13 / 1980 * window.width),
                                            self.resultTexture.height * (0.13 / 1080 * window.height),
                                            self.resultTexture)
        arcade.draw_lrwh_rectangle_textured(window.width / 7, window.height / 4.95,
                                            self.recordTexture.width * (0.15 / 1980 * window.width),
                                            self.recordTexture.height * (0.15 / 1080 * window.height),
                                            self.recordTexture)

        arcade.draw_lrwh_rectangle_textured(window.width / 33, window.height / 9,
                                            self.exitStatic.width * (0.08 / 1980 * window.width),
                                            self.exitStatic.height * (0.08 / 1080 * window.height), self.exitStatic)
        if (window.width / 33 <= window._mouse_x <=
                window.width / 33 + self.exitStatic.width * (0.08 / 1980 * window.width) and
                window.height / 9 <= window._mouse_y <=
                window.height / 9 + self.exitStatic.height * (0.08 / 1080 * window.height)):
            arcade.draw_lrwh_rectangle_textured(window.width / 33, window.height / 9,
                                                self.exitStatic.width * (0.08 / 1980 * window.width),
                                                self.exitStatic.height * (0.08 / 1080 * window.height),
                                                self.exitDinamic)

        # arcade.draw_line(window.width / 25, 0, window.width / 25, window.height, arcade.color.WHITE)

        # arcade.draw_text(f"{self.mesto} mesto", window.width / 2, window.height / 2, anchor_x="center",
        #                  color=arcade.color.WHITE, font_name="Yukarimobile", font_size=80)
        # arcade.draw_text(f"{self.result} best result", window.width / 2, window.height / 3, anchor_x="center",
        #                  color=arcade.color.WHITE, font_name="Yukarimobile", font_size=80)
        # arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.logo)
        #
        # arcade.draw_text(f"{self.result}", start_x=window.width / 8, start_y=window.height / 6.7, anchor_x="center",
        #                  color=arcade.color.WHITE, font_size=80, font_name="Yukarimobile")
        #
        # if self.minTwo > window.width:
        #     self.minTwo = 0
        # if self.minThree > window.width:
        #     self.minThree = 0
        # if self.minFour > window.width:
        #     self.minFour = 0
        # if self.minFive > window.width:
        #     self.minFive = 0
        # if self.minSix > window.width:
        #     self.minSix = 0
        # self.minTwo += 0.5 / 1980 * window.width
        # self.minThree += 0.8 / 1980 * window.width
        # self.minFour += 1.1 / 1980 * window.width
        # self.minFive += 1.4 / 1980 * window.width
        # self.minSix += 1.7 / 1980 * window.width

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if (window.width / 35 <= x <=
                window.width / 35 + self.startDinamic.width * (0.23 / 1980 * window.width) and
                window.height / 1.7 <= y <=
                window.height / 1.7 + self.startDinamic.height * (0.23 / 1080 * window.height)):
            arcade.play_sound(self.huh)
            self.window.show_view(gameView)
        if (window.width / 33 <= x <= window.width / 33 + self.exitStatic.width * 0.08 and
                window.height / 9 <= y <= window.height / 9 + self.exitStatic.height * 0.08):
            window.close()
        if (window.width / 1.1 <= x <= window.width / 1.1 + self.generalStatic.width * 0.09 and
                window.height / 1.3 <= y <= window.height / 1.3 + self.generalStatic.height * 0.09):
            generalView.i = self.i
            self.window.show_view(generalView)
        if (window.width / 35 <= x <=
                window.width / 35 + self.topStatic.width * (0.123 / 1980 * window.width) and
                window.height / 2.33 <= window._mouse_y <=
                window.height / 2.33 + self.topStatic.height * (0.123 / 1080 * window.height)):
            self.window.show_view(LidersView())
        # if not self.l and (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
        #                    <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
        #                    and
        #                    window.height / 2 - self.startButton.height / 2 * self.ButtonScale <= y
        #                    <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale):
        #     arcade.play_sound(self.huh)
        #     global chipsView
        #     self.window.show_view(chipsView)
        # if (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
        #         <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
        #         and
        #         window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height <= y
        #         <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale - 0.15 * window.height):
        #     global optView
        #     optView.z = self.z
        #     self.window.show_view(optView)
        # if (window.width / 2 - self.startButton.width / 2 * self.ButtonScale <= x
        #         <= window.width / 2 + self.startButton.width / 2 * self.ButtonScale
        #         and
        #         window.height / 2 - self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height <= y
        #         <= window.height / 2 + self.startButton.height / 2 * self.ButtonScale - 0.3 * window.height):
        #     arcade.play_sound(self.huh)
        #     arcade.exit()
        # if (window.width / 10 - self.iconVk.width / 2 * 0.05 <= x <=
        #         window.width / 10 + self.iconVk.width * 0.05
        #         and window.height / 9 - self.iconVk.height / 2 * 0.05 <= y <=
        #         window.height / 9 + self.iconVk.height * 0.05):
        #     webbrowser.open("https://vk.com/blaatnoiii")
        # if (window.width / 2 - self.quest.width / 2 * 0.1 <= x <=
        #         window.width / 2 + self.quest.width / 2 * 0.1 and
        #         window.height / 2 - self.quest.height / 2 * 0.1 <= y <=
        #         window.height / 2 + self.quest.height / 2 * 0.1):
        #     self.scaleOfQuest = 0.001
        #     self.on_click_open()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P:
            self.window.show_view(LidersView())


class GeneralView(arcade.View):
    def __init__(self, i):
        super().__init__()
        self.fon = arcade.load_texture("env/bg/fon.png")
        self.bg = []

        for i in range(1, 61):
            self.bg.append(arcade.load_texture(f"env/parallax/mainbg/full with noise{i}.jpg"))
        self.i = i
        self.start = time.time()

    def on_draw(self):
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bg[self.i])
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.fon)
        arcade.draw_text("general", window.width / 2, window.height / 1.2, anchor_x="center",
                         color=arcade.color.WHITE, font_name="Yukarimobile", font_size=100 / 1980 * window.width)
        if time.time() - self.start > 1 / 9:
            self.i += 1
            self.start = time.time()
        if self.i >= 60:
            self.i = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            start_view.i = self.i
            self.window.show_view(start_view)


class OptionsView(arcade.View):
    def __init__(self, z):
        super().__init__()
        self.bg = arcade.load_texture("env/Shadow.png")
        self.font = arcade.load_font("env/DischargePro.ttf")
        self.rus = arcade.load_texture("env/rus.png")
        self.eng = arcade.load_texture("env/eng.png")
        self.login = arcade.load_texture("env/login.png")
        self.on = arcade.load_texture("env/onoff.png", x=0, y=0, width=1146, height=503)
        self.off = arcade.load_texture("env/onoff.png", x=0, y=503, width=1146, height=503)
        self.chet = 0
        self.sizeOFFlag = 0.1
        self.z = z
        self.base = False

        with open("env/data/user.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "None":
                    self.manager = arcade.gui.UIManager()
                    self.manager.enable()
                    self.l = True
                    animals = ["кенгуру", "жираф", "пингвин", "лев"]
                    self.textq = arcade.gui.UIInputText(window.width / 1.65, 0.3 * window.height,
                                                        width=window.width / 4, height=140, font_name="Discharge Pro",
                                                        text_color=arcade.color.WHITE,
                                                        font_size=80,
                                                        text=f"{animals[random.randint(0, len(animals) - 1)]}"
                                                             f"{random.randint(0, 100)}")
                    self.manager.add(self.textq)
                else:
                    self.nick = line.strip()
                    self.l = False

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0 - self.z, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(window.width - self.z, 0, window.width, window.height, self.bg)
        if LANGUAGE == "rus":
            arcade.draw_text(f"Настройки", window.width / 2, 0.84 * window.height,
                             arcade.color.WHITE, 80,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Язык", window.width / 4, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"какая то настройка", window.width / 4 + window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Музыка", window.width / 4, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"какая то настройка", window.width / 4 + window.width / 2, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Пользователь", window.width / 4, 0.35 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text("О разработчиках", window.width / 4, 0.2 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
        else:
            arcade.draw_text(f"Options", window.width / 2, 0.84 * window.height,
                             arcade.color.WHITE, 80,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Language", window.width / 4, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Ram mode", window.width / 4 + window.width / 2, 0.65 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Music", window.width / 4, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")
            arcade.draw_text(f"Python is trash", window.width / 4 + window.width / 2, 0.5 * window.height,
                             arcade.color.WHITE, 65,
                             font_name="Discharge Pro", anchor_x="center")

        if self.l:
            self.manager.draw()
            arcade.draw_lrwh_rectangle_textured(window.width / 4 + window.width / 2 - self.login.width / 2 * 0.2,
                                                0.15 * window.height,
                                                self.login.width * 0.2,
                                                self.login.height * 0.2, self.login)
        else:
            arcade.draw_text(self.nick, window.width / 4 + window.width / 2, 0.35 * window.height,
                             font_name="Discharge Pro",
                             color=arcade.color.GREEN, anchor_x="center",
                             font_size=80)
        if self.base:
            arcade.draw_text("ник занят", window.width / 4 + window.width / 2, 0.1 * window.height,
                             font_name="Discharge Pro",
                             color=arcade.color.RED, anchor_x="center",
                             font_size=80)

        arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.1 * window.width,
                                            0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag,
                                            self.rus.width * self.sizeOFFlag,
                                            self.rus.height * self.sizeOFFlag, self.rus)
        arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.2 * window.width,
                                            0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag,
                                            self.rus.width * self.sizeOFFlag,
                                            self.rus.height * self.sizeOFFlag, self.eng)

        if (window.width / 4 + 0.1 * window.width <= window._mouse_x
                <= window.width / 4 + 0.1 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= window._mouse_y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.1 * window.width,
                                                0.67 * window.height - self.rus.height / 2 * (self.sizeOFFlag + 0.04),
                                                self.rus.width * (self.sizeOFFlag + 0.04),
                                                self.rus.height * (self.sizeOFFlag + 0.04), self.rus)
        if (window.width / 4 + 0.2 * window.width <= window._mouse_x
                <= window.width / 4 + 0.2 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= window._mouse_y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            arcade.draw_lrwh_rectangle_textured(window.width / 4 + 0.2 * window.width,
                                                0.67 * window.height - self.rus.height / 2 * (self.sizeOFFlag + 0.04),
                                                self.rus.width * (self.sizeOFFlag + 0.04),
                                                self.rus.height * (self.sizeOFFlag + 0.04), self.eng)
        if self.chet % 2 == 0:
            arcade.draw_lrwh_rectangle_textured(window.width / 2.8,
                                                0.5 * window.height,
                                                self.on.width * 0.15,
                                                self.on.height * 0.15,
                                                self.on)
        else:
            arcade.draw_lrwh_rectangle_textured(window.width / 2.8,
                                                0.5 * window.height,
                                                self.on.width * 0.15,
                                                self.on.height * 0.15,
                                                self.off)

        self.z += 3
        if self.z > window.width:
            self.z = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            start_view.z = self.z
            self.window.show_view(start_view)
        if symbol == arcade.key.D:
            webbrowser.open("https://github.com/luckybearprogrammer")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        global LANGUAGE
        if (window.width / 4 + 0.1 * window.width <= x
                <= window.width / 4 + 0.1 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            LANGUAGE = "rus"
        if (window.width / 4 + 0.2 * window.width <= window._mouse_x
                <= window.width / 4 + 0.2 * window.width + self.rus.width * self.sizeOFFlag and
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag <= window._mouse_y <=
                0.67 * window.height - self.rus.height / 2 * self.sizeOFFlag + self.rus.height * self.sizeOFFlag):
            LANGUAGE = "eng"
        if (window.width / 4 + window.width / 2 - self.login.width / 2 * 0.2 <= x <= window.width / 4 +
                window.width / 2 - self.login.width / 2 * 0.2 + self.login.width * 0.2 and
                0.15 * window.height <= y <= 0.15 * window.height + self.login.height * 0.2):
            if can(str(self.textq.text)):
                print(f"да, ник {self.textq.text} не занят")
                with open("env/data/user.txt", "w", encoding="utf-8") as file:
                    file.write(self.textq.text)
                self.nick = self.textq.text
                self.l = False
                self.base = False
                start_view.l = False
            else:
                self.base = True
        if window.width / 2.8 <= x <= window.width / 2.8 + self.on.width * 0.15 and 0.5 * window.height <= 0.5 * window.height + self.on.height:
            global music
            if self.chet % 2 != 0:
                music.volume = 1
            else:
                music.volume = 0
            self.chet += 1


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.camera = arcade.Camera(window.width, window.height)
        self.enemy_list = arcade.SpriteList()
        self.tile_map = arcade.load_tilemap("env/For_my_game.tmx")
        print(self.tile_map.sprite_lists)
        self.scene = arcade.Scene()
        self.background_list = arcade.SpriteList()
        self.background_list_2 = arcade.SpriteList()
        for i in self.tile_map.sprite_lists['Platforms']:
            self.scene.add_sprite('Ground', i)
        for i in self.tile_map.sprite_lists['Background']:
            self.background_list.append(i)
        for i in self.tile_map.sprite_lists['Background2']:
            self.background_list_2.append(i)
        for i in self.tile_map.sprite_lists['Enemy']:
            self.enemy_list.append(i)
        self.setup()

    def on_resize(self, width: int, height: int):
        self.camera.viewport_width = window.width
        self.camera.viewport_height = window.height
        self.tile_map.scaling = 1 / 1980 * window.width

    def on_draw(self):
        self.clear()
        self.background_list.draw()
        self.background_list_2.draw()
        self.enemy_list.draw()
        self.scene.draw()
        self.enemy_list.draw()
        self.camera.use()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.background_list.update()
        self.background_list_2.update()
        self.center_camera_to_player()
        self.player.update()
        self.scene.update()
        self.enemy_list.update()
        self.physics_engine.update()
        # self.center_camera_to_player()
        self.enemy_list.update()
        self.player.update_animation()
        if self.player.center_x <= self.player.width / 4:
            self.player.center_x = self.player.width / 4
        # if self.player.center_x >= self.width - self.player.width / 4:
        #     self.player.center_x = self.width - self.player.width / 4
        # for enemy in self.enemy_list:
        #     death_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
        #     if death_list:
        #         enemy.kill()
        #         print("Game over")
        #         window.close()

    def setup(self):
        self.scene.add_sprite_list('Player')
        self.player.position = 50 * self.tile_map.scaling, 384 * self.tile_map.scaling
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene['Ground'],
                                                             gravity_constant=1.8 / 1980 * window.width)

    def center_camera_to_player(self):
        screen_center_x_1 = self.player.center_x - self.camera.viewport_width / 2
        screen_center_y_1 = window.height / 32
        if screen_center_x_1 < 0:
            screen_center_x_1 = 0
        if not self.camera.position.x + window.width >= 200 * 64 * self.tile_map.scaling:
            self.camera.move_to((screen_center_x_1, screen_center_y_1))
        else:
            chipsView.camerax = self.camera.position.x
            chipsView.cameray = self.camera.position.y
            self.window.show_view(chipsView)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x += 4 / 1980 * window.width
        if symbol == arcade.key.D:
            self.player.change_x += 4 / 1980 * window.width
        if symbol == arcade.key.LEFT:
            self.player.change_x -= 4 / 1980 * window.width
        if symbol == arcade.key.A:
            self.player.change_x -= 4 / 1980 * window.width
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 20 / 1080 * window.height
        if symbol == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = 20 / 1080 * window.height

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        if symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 0
        if symbol == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = 0

        if symbol == arcade.key.E:
            self.player.position = 200 * 60 * self.tile_map.scaling, 100


class ChipsView(arcade.View):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.z = 0
        self.camerax = x
        self.cameray = y
        self.bg = []
        # for i in range(1, 832):
        #     self.bg.append(arcade.load_texture(f"env/mem/cadr{i}.jpg"))
        self.start = time.time()

        self.i = 0

    def on_show_view(self):
        arcade.play_sound(arcade.load_sound("env/mem/Мужик-ест-чипсы.mp3"), looping=True, volume=0.4)

    def on_draw(self):
        self.clear()
        # if time.time() - self.start >= 1 / 60:
        #     self.i += 1
        # if self.i >= 831:
        #     self.i = 0
        # arcade.draw_lrwh_rectangle_textured(self.camerax - self.z, self.cameray, window.width, window.height,
        #                                     self.bg[self.i])

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(start_view)

#тест
class LidersView(arcade.View):
    def __init__(self):
        # self.startProgramm = time.time()
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.load_font("env/fonts/yukari.ttf")
        x = random.randint(0, 1)
        print(x)
        if x == 0:
            self.bgTexture = [arcade.load_texture(f"env/bg/bg1/cadr{i}.jpg") for i in range(7)]
            self.perelist = 1 / 15
        else:
            self.bgTexture = [arcade.load_texture(f"env/bg/lid/cadr{i}.jpg") for i in range(61)]
            self.perelist = 1 / 40

        self.i = 0
        self.start = time.time()

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.loadingLid())

    async def loadingLid(self):
        bg_tex = arcade.load_texture("env/bg/bgliders.png")
        formatted_lorem_ipsum = ""
        max_length = 0
        names = []
        numbers = []
        a = await top()
        for line in a:
            if line:
                parts = line.split()
                if len(parts) == 2:
                    name, number = parts
                    names.append(name)
                    numbers.append(number)
                    max_length = max(max_length, len(name))
        max_length += 20
        a.pop(-1)
        for line in a:
            formatted_lorem_ipsum += line.split()[0] + " " * (max_length - len(line)) + line.split()[1] + "\n\n"

        text_area = arcade.gui.UITextArea(x=500 / 1980 * window.width,
                                          y=200 / 1080 * window.height,
                                          width=1500 / 1980 * window.width,
                                          height=800 / 1080 * window.height,
                                          text=formatted_lorem_ipsum,
                                          text_color=arcade.color.WHITE,
                                          font_size=50 / 1980 * window.width,
                                          font_name="Yukarimobile")
        self.manager.add(
            arcade.gui.UITexturePane(
                text_area.with_space_around(),
                tex=bg_tex,
            )
        )
        # print(time.time() - self.startProgramm)

    def on_draw(self):
        self.clear()
        if time.time() - self.start >= self.perelist:
            self.i += 1
            self.start = time.time()
        if self.i >= len(self.bgTexture):
            self.i = 0
        # arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bg)
        arcade.draw_lrwh_rectangle_textured(0, 0, window.width, window.height, self.bgTexture[self.i])

        self.manager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.window.show_view(start_view)


window = arcade.Window(fullscreen=True)

# Load the icon image


# window = arcade.Window(fullscreen=True)
start_view = StartView()
chipsView = ChipsView()
gameView = GameView()
# optView = OptionsView(0)
generalView = GeneralView(0)
window.show_view(start_view)
arcade.run()
# тест