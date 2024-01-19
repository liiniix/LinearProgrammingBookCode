from manim import *

isAnimate = False


class TabularMethodEquivalentToMatrixMethod(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{tblr}")

        tex = Tex(
            r"$A$",
            tex_template=myTemplate,
            font_size=144,
        )

        self.add(tex)