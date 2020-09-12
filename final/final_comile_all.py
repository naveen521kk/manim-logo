from manim import *

class ManimLogo(Scene):
    def construct(self):
        back=ImageMobject("back_ground.png").scale(4)
        self.add(back)
        self.wait(2)
        text=ImageMobject("m_logo.png").scale(4)
        self.play(FadeIn(text),run_time=3)
        self.wait(2)
        temp=text
        temp_dict={}
        for i in "anim":
            text=ImageMobject(i+"_logo.png").scale(4)
            temp_dict[i]=text
            self.play(Transform(temp,text),run_time=2)
            self.wait(3)
            self.remove(temp)
            temp=text
        for i in temp_dict:
            self.add(temp_dict[i])
        self.wait(3)

"manim final_comile_all.py -pl -r 500,500 --disable_caching"
