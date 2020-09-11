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
    def some(self):
        m_text=ImageMobject("m_logo.png").scale(4)
        self.play(FadeIn(m_text),run_time=3)
        self.wait(2)
        self.remove(m_text)
        
        a_text=ImageMobject("a_logo.png").scale(4)
        self.play(FadeIn(a_text),run_time=3)
        self.remove(a_text)
        self.wait(1)
        n_text=ImageMobject("n_logo.png").scale(4)
        self.play(FadeIn(n_text),run_time=3)
        self.remove(n_text)
        self.wait(2)
        i_text=ImageMobject("i_logo.png").scale(4)
        self.play(FadeIn(i_text),run_time=3)
        self.remove(i_text)
        self.wait(2)
        m_text=ImageMobject("m_logo.png").scale(4)
        self.play(FadeIn(m_text),run_time=3)
        self.remove(m_text)
        self.wait(2)
"manim final_comile_all.py -pl -r 500,500 --disable_caching"