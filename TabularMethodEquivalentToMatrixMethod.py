from manim import *

isAnimate = False


class TabularMethodEquivalentToMatrixMethod(Scene):
    def construct(self):
        self.color_selector = 0
        self.colors = [BLUE_C, DARK_BROWN, GRAY, YELLOW_D,
                       DARK_BLUE, GREEN_C, LIGHT_PINK, PURE_BLUE,
                       PURE_RED, DARK_BLUE, BLUE, RED, MAROON_E, PURPLE,
                       TEAL_E, RED_B, PURPLE_C]

        def playTransform(a, b, c, x, y, z):
            self.play(
                AnimationGroup(Transform(a, x),
                               Transform(b, y),
                               Transform(c, z)
                )
            )
            self.wait(1)
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{tabularray}")

        tabularNotation = Tex(
            r"""\begin{tblr}{
			colspec = {ccccc},
			hline{2-7}  = {1}{2-5}{solid},
			vline{2-10} = {1}{2-6}{solid}
		}
				&	$z$	&	$x_B$	&	$x_N$		&	RHS		\\
		$z$		&	$1$	&	$0$		&	$z_j-c_j$	&	$z_0$	\\
		$x_B$	&	$0$	&	$1$		&	$y_j$		&	$b$		\\
	\end{tblr}""",
            tex_template=myTemplate,
            font_size=40,
        ).to_edge(LEFT + UP)


        tabularNotationEquivalet = Tex(
            r"""\begin{tblr}{
			colspec = {ccccc},
			hline{2-7}  = {1}{2-5}{solid},
			vline{2-10} = {1}{2-6}{solid}
		}
				&	$z$	&	$x_B$	&	$x_N$				&	RHS		\\
		$z$		&	$1$	&	$0$		&	$c_BB^{-1}N-c_N$	&	$z_0$	\\
		$x_B$	&	$0$	&	$1$		&	$B^{-1}N$			&	$b$		\\
	\end{tblr}""",
            tex_template=myTemplate,
            font_size=40
        ).to_edge(RIGHT + UP)

        actualTabular = Tex(
            r"""\begin{tblr}{
			colspec = {ccccccccc},
			hline{2-6}  = {1}{2-9}{solid},
			vline{2-10} = {1}{2-5}{solid}
		}
			 & $z$ & $x_1$ & $x_2$ & $x_3$ & $x_4$ & $x_5$ & $x_6$ & RHS\\
		$z$  & $1$ & $-1$  & $-1$  & $4$   & $0$   & $0$   & $0$   & $0$\\
		$x_4$& $0$ & $1$   & $1$   & $2$   & $1$   & $0$   & $0$   & $9$\\
		$x_5$& $0$ & $1$   & $1$   & $-1$  & $0$   & $1$   & $0$   & $2$\\
		$x_6$& $0$ & $-1$  & $1$   & $1$   & $0$   & $0$   & $1$   & $4$\\
	\end{tblr}""",
            tex_template=myTemplate,
            font_size=40,
        ).to_edge(DOWN)

        self.add(tabularNotation, tabularNotationEquivalet, actualTabular)
















        z_up_tabularNotation = tabularNotation[0][0]
        z_up_tabularNotationEquivalet = tabularNotationEquivalet[0][0]
        z_up_actualTabular = actualTabular[0][0]

        a0 = self.getSurroundingRectangle(z_up_tabularNotation)
        b0 = self.getSurroundingRectangle(z_up_tabularNotationEquivalet)
        c0 = self.getSurroundingRectangle(z_up_actualTabular)
        
        self.play(
            FadeIn(a0, b0, c0)
        )
        self.wait(1)

        a = self.getSurroundingRectangle(z_up_tabularNotation)
        b = self.getSurroundingRectangle(z_up_tabularNotationEquivalet)
        c = self.getSurroundingRectangle(z_up_actualTabular)

        xb_up_tabularNotation = tabularNotation[0][1:3]
        xb_up_tabularNotationEquivalet = tabularNotationEquivalet[0][1:3]
        xb_up_actualTabular = actualTabular[0][7:13]

        d = self.getSurroundingRectangle(xb_up_tabularNotation)
        e = self.getSurroundingRectangle(xb_up_tabularNotationEquivalet)
        f = self.getSurroundingRectangle(xb_up_actualTabular)

        playTransform(a, b, c, d, e, f)

        xn_up_tabularNotation = tabularNotation[0][3:5]
        xn_up_tabularNotationEquivalet = tabularNotationEquivalet[0][3:5]
        xn_up_actualTabular = actualTabular[0][1:7]

        g = self.getSurroundingRectangle(xn_up_tabularNotation)
        h = self.getSurroundingRectangle(xn_up_tabularNotationEquivalet)
        i = self.getSurroundingRectangle(xn_up_actualTabular)

        playTransform(d, e, f, g, h, i)

        rhs_up_tabularNotation = tabularNotation[0][5:8]
        rhs_up_tabularNotationEquivalet = tabularNotationEquivalet[0][5:8]
        rhs_up_actualTabular = actualTabular[0][13:16]

        j = self.getSurroundingRectangle(rhs_up_tabularNotation)
        k = self.getSurroundingRectangle(rhs_up_tabularNotationEquivalet)
        l = self.getSurroundingRectangle(rhs_up_actualTabular)

        playTransform(g, h, i, j, k, l)


        z_left_tabularNotation = tabularNotation[0][8:9]
        z_left_tabularNotationEquivalet = tabularNotationEquivalet[0][8:9]
        z_left_actualTabular = actualTabular[0][16:17]

        m = self.getSurroundingRectangle(z_left_tabularNotation)
        n = self.getSurroundingRectangle(z_left_tabularNotationEquivalet)
        o = self.getSurroundingRectangle(z_left_actualTabular)

        playTransform(j, k, l, m, n, o)

        one_below_z_tabularNotation = tabularNotation[0][9:10]
        one_below_z_tabularNotationEquivalet = tabularNotationEquivalet[0][9:10]
        one_below_z_actualTabular = actualTabular[0][17:18]

        p = self.getSurroundingRectangle(one_below_z_tabularNotation)
        q = self.getSurroundingRectangle(one_below_z_tabularNotationEquivalet)
        r = self.getSurroundingRectangle(one_below_z_actualTabular)

        playTransform(m, n, o, p, q, r)

        zero_below_xb_tabularNotation = tabularNotation[0][10:11]
        zero_below_xb_tabularNotationEquivalet = tabularNotationEquivalet[0][10:11]
        zero_below_xb_actualTabular = actualTabular[0][23:26]

        s = self.getSurroundingRectangle(zero_below_xb_tabularNotation)
        t = self.getSurroundingRectangle(zero_below_xb_tabularNotationEquivalet)
        u = self.getSurroundingRectangle(zero_below_xb_actualTabular)

        playTransform(p, q, r, s, t, u)

        zjcj_tabularNotation = tabularNotation[0][11:16]
        zjcj_tabularNotationEquivalet = tabularNotationEquivalet[0][11:20]
        zjcj_actualTabular = actualTabular[0][18:23]

        v = self.getSurroundingRectangle(zjcj_tabularNotation)
        w = self.getSurroundingRectangle(zjcj_tabularNotationEquivalet)
        x = self.getSurroundingRectangle(zjcj_actualTabular)

        playTransform(s, t, u, v, w, x)

        z0_tabularNotation = tabularNotation[0][16:18]
        z0_tabularNotationEquivalet = tabularNotationEquivalet[0][20:22]
        z0_actualTabular = actualTabular[0][26:27]

        y = self.getSurroundingRectangle(z0_tabularNotation)
        z = self.getSurroundingRectangle(z0_tabularNotationEquivalet)
        aa = self.getSurroundingRectangle(z0_actualTabular)

        playTransform(v, w, x, y, z, aa)

        xb_left_tabularNotation = tabularNotation[0][23:25]
        xb_left_tabularNotationEquivalet = tabularNotationEquivalet[0][27:29]
        xb_left_actualTabular_1 = actualTabular[0][36:38]
        xb_left_actualTabular_2 = actualTabular[0][55:57]
        xb_left_actualTabular_3 = actualTabular[0][75:77]

        ab = self.getSurroundingRectangle(xb_left_tabularNotation)
        ac = self.getSurroundingRectangle(xb_left_tabularNotationEquivalet)
        ad = self.getSurroundingRectangle([xb_left_actualTabular_1, xb_left_actualTabular_2, xb_left_actualTabular_3])

        playTransform(y, z, aa, ab, ac, ad)

        zero_below_z_tabularNotation = tabularNotation[0][25:26]
        zero_below_z_tabularNotationEquivalet = tabularNotationEquivalet[0][29:30]
        zero_below_z_actualTabular_1 = actualTabular[0][38:39]
        zero_below_z_actualTabular_2 = actualTabular[0][57:58]
        zero_below_z_actualTabular_3 = actualTabular[0][77:78]

        ae = self.getSurroundingRectangle(zero_below_z_tabularNotation)
        af = self.getSurroundingRectangle(zero_below_z_tabularNotationEquivalet)
        ag = self.getSurroundingRectangle([zero_below_z_actualTabular_1, zero_below_z_actualTabular_2, zero_below_z_actualTabular_3])

        playTransform(ab, ac, ad, ae, af, ag)

        one_below_xb_tabularNotation = tabularNotation[0][26:27]
        one_below_xb_tabularNotationEquivalet = tabularNotationEquivalet[0][30:31]
        one_below_xb_actualTabular_1 = actualTabular[0][42:45]
        one_below_xb_actualTabular_2 = actualTabular[0][62:65]
        one_below_xb_actualTabular_3 = actualTabular[0][82:85]

        ah = self.getSurroundingRectangle(one_below_xb_tabularNotation)
        ai = self.getSurroundingRectangle(one_below_xb_tabularNotationEquivalet)
        aj = self.getSurroundingRectangle([one_below_xb_actualTabular_1, one_below_xb_actualTabular_2, one_below_xb_actualTabular_3])

        playTransform(ae, af, ag, ah, ai, aj)


        yj_tabularNotation = tabularNotation[0][27:29]
        yj_tabularNotationEquivalet = tabularNotationEquivalet[0][31:35]
        yj__actualTabular_1 = actualTabular[0][39:42]
        yj__actualTabular_2 = actualTabular[0][58:62]
        yj__actualTabular_3 = actualTabular[0][78:82]

        ak = self.getSurroundingRectangle(yj_tabularNotation)
        al = self.getSurroundingRectangle(yj_tabularNotationEquivalet)
        am = self.getSurroundingRectangle([yj__actualTabular_1, yj__actualTabular_2, yj__actualTabular_3])

        playTransform(ah, ai, aj, ak, al, am)

        b_tabularNotation = tabularNotation[0][29:30]
        b_tabularNotationEquivalet = tabularNotationEquivalet[0][35:36]
        b_actualTabular_1 = actualTabular[0][45:46]
        b_actualTabular_2 = actualTabular[0][65:66]
        b_actualTabular_3 = actualTabular[0][85:86]

        an = self.getSurroundingRectangle(b_tabularNotation)
        ao = self.getSurroundingRectangle(b_tabularNotationEquivalet)
        ap = self.getSurroundingRectangle([b_actualTabular_1, b_actualTabular_2, b_actualTabular_3])

        playTransform(ak, al, am, an, ao, ap)
    
        

        


    def getSurroundingRectangle(self, mobject_list):
        mobject_group = VGroup(
            *mobject_list
        )

        discre_color_selector_after_every_three = int(self.color_selector/3)

        sr = SurroundingRectangle(
            mobject_group,
            color=self.colors[discre_color_selector_after_every_three],
            fill_opacity=0.15
        )
        
        self.color_selector += 1

        return sr