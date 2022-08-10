from manim import *
from pathlib import Path
import os

FLAGS = "-pqm"
SCENE = "MyScene2"


class MyScene1(Scene):
    def construct(self):
        self.play(GrowFromCenter(Circle()))


class MyScene2(Scene):
    def construct(self):
        self.play(GrowFromCenter(Square()))


if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
