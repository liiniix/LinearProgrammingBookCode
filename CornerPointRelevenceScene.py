from manim import *
from enum import Enum


isAnimate = False

class SolutionType(Enum):
    SINGLESOLUTION = 1
    LINESOLUTION = 2
    UNBOUNDEDSOLUTION = 3

IntendedSolutionType = SolutionType.SINGLESOLUTION

def plotConstraintsOnAxesAndReturn(axes):
    if IntendedSolutionType == SolutionType.SINGLESOLUTION or IntendedSolutionType == SolutionType.LINESOLUTION:

        # First Constraint
        firstConstraintEquation = MathTex(
            r"3x_1 + x_2 \le 4",
            color = RED_A
        )
        firstConstraintPlot = axes.plot(lambda x: 4 - 3*x, x_range=[0, 4./3., 1], color=YELLOW)
        firstConstraintRegion = axes.get_area(firstConstraintPlot, [0, 4./3.], color=RED_A, opacity=0.6)
        firstConstraintEquation.move_to([-2, 2, 0]) #.set_color_by_tex("x", YELLOW)

        # Second Constraint
        secondConstraintEquation = MathTex(
            r"x_1 + 3x_2 \le 4",
            color = RED_A
        )
        secondConstraintPlot = axes.plot(lambda x: (4 - x)/3, x_range=[0, 4, 1], color=YELLOW)
        secondConstraintRegion = axes.get_area(secondConstraintPlot, [0, 4], color=RED_A, opacity=0.6)
        secondConstraintEquation.move_to([2,-1,0])

    elif IntendedSolutionType == SolutionType.UNBOUNDEDSOLUTION:
        # First Constraint
        firstConstraintEquation = MathTex(
            r"x_1 - 2x_2 \le 1",
            color = RED_A
        )
        firstConstraintPlot = axes.plot(lambda x: (x - 1)/2, x_range=[1, 10, 1], color=YELLOW)
        firstConstraintRegion = axes.get_area(firstConstraintPlot, [1, 10], color=RED_A, opacity=0.6)
        firstConstraintEquation.move_to([2,-1,0]) #.set_color_by_tex("x", YELLOW)

        # Second Constraint
        secondConstraintEquation = MathTex(
            r"x_1 - x_2 \le 0",
            color = RED_A
        )
        secondConstraintPlot = axes.plot(lambda x: x, x_range=[0, 10, 1], color=YELLOW)
        secondConstraintRegion = axes.get_area(secondConstraintPlot, [0, 10], color=RED_A, opacity=0.6)
        secondConstraintEquation.move_to([0, 2, 0])

    
    return (axes,
            firstConstraintEquation,
            firstConstraintPlot,
            firstConstraintRegion,
            secondConstraintEquation,
            secondConstraintPlot,
            secondConstraintRegion)


class CornerPointRelevence(ThreeDScene):
    def GenerateObjectiveFunctionZValue(self, u, v):

        if IntendedSolutionType in [SolutionType.SINGLESOLUTION, SolutionType.UNBOUNDEDSOLUTION]:
            return np.array([u, v, 1 + u + v])
        
        return np.array([u, v, 2 + 2*v])

    def construct(self):

        axes = ThreeDAxes()
        axesLabels = axes.get_axis_labels(
            Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )
        if IntendedSolutionType == SolutionType.SINGLESOLUTION:
            problemText = MathTex(
                r"\text{Max } & z = 1 + x_1 + x_2 \\ \text{Sub To }& 3x_1 + x_2 \le 4 \\ & x_1 + 3x_2 \le 4\\ & x_1, x_2 \ge 0"
            ).scale(.5)

        elif IntendedSolutionType == SolutionType.LINESOLUTION:
            problemText = MathTex(
                r"\text{Min } & z = 2 + 2x_1 \\ \text{Sub To }& 3x_1 + x_2 \le 4 \\ & x_1 + 3x_2 \le 4\\ & x_1, x_2 \ge 0"
            ).scale(.5)

        elif IntendedSolutionType == SolutionType.UNBOUNDEDSOLUTION:
            problemText = MathTex(
                r"\text{Max } & z = 1 + x_1 + x_2 \\ \text{Sub To }& x_1 - 2x_2 \le 1 \\ & x_1 - x_2 \le 0\\ & x_1, x_2 \ge 0"
            ).scale(.5)

        self.add_fixed_in_frame_mobjects(problemText)
        problemText.move_to(axes.c2p(-6., 0.8))

        # Objective Function
        
        objectiveFunctionEquation = MathTex(
            r"z = 1 + x_1 + x_2" if IntendedSolutionType in [SolutionType.SINGLESOLUTION, SolutionType.UNBOUNDEDSOLUTION]
            else r"z = 2 + 2x_2",
            color = DARK_BLUE
        )
        objectiveFunctionEquation.move_to([-2, -1.5, 0])

        objectiveFunctionSurface = Surface(
            lambda u, v: axes.c2p(*self.GenerateObjectiveFunctionZValue(u, v)),
            u_range=[0, 10],
            v_range=[0, 10],
            resolution=8,
            checkerboard_colors=False,
            fill_color=BLUE_E
        ).set_opacity(.95)

        (axes,
        firstConstraintEquation,
        firstConstraintPlot,
        firstConstraintRegion,
        secondConstraintEquation,
        secondConstraintPlot,
        secondConstraintRegion) = plotConstraintsOnAxesAndReturn(axes)

        if IntendedSolutionType == SolutionType.SINGLESOLUTION:
        
            solutionPointInFeasibleRegion = Dot(axes.c2p(1., 1.), radius=.02, stroke_width=0, fill_opacity=1.0, color=YELLOW)
            solutionPointInObjective = Dot(axes.c2p(1., 1., 3.), radius=.02, stroke_width=0, fill_opacity=1.0, color=YELLOW)
            solutionPointInFeasibleRegionObjectiveLine = Line(solutionPointInFeasibleRegion, solutionPointInObjective).set_color(PURE_RED)

        elif IntendedSolutionType == SolutionType.LINESOLUTION:
            firstSolutionPointInFeasibleRegion = Dot(axes.c2p(0., 0.), radius=.02, stroke_width=0, fill_opacity=1.0, color=YELLOW)
            firstSolutionPointInObjective = Dot(axes.c2p(0., 0., 2.), radius=.02, stroke_width=0, fill_opacity=1.0, color=YELLOW)
            firstSolutionPointInFeasibleRegionToObjectiveLine = Line(firstSolutionPointInFeasibleRegion, firstSolutionPointInObjective)\
                                                                .set_color(PURE_RED)

            secondSolutionPointInFeasibleRegion = Dot(axes.c2p(4./3., 0.), radius=.02, stroke_width=0, fill_opacity=1.0, color=YELLOW)
            secondSolutionPointInObjective = Dot(axes.c2p(4./3., 0., 2.), radius=.02, stroke_width=0, fill_opacity=1.0, color=YELLOW)
            secondSolutionPointInFeasibleRegionToObjectiveLine = Line(secondSolutionPointInFeasibleRegion, secondSolutionPointInObjective)\
                                                                    .set_color(PURE_RED)
            
            lineSolutionInObjectiveLine = Line(firstSolutionPointInObjective, secondSolutionPointInObjective)\
                                            .set_color(PURE_RED)

        elif IntendedSolutionType == SolutionType.UNBOUNDEDSOLUTION:
            pass
            
        if isAnimate:
            self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
            self.play(Create(problemText))
            self.wait()
            self.play(Create(axes),
                      Create(axesLabels)
            )
            self.wait()
            
            self.play(Create(firstConstraintEquation),
                      Create(firstConstraintPlot),
                      Create(firstConstraintRegion))
            self.wait()
            self.play(Create(secondConstraintEquation),
                      Create(secondConstraintPlot),
                      Create(secondConstraintRegion))
            
            self.wait()
            self.move_camera(phi=0 * DEGREES, theta=45 * DEGREES)
            self.wait()
            self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES)
            self.play(Create(objectiveFunctionEquation),
                      Create(objectiveFunctionSurface))
            self.wait()
            if IntendedSolutionType == SolutionType.SINGLESOLUTION:
                self.play(Create(solutionPointInFeasibleRegionObjectiveLine))
                self.wait()

            elif IntendedSolutionType == SolutionType.LINESOLUTION:
                
                self.play(Create(firstSolutionPointInFeasibleRegionToObjectiveLine))
                self.wait()
                
                self.play(Create(secondSolutionPointInFeasibleRegionToObjectiveLine))
                self.wait()
                self.play(Create(lineSolutionInObjectiveLine))
                self.wait()

            elif IntendedSolutionType == SolutionType.UNBOUNDEDSOLUTION:
                pass
            

            # built-in updater which begins camera rotation
            self.begin_ambient_camera_rotation(rate=1.5)
            self.wait(4.5)
            self.stop_ambient_camera_rotation()
            self.wait()
            self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES)
            self.wait()
            return
        
        self.add(axes, axesLabels, objectiveFunctionSurface, firstConstraintPlot, firstConstraintRegion,
                 secondConstraintPlot, secondConstraintRegion, firstConstraintEquation, secondConstraintEquation, objectiveFunctionEquation)
        
        if IntendedSolutionType == SolutionType.SINGLESOLUTION:
            self.add(solutionPointInFeasibleRegionObjectiveLine, solutionPointInObjective, solutionPointInFeasibleRegion)

        elif IntendedSolutionType == SolutionType.LINESOLUTION:
            self.add(firstSolutionPointInFeasibleRegion, firstSolutionPointInObjective, firstSolutionPointInFeasibleRegionToObjectiveLine,
                     secondSolutionPointInFeasibleRegion, secondSolutionPointInObjective, secondSolutionPointInFeasibleRegionToObjectiveLine,
                     lineSolutionInObjectiveLine)
            
        elif IntendedSolutionType == SolutionType.UNBOUNDEDSOLUTION:
            pass

        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)