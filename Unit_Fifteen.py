from big_ol_pile_of_manim_imports import *
import math
class Intro(Scene):
	def construct(self):
		ChapterText = TextMobject("Chapter 15: Acid-Base Equilibria")
		ChapterText.scale(.75)
		self.add(ChapterText)
		self.play(Write(ChapterText))
		self.wait(1)
		self.play(ApplyMethod(ChapterText.to_corner,UL))
		self.wait(2)
		self.play(FadeOut(ChapterText))
class CIE(Scene):
	def construct(self):
		Socratic1 = TextMobject("1. Define common ion effect.")
		Socratic1.scale(.5)

		NaFEquil = TexMobject(r"NaF", r"\rightleftharpoons", r"Na_{(aq)}^{+}", r"+", r"F_{(aq)}^{-}")
		NaFEquil.scale(.5)
		NaFEquil.shift(UP*2+LEFT*3)
		NaFEquil[0].set_color(BLUE)
		NaFEquil[2].set_color(ORANGE)
		NaFEquil[4].set_color(PURPLE)

		HFEquil = TexMobject(r"HF", r"\rightleftharpoons", r"H_{(aq)}^{+}", r"+", r"F_{(aq)}^{-}")
		HFEquil.scale(.5)
		HFEquil.shift(UP*2+RIGHT*3)
		HFEquil[0].set_color(BLUE)
		HFEquil[2].set_color(ORANGE)
		HFEquil[4].set_color(PURPLE)

		NaFRect = Rectangle(Height = .5, Width = 1, color = BLUE, fill_opacity = 1.0)
		NaFRect.scale(.25)
		NaFRect.shift(UP+LEFT*4)
		NaFRectTxt = TextMobject("NaF")
		NaFRectTxt.scale(.5)
		NaFRectTxt.shift(UP+LEFT*4)

		Na1Rect = Rectangle(Height = .5, Width = .5, color = ORANGE, fill_opacity = 1.0)
		Na1Rect.scale(.15)
		Na1Rect.shift(UP*1.5+LEFT*2.45)
		Na1RectTxt = TexMobject(r"Na_{(aq)}^{+}")
		Na1RectTxt.scale(.35)
		Na1RectTxt.shift(UP*1.5+LEFT*2.45)

		F1Rect = Rectangle(Height = .5, Width = .5, color = PURPLE, fill_opacity = 1.0)
		F1Rect.scale(.15)
		F1Rect.shift(UP*.5+LEFT*2.45)
		F1RectTxt = TexMobject(r"F_{(aq)}^{-}")
		F1RectTxt.scale(.35)
		F1RectTxt.shift(UP*.5+LEFT*2.45)

		HFRect = Rectangle(Height = .5, Width = 1, color = BLUE, fill_opacity = 1.0)
		HFRect.scale(.25)
		HFRect.shift(UP+RIGHT*4)
		HFRectTxt = TextMobject("HF")
		HFRectTxt.scale(.5)
		HFRectTxt.shift(UP+RIGHT*4)

		H1Rect = Rectangle(Height = .5, Width = .5, color = ORANGE, fill_opacity = 1.0)
		H1Rect.scale(.05)
		H1Rect.shift(UP*1.5+RIGHT*2.55)

		F2Rect = Rectangle(Height = .5, Width = .5, color = PURPLE, fill_opacity = 1.0)
		F2Rect.scale(.05)
		F2Rect.shift(UP*.5+RIGHT*2.55)

		NaFNa = Arrow(UP*.9+LEFT*3.65,UP*1.6+LEFT*2.6, color = GREEN)
		NaFF = Arrow(UP*1.1+LEFT*3.65,UP*.4+LEFT*2.6, color = GREEN)

		HFH = Arrow(UP*.9+RIGHT*3.65,UP*1.6+RIGHT*2.6, color = GREEN)
		HFF = Arrow(UP*1.1+RIGHT*3.65,UP*.4+RIGHT*2.6, color = GREEN)

		F3Rect = Rectangle(Height = .5, Width = .5, color = PURPLE, fill_opacity = 1.0)
		F3Rect.scale(.15)
		F3Rect.shift(UP*.5+LEFT*2.45)
		F3RectTxt = TexMobject(r"F_{(aq)}^{-}")
		F3RectTxt.scale(.35)
		F3RectTxt.shift(UP*.5+LEFT*2.45)
		F3 = VGroup(F3Rect,F3RectTxt)

		Add = TextMobject("+")

		self.add(Socratic1)
		self.play(Write(Socratic1))
		self.wait(3)
		self.play(FadeOut(Socratic1))
		self.wait(6)
		self.play(Write(NaFEquil))
		self.wait(3.5)
		self.play(Write(HFEquil))
		self.wait(6)
		self.play(DrawBorderThenFill(NaFRect))
		self.play(Write(NaFRectTxt))
		self.wait(2)
		self.play(ShowCreation(NaFNa),DrawBorderThenFill(Na1Rect),ShowCreation(NaFF),DrawBorderThenFill(F1Rect))
		self.play(Write(Na1RectTxt),Write(F1RectTxt))
		self.play(DrawBorderThenFill(HFRect))
		self.play(Write(HFRectTxt))
		self.wait(1)
		self.play(ApplyMethod(F3.shift,RIGHT*4))
		Add.next_to(F3,RIGHT)
		Add.shift(LEFT*.1)
		self.play(Write(Add))
		self.wait(6)
		self.play(ShowCreation(HFF),DrawBorderThenFill(F2Rect))
		self.play(ShowCreation(HFH),DrawBorderThenFill(H1Rect))
		self.wait(9)

		self.play(FadeOut(NaFEquil),FadeOut(HFEquil),FadeOut(NaFRect),FadeOut(NaFRectTxt),FadeOut(NaFNa),FadeOut(Na1Rect),FadeOut(Na1RectTxt),
			FadeOut(NaFF),FadeOut(F1Rect),FadeOut(F1RectTxt),FadeOut(HFRect),FadeOut(HFRectTxt),FadeOut(F3),FadeOut(HFF),FadeOut(F2Rect),FadeOut(HFH),FadeOut(H1Rect),FadeOut(Add))
		self.wait()
class PPA(Scene):
	def construct(self):
		Socratic2 = VGroup(
			TexMobject(r"\text{2. Polyprotic acids typically have K}",r"_{a}",r"\text{ values that decrease significantly after}"),
			TexMobject(r"\text{each H}", "^{+}", r"\text{is removed. How does the common }",r"\text{ion effect explain this phenomenon?}")
			)
		Socratic2.scale(.5)
		for x in range(1):
			Socratic2[x+1].next_to(Socratic2[x],DOWN)
		H3PO4 = VGroup(Square(fill_opacity=1,color=BLUE),TexMobject(r"H_{3}PO_{4}"))
		H3PO4.shift(UP*2,LEFT*4)
		H2PO4 = VGroup(Square(fill_opacity=1,color=BLUE),TexMobject(r"H_{2}PO_{4}^{-}"))
		H2PO4.shift(UP*0,LEFT*1)
		H2PO4.scale(.5)
		HPO4 = VGroup(Square(fill_opacity=1,color=BLUE),TexMobject(r"HPO_{4}^{-2}"))
		HPO4.shift(DOWN*1,RIGHT*1)
		HPO4.scale(.25)
		PO4 = VGroup(Square(fill_opacity=1,color=BLUE),TexMobject(r"PO_{4}^{-3}"))
		PO4.shift(DOWN*1.5,RIGHT*2)
		PO4.scale(.125)
		H3PO4_H2PO4 = VGroup(Line(UP*.9+LEFT*4,LEFT*4),Line(LEFT*4,LEFT*1.6),Line(LEFT*1.6,UP*.35355+LEFT*(1.6+.35355)),Line(LEFT*1.6,DOWN*.35355+LEFT*(1.6+.35355)))
		H2PO4_HPO4 = VGroup(Line(DOWN*.55+LEFT*1,DOWN*1+LEFT*1),Line(DOWN*1+LEFT*1,DOWN*1+RIGHT*.7),Line(DOWN*1+RIGHT*.7,DOWN*(1-.17678)+RIGHT*(.7-.17678)),Line(DOWN*1+RIGHT*.7,DOWN*(1+.17678)+RIGHT*(.7-.17678)))
		HPO4_PO3 = VGroup(Line(DOWN*1.275+RIGHT,DOWN*1.5+RIGHT),Line(DOWN*1.5+RIGHT,DOWN*1.5+RIGHT*1.85),Line(DOWN*1.5+RIGHT*1.85,DOWN*(1.5-.088388)+RIGHT*(1.85-.088388)),Line(DOWN*1.5+RIGHT*1.85,DOWN*(1.5+.088388)+RIGHT*(1.85-.088388)))
		H1Release = VGroup(Square(fill_opacity=1,color=ORANGE),TexMobject(r"H^{+}"))
		H1Release.shift(UP*2,LEFT*1)
		H1Release.scale(.5)
		H2Release = VGroup(Square(fill_opacity=1,color=ORANGE),TexMobject(r"H^{+}"))
		H2Release.shift(RIGHT)
		H2Release.scale(.25)
		H3Release = VGroup(Square(fill_opacity=1,color=ORANGE),TexMobject(r"H^{+}"))
		H3Release.shift(DOWN,RIGHT*2)
		H3Release.scale(.125)
		H3PO4_H1 = VGroup(
			Line(UP*2+LEFT*2.9,UP*2+LEFT*1.6),
			Line(UP*2+LEFT*1.6,UP*(2+.35355)+LEFT*(1.6+.35355)),
			Line(UP*2+LEFT*1.6,UP*(2-.35355)+LEFT*(1.6+.35355))
			)
		H2PO4_H2 = VGroup(
			Line(LEFT*.45,RIGHT*.7),
			Line(RIGHT*.7,UP*.17678+RIGHT*(.7-.17678)),
			Line(RIGHT*.7,DOWN*.17678+RIGHT*(.7-.17678))
			)
		HPO4_H3 = VGroup(
			Line(DOWN+RIGHT*1.25,DOWN+RIGHT*1.85),
			Line(DOWN+RIGHT*1.85,DOWN*(1-.088388)+RIGHT*(1.85-.088388)),
			Line(DOWN+RIGHT*1.85,DOWN*(1+.088388)+RIGHT*(1.85-.088388))
			)
		self.add(Socratic2)
		self.play(Write(Socratic2))
		self.wait(5)
		self.play(FadeOut(Socratic2))
		self.wait(2)
		self.play(DrawBorderThenFill(H3PO4))
		self.wait(2)
		self.play(ShowCreation(H3PO4_H2PO4))
		self.play(ShowCreation(H3PO4_H1))
		self.play(DrawBorderThenFill(H2PO4))
		self.play(DrawBorderThenFill(H1Release))
		self.wait(2)
		self.play(ShowCreation(H2PO4_HPO4))
		self.play(ShowCreation(H2PO4_H2))
		self.play(DrawBorderThenFill(HPO4))
		self.play(DrawBorderThenFill(H2Release))
		self.wait(13)
		self.play(DrawBorderThenFill(HPO4_PO3))
		self.play(DrawBorderThenFill(HPO4_H3))
		self.play(DrawBorderThenFill(PO4))
		self.play(DrawBorderThenFill(H3Release))
		self.wait(1)
		self.play(FadeOut(H3PO4),FadeOut(H3PO4_H2PO4),FadeOut(H3PO4_H1),FadeOut(H2PO4),FadeOut(H1Release),FadeOut(H2PO4_HPO4),FadeOut(H2PO4_H2),FadeOut(HPO4),FadeOut(H2Release),FadeOut(HPO4_PO3),FadeOut(HPO4_H3),FadeOut(PO4),FadeOut(H3Release))
		self.wait()
class BFS(Scene):
	def construct(self):
		Socratic3 = TextMobject("3. What is a buffered solution and how is a buffered solution made?")
		Socratic3.scale(.5)
		Items = VGroup(
			TextMobject("Weak Acid: HF"),
			TextMobject("Salt: NaF"),
			TexMobject(r"\text{Weak Base: NH}", r"_{3}"),
			TexMobject(r"\text{Salt: NH}",r"_{4}",r"\text{Cl}")
			)
		Items.scale(.5)
		Items[0].shift(UP*2,LEFT*4)
		Items[1].next_to(Items[0],DOWN)
		Items[2].shift(UP*2,RIGHT*4)
		Items[3].next_to(Items[2],DOWN)
		self.add(Socratic3)
		self.play(Write(Socratic3))
		self.wait(3)
		self.play(FadeOut(Socratic3))
		self.wait(7)
		self.play(Write(Items))
		self.wait(3)
		self.play(FadeOut(Items))
		self.wait()
class AHA(Scene):
	def construct(self):
		Socratic4 = VGroup(
			TexMobject(r"\text{4. Why must [A}", r"^{-}",r"\text{] and [HA] be relatively high compared}"),
			TexMobject(r"\text{to the amount of [H}",r"^{+}",r"\text{] or [OH}",r"^{-}",r"\text{] added"),
			TexMobject(r"\text{in order for a buffer to be effective?}")
			)
		Socratic4.scale(.5)
		for x in range(2):
			Socratic4[x+1].next_to(Socratic4[x],DOWN)
		AcidDis = TexMobject(r"HA \rightleftharpoons H_{(aq)}^{+} + A_{(aq)}^{-}")
		AcidDis.scale(.5)
		AcidDis.shift(UP*3)
		KaEq1 = TexMobject(r"K_{a} = \frac{[H^{+}][A^{-}]}{[HA]}")
		KaEq1.scale(.5)
		KaEq1.shift(UP*2)
		KaEq2 = TexMobject(r"[HA]\cdot K_{a} = [H^{+}]\cdot [A^{-}]")
		KaEq2.scale(.5)
		KaEq3 = TexMobject(r"\frac{[HA]}{[A^{-}]}",r"\cdot", r"K_{a}", r"= [H^{+}]")
		KaEq3.scale(.5)
		KaEq2.next_to(KaEq1,DOWN)
		KaEq3.next_to(KaEq2,DOWN)

		AcidBase = TexMobject(r"HA", r"+",r" OH^{-}",r" \rightleftharpoons",r" H_{2}O",r"+",r" A^{-}")
		AcidBase.scale(.5)
		AcidBase.shift(UP*2)
		Arrow = TexMobject(r"\rightarrow")
		Arrow.scale(.5)
		Arrow.move_to(AcidBase[3])

		I = TextMobject("I",color = RED)
		C = TextMobject("C",color = YELLOW)
		E = TextMobject("E",color = PURPLE)

		I.scale(.5)
		C.scale(.5)
		E.scale(.5)

		I.shift(LEFT*5.5)
		C.next_to(I,DOWN)
		E.next_to(C,DOWN)

		Initial = VGroup(
			TexMobject(r"[HA]"),
			TexMobject(r"[OH",r"^{-}",r"]"),
			TexMobject(r"[H",r"_{2}",r"O]"),
			TexMobject(r"[A",r"^{-}",r"]"),
		)

		Initial[0].scale(.5)
		Initial[1].scale(.5)
		Initial[2].scale(.5)
		Initial[3].scale(.5)

		Initial[0].shift(LEFT*4)
		Initial[1].shift(LEFT*2)
		Initial[2].shift(RIGHT*2)
		Initial[3].shift(RIGHT*4)

		HA_OH = TexMobject(r"[HA] > [OH",r"^{-}",r"]")
		HA_OH.scale(.5)
		HA_OH.shift(UP*2)
		Change = VGroup(
			TexMobject(r"-[OH",r"^{-}",r"]"),
			TexMobject(r"-[OH",r"^{-}",r"]"),
			TexMobject(r"+[OH",r"^{-}",r"]"),
			TexMobject(r"+[OH",r"^{-}",r"]"),
		)

		Change.scale(.5)
		for x in range(4):
			Change[x].next_to(Initial[x],DOWN)

		End = VGroup(
			TexMobject(r"[HA]-[OH",r"^{-}",r"]"),
			TexMobject(r"0"),
			TexMobject(r"[H",r"_{2}",r"O]+[OH",r"^{-}",r"]"),
			TexMobject(r"[A",r"^{-}",r"]+[OH",r"^{-}",r"]")
			)
		End.scale(.5)
		for x in range(4):
			End[x].next_to(Change[x],DOWN)

		FinalKaEq = TexMobject(r"\frac{[HA]-[OH^{-}]}{[A^{-}]+[OH^{-}]}",r"\cdot" ,r"K_{a}", r"= [H^{+}]")
		FinalKaEq.scale(.5)
		FinalKaEq[2].set_color(GREEN)

		Ratio = TexMobject(r"\frac{[HA]-[OH^{-}]}{[A^{-}]+[OH^{-}]}")
		Ratio.scale(.5)

		RatioEx1 = TexMobject(r"\frac{1.00-[OH^{-}]}{1.00+[OH^{-}]}")
		RatioEx1.scale(.5)
		RatioEx1.next_to(Ratio,DOWN)
		RatioEx1.shift(LEFT*3)

		RatioEx11 = TexMobject(r"\frac{1.00-0.05}{1.00+0.05}")
		RatioEx11.scale(.5)
		RatioEx11.next_to(RatioEx1,DOWN)

		RatioEx12 = TexMobject(r"\approx .905")
		RatioEx12.scale(.5)
		RatioEx12.next_to(RatioEx11,DOWN)

		RatioEx2 = TexMobject(r"\frac{1.00-[OH^{-}]}{1.00+[OH^{-}]}")
		RatioEx2.scale(.5)
		RatioEx2.next_to(Ratio,DOWN)
		RatioEx2.shift(RIGHT*3)

		RatioEx21 = TexMobject(r"\frac{1.00-0.20}{1.00+0.20}")
		RatioEx21.scale(.5)
		RatioEx21.next_to(RatioEx2,DOWN)

		RatioEx22 = TexMobject(r"\approx .667")
		RatioEx22.scale(.5)
		RatioEx22.next_to(RatioEx21,DOWN)

		self.add(Socratic4)
		self.play(Write(Socratic4))
		self.wait(3)
		self.play(FadeOut(Socratic4))
		self.wait(7)
		self.play(Write(AcidDis))
		self.wait(2)
		self.play(Write(KaEq1))
		self.wait(2)
		self.play(TransformFromCopy(KaEq1,KaEq2))
		self.play(TransformFromCopy(KaEq2,KaEq3))
		self.wait(2)
		self.play(FadeOut(KaEq1),FadeOut(KaEq2),FadeOut(AcidDis))
		self.wait(2)
		self.play(FadeToColor(KaEq3[2],GREEN))
		self.wait(11)
		self.play(Indicate(KaEq3[0]),Indicate(KaEq3[3]))
		self.wait(3)
		self.play(ApplyMethod(KaEq3.to_corner,UR))
		self.wait(2)
		self.play(Write(AcidBase))
		self.wait(7)
		self.play(ReplacementTransform(AcidBase[3],Arrow))
		self.wait(2)
		self.play(Write(I),Write(C),Write(E))
		self.play(ApplyMethod(AcidBase[0].move_to,UP*.5+LEFT*4),ApplyMethod(AcidBase[1].move_to,UP*.5+LEFT*3),ApplyMethod(AcidBase[2].move_to,UP*.5+LEFT*2),ApplyMethod(Arrow.move_to,UP*.5),ApplyMethod(AcidBase[4].move_to,UP*.5+RIGHT*2),ApplyMethod(AcidBase[5].move_to,UP*.5+RIGHT*3),ApplyMethod(AcidBase[6].move_to,UP*.5+RIGHT*4))
		self.wait(2)
		self.play(Write(Initial[0]))
		self.wait(2)
		self.play(Write(Initial[1]))
		self.wait(2)
		self.play(Write(Initial[2]))
		self.wait(2)
		self.play(Write(Initial[3]))
		self.wait(7)
		self.play(Write(HA_OH))
		self.wait(2)
		self.play(ApplyMethod(HA_OH.to_corner,UL))
		self.wait(6)
		self.play(Write(Change[0:2]))
		self.wait(2)
		self.play(Write(Change[2:4]))
		self.wait(6)
		self.play(Write(End[0:2]))
		self.wait(2)
		self.play(Write(End[2:4]))
		self.wait(.5)
		self.play(Indicate(End[0]),Indicate(End[3]))
		self.wait(2)
		self.play(ApplyMethod(End[0].shift,DOWN),ApplyMethod(End[3].shift,DOWN))
		self.play(FadeOut(Initial),FadeOut(Change),FadeOut(I),FadeOut(C),FadeOut(E),FadeOut(End[1:3]),FadeOut(HA_OH),FadeOut(AcidBase[0:3]),FadeOut(AcidBase[4:len(AcidBase)]),FadeOut(Arrow))
		self.wait(2)
		self.play(ApplyMethod(End[0].move_to,UP*2+LEFT*2),ApplyMethod(End[3].move_to,UP+LEFT*2),ApplyMethod(KaEq3.move_to,UP*1.5+RIGHT))
		self.wait(13)
		self.play(Write(FinalKaEq))
		self.wait(2)
		self.play(FadeOut(End[0]),FadeOut(End[3]),ApplyMethod(KaEq3.shift,LEFT*1.5))
		self.wait(2)
		self.play(Indicate(KaEq3[0]),Indicate(KaEq3[3]))
		self.wait(2)
		self.play(Indicate(FinalKaEq[0]),Indicate(FinalKaEq[3]))
		self.wait(2)
		self.play(FadeOut(KaEq3),FadeOut(FinalKaEq[1:4]),ApplyMethod(FinalKaEq[0].move_to,UP*0+RIGHT*0))
		self.wait(9)
		self.play(TransformFromCopy(FinalKaEq[0],RatioEx1))
		self.wait(7)
		self.play(TransformFromCopy(RatioEx1,RatioEx11))
		self.play(TransformFromCopy(RatioEx11,RatioEx12))
		self.wait(2)
		self.play(TransformFromCopy(FinalKaEq[0],RatioEx2))
		self.wait(7)
		self.play(TransformFromCopy(RatioEx2,RatioEx21))
		self.play(TransformFromCopy(RatioEx21,RatioEx22))
		self.wait(7)
		self.play(FadeOut(FinalKaEq[0]),FadeOut(RatioEx1),FadeOut(RatioEx11),FadeOut(RatioEx12),FadeOut(RatioEx2),FadeOut(RatioEx21),FadeOut(RatioEx22))
		self.wait(2)
class HHE(Scene):
	def construct(self):
		Socratic5 = TextMobject("5. What is the Henderson-Hasselbach equation and what is it used for?")
		Socratic5.scale(.5)
		KaEqs = VGroup(
			TexMobject(r"\frac{[HA]}{[A^{-}]}",r"\cdot", r"K_{a}", r"= [H^{+}]"), #KaEq
			TexMobject(r"\log(\frac{[HA]}{[A^{-}]}\cdot K_{a}) = \log([H^{+}])"), #KaEqLog
			TexMobject(r"\log(\frac{[HA]}{[A^{-}]}) + \log(K_{a}) = \log([H^{+}])"), #KaEqLogSim
			TexMobject(r"-\log(\frac{[HA]}{[A^{-}]}) - \log(K_{a}) = -\log([H^{+}])"), #KaLogNegSim
			TexMobject(r"-\log(\frac{[HA]}{[A^{-}]}) + ",r"pK_{a}",r" = ",r"pH"), #KaEqLogNegSim
			TexMobject(r"-\log([H^{+}]) = pH"), #LogH_pH
			TexMobject(r"-\log(K_{a}) = pK_{a}") #LogK_pK
		)
		KaEqs.scale(.5)
		KaEqs.shift(UP*3)
		for x in range(6):
			KaEqs[x+1].next_to(KaEqs[x],DOWN)
		KaEqs[5].to_corner(UL)
		KaEqs[6].next_to(KaEqs[5],DOWN)
		self.add(Socratic5)
		self.play(Write(Socratic5))
		self.wait(2)
		self.play(FadeOut(Socratic5))
		self.wait(6)
		self.play(Write(KaEqs[0]))
		self.wait(4)
		for x in range(3):
			self.play(TransformFromCopy(KaEqs[x],KaEqs[x+1]))
			self.wait(2)
		self.wait(2)
		self.play(Write(KaEqs[5:7]))
		self.wait(2)
		self.play(TransformFromCopy(KaEqs[3],KaEqs[4]))
		self.wait(2)
		self.play(FadeToColor(KaEqs[4][1],GREEN))
		self.wait(2)
		self.play(Indicate(KaEqs[4][0]),Indicate(KaEqs[4][3]))
		self.wait(7)
		self.play(FadeOut(KaEqs))
		self.wait(2)
class CTF(Scene):
	def construct(self):
		Socratic6 = TextMobject("6. Complete the following:")
		Socratic6.scale(.5)

		Fill1 = TextMobject("The pH of a buffered solution is determined by")
		Fill1.scale(.5)
		Fill1.shift(UP*2)

		HHA = TexMobject(r"-\log(\frac{[HA]}{[A^{-}]}) + ",r"pK_{a}",r" = ",r"pH")
		HHA.scale(.5)

		self.add(Socratic6)
		self.play(Write(Socratic6))
		self.wait(2)
		self.play(FadeOut(Socratic6))
		self.wait(2)
		self.play(Write(Fill1))
		self.play(Write(HHA))
		self.wait(2)
		self.play(FadeToColor(HHA[1],GREEN))
		self.wait(2)
		self.play(Indicate(HHA[3]),Indicate(HHA[0]))
		self.wait(2)
		self.play(FadeOut(HHA),FadeOut(Fill1))
		self.wait(2)
class PHPK(Scene):
	def construct(self):
		Socratic7 = VGroup(
			TextMobject("7. When choosing a weak acid buffer, the pH should be as"),
			TexMobject(r"\text{close as possible to the pK}",r"_{a}",r"\text{ of the weak acid. Why?")
			)
		Socratic7.scale(.5)
		Socratic7[1].next_to(Socratic7[0],DOWN)

		PK_PH = VGroup(
			TexMobject(r"pH = \lim_{pK_{a}\rightarrow pH} pK_{a} - \log(\frac{[HA]}{[A^{-}]})"),
			TexMobject(r"pH = pH - \log(\frac{[HA]}{[A^{-}]})"),
			TexMobject(r"0 = - \log(\frac{[HA]}{[A^{-}]})"),
			TexMobject(r"0 = \log(\frac{[HA]}{[A^{-}]})"),
			TexMobject(r"10^{0} = \frac{[HA]}{[A^{-}]}"),
			TexMobject(r"1 = \frac{[HA]}{[A^{-}]}")
			)
		PK_PH.scale(.5)
		PK_PH[0].shift(UP*3)
		for x in range(5):
			PK_PH[x+1].next_to(PK_PH[x],DOWN)
		OH_Add = TexMobject(r"\frac{[HA]-[OH^{-}]}{[A^{-}]+[OH^{-}]}",r"\cdot" ,r"K_{a}", r"= [H^{+}]")
		OH_Add.scale(.5)

		Examples = VGroup(
			TexMobject(r"\frac{[HA]}{[A^{-}]} = \frac{1.00}{1.00}"),
			TexMobject(r"\frac{1.00-[OH^{-}]}{1.00+[OH^{-}]}"),
			TexMobject(r"\frac{1.00-0.01}{1.00+0.01}"),
			TexMobject(r"\frac{0.99}{1.01}"),
			TexMobject(r"\approx .980"),
			TexMobject(r"\frac{[HA]}{[A^{-}]} = \frac{1.00}{0.01}"),
			TexMobject(r"\frac{1.00-[OH^{-}]}{0.01+[OH^{-}]}"),
			TexMobject(r"\frac{1.00-0.01}{0.01+0.01}"),
			TexMobject(r"\frac{0.99}{0.02}"),
			TexMobject(r"\approx49.5")
			)
		Examples.scale(.5)
		Examples[0].shift(UP+LEFT*3)
		Examples[5].shift(UP+RIGHT*3)
		for x in range(4):
			Examples[x+1].next_to(Examples[x],DOWN)
		for x in range(5,9):
			Examples[x+1].next_to(Examples[x],DOWN)
		self.add(Socratic7)
		self.play(Write(Socratic7))
		self.wait(2)
		self.play(FadeOut(Socratic7))
		self.wait(2)
		self.play(Write(PK_PH[0]))
		self.wait(2)
		for x in range(5):
			self.play(TransformFromCopy(PK_PH[x],PK_PH[x+1]))
		self.wait(4)
		self.play(FadeOut(PK_PH[0:5]))
		self.wait(1)
		self.play(PK_PH[5].move_to,UP*3)
		OH_Add.next_to(PK_PH[5],DOWN)
		self.wait(2)
		self.play(Write(OH_Add))
		self.wait(4)
		self.play(Write(Examples[0]),Write(Examples[5]))
		self.wait(6)
		for x in range(4):
			self.play(TransformFromCopy(Examples[x],Examples[x+1]))
		self.wait(7)
		for x in range(5,9):
			self.play(TransformFromCopy(Examples[x],Examples[x+1]))
		self.wait(2)
		self.play(Indicate(Examples[4]),Indicate(Examples[0]))
		self.wait(2)
		self.play(Indicate(Examples[9]),Indicate(Examples[5]))
		self.wait(8)
		self.play(FadeOut(Examples),FadeOut(OH_Add),FadeOut(PK_PH[5]))
		self.wait(2)

class Socratic8(Scene):
	def construct(self):
		Socratic8 = TextMobject("8. What is a millimole? Why is it used in titrations?")
		Socratic8.scale(.5)
		self.add(Socratic8)
		self.play(Write(Socratic8))
		self.wait(2)
		self.play(FadeOut(Socratic8))
		self.wait(2)
class Socratic8Graph(GraphScene):
	CONFIG = {
	    "y_max" : 13,
	    "y_min" : 0,
	    "x_max" : 200,
	    "x_min" : 0,
	    "y_tick_frequency" : 1,
	    "x_tick_frequency" : 25,
	    "axes_color" : WHITE,
	    "x_axis_label" : "Vol NaOH Added (mL)",
	    "y_axis_label" : "pH",
	}
	def construct(self):
	    self.setup_axes()
	    graph = self.get_graph(lambda x : ((-12/(1+1.5**(x-100)))+13), color = GREEN)
	    vert_line = self.get_vertical_line_to_graph(100,graph,color=BLUE)
	    v_dashed = DashedLine(*vert_line.get_start_and_end(),color= BLUE)
	    intersect = Dot(self.coords_to_point(100,7),color= BLUE)
	    vert_line2 = self.get_vertical_line_to_graph(105,graph,color=BLUE)
	    v_dashed2 = DashedLine(*vert_line2.get_start_and_end(),color=BLUE)
	    intersect2 = Dot(self.coords_to_point(105,11.604),color= BLUE)
	    dx = VGroup(v_dashed,v_dashed2)
	    change = Brace(dx,UP)
	    millimole = TexMobject(r"\text{1 mmol = 10}",r"^{-3}",r"\text{mol}")
	    millimole.scale(.5)
	    MolFormula = VGroup(
	    	TexMobject(r"M = \frac{mol}{L}"),
	    	TexMobject(r"M = \frac{10^{-3}\cdot mol}{10^{-3}\cdot L} "),
	    	TexMobject(r"M = \frac{mmol}{mL}")
	    	)
	    MolFormula.scale(.5)
	    MolFormula.shift(UP)
	    for x in range(len(MolFormula)-1):
	    	MolFormula[x+1].next_to(MolFormula[x],DOWN)

	    self.play(
	        ShowCreation(graph),
	        run_time = 2
	    )
	    self.wait(2)
	    self.play(
	    	ShowCreation(v_dashed),
	    	run_time = 2
	    	)
	    self.play(ShowCreation(intersect))
	    self.wait()
	    self.play(
	    	ShowCreation(v_dashed2),
	    	run_time = 2
	    	)
	    self.play(ShowCreation(intersect2))
	    self.wait()
	    self.play(ShowCreation(change))
	    self.wait()
	    self.play(FadeOut(graph),FadeOut(v_dashed),FadeOut(intersect),FadeOut(v_dashed2),FadeOut(intersect2),FadeOut(change),FadeOut(self.x_axis),FadeOut(self.y_axis))
	    self.wait()
	    self.play(Write(millimole))
	    self.wait(8)
	    self.play(ApplyMethod(millimole.to_corner,UR))
	    self.wait()
	    self.play(Write(MolFormula[0]))
	    self.wait(4)
	    for x in range(len(MolFormula)-1):
	    	self.play(TransformFromCopy(MolFormula[x],MolFormula[x+1]))
	    	self.wait()
	    self.wait(9)
	    self.play(FadeOut(MolFormula),FadeOut(millimole))
	    self.wait()

	def setup_axes(self):
	    GraphScene.setup_axes(self)
	    # Custom parametters
	    self.x_axis.add_numbers(*range(0,225,25))
	    # Y parametters
	    self.y_axis.label_direction = LEFT
	    self.y_axis.add_numbers(*[0,7,13])
	    self.play(Write(self.x_axis),Write(self.y_axis))
class Socratic9(Scene):
	def construct(self):
		Socratic9 = VGroup(
			TextMobject("9. Why is the titration curve for a strong acid and strong base"), 
			TextMobject("so steep near the equivience point")
			)
		Socratic9.scale(.5)
		Socratic9[1].next_to(Socratic9[0],DOWN)
		self.add(Socratic9)
		self.play(Write(Socratic9))
		self.wait(2)
		self.play(FadeOut(Socratic9))
		self.wait(2)
class Socratic9Graph(GraphScene):
	CONFIG = {
	    "y_max" : 13,
	    "y_min" : 0,
	    "x_max" : 200,
	    "x_min" : 0,
	    "y_tick_frequency" : 1,
	    "x_tick_frequency" : 25,
	    "axes_color" : WHITE,
	    "x_axis_label" : "Vol NaOH Added (mL)",
	    "y_axis_label" : "pH",
	}
	def construct(self):
	    self.setup_axes()
	    graph = self.get_graph(lambda x : ((-12/(1+1.5**(x-100)))+13), color = GREEN, x_min=0,x_max=100)
	    graph2 = self.get_graph(lambda x : ((-12/(1+1.5**(x-100)))+13), color = GREEN, x_min=100,x_max=200)
	    BottomHalf = VGroup(Dot(self.coords_to_point(100,1)),Dot(self.coords_to_point(100,6.5)))
	    BottomBrace = Brace(BottomHalf,RIGHT)
	    Equivalence = Dot(self.coords_to_point(100,7),color=BLUE)
	    TopHalf = VGroup(Dot(self.coords_to_point(100,7.5)),Dot(self.coords_to_point(200,13)))
	    TopBrace = Brace(TopHalf,LEFT)
	    h_dashed = DashedLine(self.coords_to_point(0,7),self.coords_to_point(100,7),color = BLUE)


	    self.play(
	        ShowCreation(graph),
	        run_time = 2
	    )
	    self.wait()
	    self.play(ShowCreation(BottomBrace))
	    self.wait()
	    self.play(ShowCreation(h_dashed))
	    self.play(ShowCreation(Equivalence))
	    self.play(Uncreate(h_dashed))
	    self.wait()
	    self.play(
	    	ShowCreation(graph2),
	    	run_time = 2
	    	)
	    self.play(ShowCreation(TopBrace))
	    self.wait(17)
	    self.play(FadeOut(BottomBrace),FadeOut(graph),FadeOut(Equivalence),FadeOut(graph2),FadeOut(TopBrace),FadeOut(self.x_axis),FadeOut(self.y_axis))
	    self.wait()


	def setup_axes(self):
	    GraphScene.setup_axes(self)
	    # Custom parametters
	    self.x_axis.add_numbers(*range(0,225,25))
	    # Y parametters
	    self.y_axis.label_direction = LEFT
	    self.y_axis.add_numbers(*[0,7,13])
	    self.play(Write(self.x_axis),Write(self.y_axis))
class pHG7(Scene):
	def construct(self):
		Socratic10 = VGroup(
			TextMobject("10. Why is the pH at the equivalence point between a"), 
			TextMobject("weak acid and strong base greater than 7?")
			)
		Socratic10.scale(.5)
		Socratic10[1].next_to(Socratic10[0],DOWN)
		WeakAcid_StrongBase = TexMobject(r"\text{HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}",r"\text{ + OH}",r"^{-}",r"\rightleftharpoons",r"\text{C}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}^{-}",r"\text{ +}",r"\text{ H}",r"_{2}",r"\text{O}")
		WeakAcid_StrongBase.scale(.5)
		WeakAcid_StrongBase_Conc = TexMobject(r"\text{mol HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}",r"\text{ = mol OH}",r"^{-}}")
		WeakAcid_StrongBase_Conc.scale(.5)
		WeakAcid_StrongBase_Conc.shift(UP)
		Single_Arrow = TexMobject(r"\rightarrow")
		Single_Arrow.scale(.5)
		Single_Arrow.move_to(WeakAcid_StrongBase[8])
		WeakAcid_StrongBase_Rev = TexMobject(r"\text{C}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}^{-}",r"\text{ + H}",r"_{2}",r"\text{O}",r"\rightleftharpoons",r"\text{HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}",r"\text{ +}",r"\text{ OH}",r"^{-}")
		WeakAcid_StrongBase_Rev.scale(.5)
		#WeakAcid_StrongBase_End = TexMobject(r"\text{[OH}",r"^{-}",r"\text{] > [H}",r"^{+}",r"\text{]}")
		#WeakAcid_StrongBase_End.scale(.5)
		#WeakAcid_StrongBase_End.shift(DOWN)
		Acid_Equation = VGroup(
			TexMobject(r"\text{C}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}^{-}"),
			TextMobject("+"),
			TexMobject(r"\text{H}",r"_{2}",r"\text{O}"),
			TexMobject(r"\rightleftharpoons"),
			TexMobject(r"\text{HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}"),
			TextMobject("+"),
			TexMobject(r"\text{OH}",r"^{-}")
			)

		Acid_Equation.scale(.5)
		Acid_Equation[0].move_to(LEFT*4+UP*.5)
		Acid_Equation[1].move_to(LEFT*3+UP*.5)
		Acid_Equation[2].move_to(LEFT*2+UP*.5)
		Acid_Equation[3].move_to(UP*.5)
		Acid_Equation[4].move_to(RIGHT*2+UP*.5)
		Acid_Equation[5].move_to(RIGHT*3+UP*.5)
		Acid_Equation[6].move_to(RIGHT*4+UP*.5)


		I = TextMobject("I",color = RED)
		C = TextMobject("C",color = YELLOW)
		E = TextMobject("E",color = PURPLE)

		I.scale(.5)
		C.scale(.5)
		E.scale(.5)

		I.shift(LEFT*5.5)
		C.next_to(I,DOWN)
		E.next_to(C,DOWN)

		ICEBOX = VGroup(
			VGroup(
				TexMobject(r"0.050"),
				TexMobject(r"\text{[H}",r"_{2}",r"\text{O]}"),
				TexMobject(r"0"),
				TexMobject(r"\approx0"),
			),
			VGroup(
				TextMobject("-x"),
				TextMobject("-x"),
				TextMobject("+x"),
				TextMobject("+x")
			),
			VGroup(
				TexMobject(r"\text{0.050 - x}"),
				TexMobject(r"\text{[H}",r"_{2}",r"\text{O] - x}"),
				TextMobject("x"),
				TextMobject("x")
				)
		)
		ICEBOX.scale(.5)

		ICEBOX[0][0].shift(LEFT*4)
		ICEBOX[0][1].shift(LEFT*2)
		ICEBOX[0][2].shift(RIGHT*2)
		ICEBOX[0][3].shift(RIGHT*4)
		EndApprox = TexMobject(r"\approx0.050")
		EndApprox.scale(.5)

		for x in range(1,3):
			for z in range(4):
				ICEBOX[x][z].next_to(ICEBOX[x-1][z],DOWN)
		KBase = TexMobject(r"\text{K}",r"_{b}",r"\text{ =}",r"\text{ 5.6*10}",r"^{-10}",r"\text{ =}",r" \frac{[HC_{2}H_{3}O_{2}]\cdot [OH^{-}]}{[C_{2}H_{3}O_{2}^{-}]}")
		KBase.scale(.5)
		KBase.shift(UP*2)
		EndApprox.move_to(ICEBOX[2][0])
		Fraction_Filled = TexMobject(r"\text{ 5.6*10}",r"^{-10}",r"\text{ =}",r"\frac{x^{2}}{0.050}")
		Fraction_Filled.scale(.5)
		pOH = VGroup(
			TexMobject(r"5.3 * 10^{-6} = x  = \text{[OH}",r"^{-}",r"\text{]}"),
			TexMobject(r"-\log(5.3 * 10^{-6}) = ",r"\text{pOH}"),
			TexMobject(r"\text{5.28 = pOH}"),
			TexMobject(r"\text{14 - pOH = pH}"),
			TexMobject(r"\text{8.72 = pH}"),
			TexMobject(r"\text{pH}",r">",r"\text{ 7}")
			)
		pOH.scale(.5)
		pOH[0].shift(UP*2)
		for x in range(5):
			pOH[x+1].next_to(pOH[x],DOWN)

		self.add(Socratic10)
		self.play(Write(Socratic10))
		self.wait(2)
		self.play(FadeOut(Socratic10))
		self.wait(1)
		self.play(Write(WeakAcid_StrongBase))
		self.wait(1)
		self.play(Write(WeakAcid_StrongBase_Conc))
		self.wait(2)
		self.play(Transform(WeakAcid_StrongBase[8],Single_Arrow))
		self.wait(7)
		self.play(FadeOut(WeakAcid_StrongBase[0:9]))
		self.play(ApplyMethod(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)].move_to,ORIGIN))
		self.wait(7)
		self.play(ApplyMethod(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)].move_to,WeakAcid_StrongBase_Rev[0:9]))
		WeakAcid_StrongBase_Rev_Final = VGroup(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)],WeakAcid_StrongBase_Rev[9:len(WeakAcid_StrongBase_Rev)])
		self.wait(2)
		self.play(Write(WeakAcid_StrongBase_Rev[9:len(WeakAcid_StrongBase_Rev)]))
		self.wait(2)
		self.play(FadeOut(WeakAcid_StrongBase_Conc),ApplyMethod(WeakAcid_StrongBase_Rev_Final.shift,UP))
		self.play(Write(I),Write(C),Write(E),ApplyMethod(WeakAcid_StrongBase[9:15].move_to,Acid_Equation[0]),ApplyMethod(WeakAcid_StrongBase[15].move_to,Acid_Equation[1]),ApplyMethod(WeakAcid_StrongBase[16:len(WeakAcid_StrongBase)].move_to,Acid_Equation[2]),ApplyMethod(WeakAcid_StrongBase_Rev[9].move_to,Acid_Equation[3]),ApplyMethod(WeakAcid_StrongBase_Rev[10:16].move_to,Acid_Equation[4]),ApplyMethod(WeakAcid_StrongBase_Rev[16].move_to,Acid_Equation[5]),ApplyMethod(WeakAcid_StrongBase_Rev[17:len(WeakAcid_StrongBase_Rev)].move_to,Acid_Equation[6]))
		self.wait(2)
		self.play(Write(ICEBOX[0][0]))
		self.wait(2)
		self.play(Write(ICEBOX[0][1]))
		self.wait(11)
		self.play(Write(ICEBOX[0][2]))
		self.wait(1)
		self.play(Write(ICEBOX[0][3]))
		self.wait(7)
		self.play(Write(ICEBOX[1][0]),Write(ICEBOX[1][1]))
		self.wait(1)
		self.play(Write(ICEBOX[1][2]),Write(ICEBOX[1][3]))
		self.wait(2)
		for x in range(2,3):
			for z in range(len(ICEBOX[x])):
				self.play(Write(ICEBOX[x][z]))
				self.wait(1)
		self.play(Write(KBase[0:5]))
		self.wait(5)
		self.play(Transform(ICEBOX[2][0],EndApprox))
		self.wait(2)
		self.play(Write(KBase[5:7]))
		self.wait(2)
		self.play(FadeOut(KBase[0:3]))
		self.wait(2)
		self.play(ApplyMethod(KBase[3:7].move_to,ORIGIN+UP*2))
		Fraction_Filled.move_to(KBase[3:7])
		self.wait(2)
		self.play(Transform(KBase[6],Fraction_Filled[3]))
		self.play(ApplyMethod(KBase[6].shift,LEFT*.3),ApplyMethod(KBase[3:6].shift,RIGHT*.3))
		self.wait(2)
		self.play(FadeOut(KBase[3:7]))
		self.wait()
		self.play(Write(pOH[0]))
		self.wait()
		self.play(FadeOut(ICEBOX),FadeOut(I),FadeOut(C),FadeOut(E),FadeOut(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)]),FadeOut(WeakAcid_StrongBase_Rev[9:len(WeakAcid_StrongBase_Rev)]))
		self.wait(2)
		for x in range(5):
			self.play(TransformFromCopy(pOH[x],pOH[x+1]))
			self.wait(2)
		self.play(FadeOut(pOH))
		self.wait(2)
class pHL7(Scene):
	def construct(self):
		Socratic11 = VGroup(
			TextMobject("11. Why is the pH at the equivalence point between a"), 
			TextMobject("weak base and strong acid less than 7?")
			)
		Socratic11.scale(.5)
		Socratic11[1].next_to(Socratic11[0],DOWN)
		WeakBase_StrongAcid = TexMobject(r"\text{NH}",r"_{3}",r" +",r"\text{ H}",r"^{+}",r" \rightleftharpoons",r"\text{ NH}",r"_{4}^{+}")
		WeakBase_StrongAcid.scale(.5)
		Single_Arrow = TexMobject(r"\rightarrow")
		Single_Arrow.scale(.5)
		Single_Arrow.move_to(WeakBase_StrongAcid[5])
		WeakBase_StrongAcid_Fin = TexMobject(r"\text{ NH}",r"_{4}^{+}",r" \rightleftharpoons",r"\text{ NH}",r"_{3}",r" +",r"\text{ H}",r"^{+}")
		WeakBase_StrongAcid_Fin.scale(.5)

		self.add(Socratic11)
		self.play(Write(Socratic11))
		self.wait(2)
		self.play(FadeOut(Socratic11))
		self.wait(2)
		self.play(Write(WeakBase_StrongAcid))
		self.wait(9)
		self.play(Transform(WeakBase_StrongAcid[5],Single_Arrow))
		self.wait(9)
		self.play(FadeOut(WeakBase_StrongAcid[0:6]))
		self.play(ApplyMethod(WeakBase_StrongAcid[6:8].move_to,ORIGIN))
		self.wait(2)
		self.play(ApplyMethod(WeakBase_StrongAcid[6:8].move_to,WeakBase_StrongAcid_Fin[0:2]))
		self.play(Write(WeakBase_StrongAcid_Fin[2:len(WeakBase_StrongAcid_Fin)]))
		self.wait(8)
		self.play(FadeOut(WeakBase_StrongAcid_Fin[2:len(WeakBase_StrongAcid_Fin)]),FadeOut(WeakBase_StrongAcid[6:8]))
		self.wait(2)
class ATSB(Scene):
	def construct(self):
		Socratic12 = VGroup(
			TextMobject("12. Assume an acid is titrated with a strong base:"), 
			TextMobject("is the equivalence point affected by acid strength?")
			)
		Socratic12.scale(.5)
		Socratic12[1].next_to(Socratic12[0],DOWN)
		Socratic12b = VGroup(
			TextMobject("12. Assume an acid is titrated with a strong base:"), 
			TextMobject("is pH affected by acid strength?")
			)
		Socratic12b.scale(.5)
		Socratic12b[1].next_to(Socratic12[0],DOWN)
		x_value = ValueTracker(1.00)
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		x_tex.scale(.5)
		oh_value = ValueTracker(1.00)
		oh_tex = DecimalNumber(oh_value.get_value()).add_updater(lambda v: v.set_value(oh_value.get_value()))
		oh_tex.scale(.5)


		WeakAcid_StrongBase = TexMobject(r"\text{HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}",r"\text{ + OH}",r"^{-}",r"\rightleftharpoons",r"\text{C}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}^{-}",r"\text{ +}",r"\text{ H}",r"_{2}",r"\text{O}")
		WeakAcid_StrongBase.scale(.5)
		WeakAcid_StrongBase.shift(UP*3+LEFT*3)
		StrongAcid_StrongBase = TexMobject(r"\text{HCl + OH}",r"^{-}",r"\rightleftharpoons",r"\text{ Cl}",r"^{-}",r"\text{ + H}",r"_{2}",r"\text{O}")
		StrongAcid_StrongBase.scale(.5)
		StrongAcid_StrongBase.shift(LEFT*3)
		Single_Arrow = TexMobject(r"\rightarrow")
		Single_Arrow.scale(.5)
		Single_Arrow.move_to(WeakAcid_StrongBase[8])
		Single_Arrow2 = TexMobject(r"\rightarrow")
		Single_Arrow2.scale(.5)
		Single_Arrow2.move_to(StrongAcid_StrongBase[2])
		molAceticAcid = TexMobject(r"\text{ mol HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}")
		molAceticAcid.scale(.5)
		x_tex.next_to(molAceticAcid,LEFT)
		AceticMol = VGroup(x_tex,molAceticAcid)
		AceticMol.move_to(UP*3+RIGHT*3)
		molHydroCl = TextMobject(r"\text{1.00 mol HCl}")
		molHydroCl.scale(.5)
		molHydroCl.shift(RIGHT*3)
		molOH = TexMobject(r"\text{ mol OH}",r"^{-}")
		molOH.scale(.5)
		oh_tex.next_to(molOH,LEFT)
		OHmol = VGroup(oh_tex,molOH)
		OHmol.next_to(AceticMol,DOWN)
		molOH2 = TexMobject(r"\text{1.00 mol OH}",r"^{-}")
		molOH2.scale(.5)
		molOH2.next_to(molHydroCl,DOWN)
		WeakAcid_StrongBase_Rev = TexMobject(r"\text{C}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}^{-}",r"\text{ + H}",r"_{2}",r"\text{O}",r"\rightleftharpoons",r"\text{HC}",r"_{2}",r"\text{H}",r"_{3}",r"\text{O}",r"_{2}",r"\text{ +}",r"\text{ OH}",r"^{-}")
		WeakAcid_StrongBase_Rev.scale(.5)
		StrongAcid_StrongBase_Rev = TexMobject(r"\text{Cl}",r"^{-}",r"\text{ + H}",r"_{2}",r"\text{O}",r" \rightleftharpoons",r"\text{ HCl + OH}",r"^{-}")
		StrongAcid_StrongBase_Rev.scale(.5)
		pHWeak = TexMobject(r"\text{pH}",r">",r"7.00")
		pHWeak.scale(.5)
		pHStrong = TexMobject(r"\text{pH}",r"\approx",r"7.00")
		pHStrong.scale(.5)



		self.add(Socratic12)
		self.play(Write(Socratic12))
		self.wait(2)
		self.play(FadeOut(Socratic12))
		self.wait(3)
		self.play(Write(StrongAcid_StrongBase),Write(WeakAcid_StrongBase))
		self.wait(9)
		self.play(Transform(WeakAcid_StrongBase[8],Single_Arrow),Transform(StrongAcid_StrongBase[2],Single_Arrow2))
		self.wait(2)
		self.play(Write(AceticMol),Write(molHydroCl))
		self.wait(2)
		self.play(Write(OHmol),Write(molOH2))
		self.wait(2)
		self.play(
		    x_value.set_value,10.00,
		    oh_value.set_value,10.00,
		    rate_func=linear,
		    run_time=5
		    )
		self.wait(2)
		StrongAcid_StrongBase.save_state()
		WeakAcid_StrongBase.save_state()
		self.play(FadeOut(AceticMol),FadeOut(molHydroCl),FadeOut(OHmol),FadeOut(molOH2),FadeOut(StrongAcid_StrongBase),FadeOut(WeakAcid_StrongBase))
		self.wait(2)
		self.add(Socratic12b)
		self.play(Write(Socratic12b))
		self.wait(2)
		self.play(FadeOut(Socratic12b))
		self.wait(2)
		self.play(FadeIn(StrongAcid_StrongBase),FadeIn(WeakAcid_StrongBase))
		self.wait(2)
		self.play(FadeOut(WeakAcid_StrongBase[0:9]),FadeOut(StrongAcid_StrongBase[0:3]))
		self.play(ApplyMethod(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)].move_to,UP*3+LEFT*3),ApplyMethod(StrongAcid_StrongBase[3:len(StrongAcid_StrongBase)].move_to,LEFT*3))
		self.wait(13)
		StrongAcid_StrongBase_Rev.next_to(StrongAcid_StrongBase[3:len(StrongAcid_StrongBase)],DOWN)
		WeakAcid_StrongBase_Rev.next_to(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)],DOWN)
		pHWeak.next_to(WeakAcid_StrongBase_Rev,DOWN)
		pHStrong.next_to(StrongAcid_StrongBase_Rev,DOWN)
		self.play(Write(WeakAcid_StrongBase_Rev))
		self.wait(2)
		self.play(Write(pHWeak))
		self.wait(4.5)
		self.play(Write(StrongAcid_StrongBase_Rev))
		self.wait(2)
		self.play(Write(pHStrong))
		self.wait(4)
		self.play(FadeOut(pHWeak),FadeOut(pHStrong),FadeOut(StrongAcid_StrongBase_Rev),FadeOut(WeakAcid_StrongBase_Rev),FadeOut(StrongAcid_StrongBase[3:len(StrongAcid_StrongBase)]),FadeOut(WeakAcid_StrongBase[9:len(WeakAcid_StrongBase)]))
		self.wait(2)
class Socratic13(Scene):
	def construct(self):
		Socratic13 = TextMobject("13. What is an acid-base indicator?")
		Socratic13.scale(.5)
		self.add(Socratic13)
		self.play(Write(Socratic13))
		self.wait(2)
		self.play(FadeOut(Socratic13))
		self.wait(10)
class Socratic14(Scene):
	def construct(self):
		Socratic14 = TextMobject("14. What should be considered when choosing an indicator for a titration?")
		Socratic14.scale(.5)
		self.add(Socratic14)
		self.play(Write(Socratic14))
		self.wait(2)
		self.play(FadeOut(Socratic14))
		self.wait(2)

class Socratic14Graph(GraphScene):
	CONFIG = {
	    "y_max" : 13,
	    "y_min" : 0,
	    "x_max" : 200,
	    "x_min" : 0,
	    "y_tick_frequency" : 1,
	    "x_tick_frequency" : 25,
	    "axes_color" : WHITE,
	    "x_axis_label" : "Vol NaOH Added (mL)",
	    "y_axis_label" : "pH",
	}
	def construct(self):
	    self.setup_axes()
	    graph = self.get_graph(lambda x : ((-12/(1+1.5**(x-100)))+13), color = GREEN,)
	    Equivalence = Dot(self.coords_to_point(100,7),color=BLUE)
	    h_dashed = DashedLine(self.coords_to_point(0,7),self.coords_to_point(100,7),color = BLUE)
	    h_dashed2 = DashedLine(self.coords_to_point(0,8),self.coords_to_point(200,8),color = WHITE)
	    h_dashed3 = DashedLine(self.coords_to_point(0,10),self.coords_to_point(200,10),color = RED)
	    h_dashed4 = DashedLine(self.coords_to_point(0,3),self.coords_to_point(200,3),color = YELLOW_E)
	    h_dashed5 = DashedLine(self.coords_to_point(0,4.5),self.coords_to_point(200,4.5),color = BLUE_B)
	    h_dashed6 = DashedLine(self.coords_to_point(0,6),self.coords_to_point(200,6),color = YELLOW_E)
	    h_dashed7 = DashedLine(self.coords_to_point(0,8),self.coords_to_point(200,8),color = BLUE_B)
	    Pheno = Polygon(self.coords_to_point(0,8),self.coords_to_point(0,10),self.coords_to_point(200,10),self.coords_to_point(200,8),stroke_width=0,fill_opacity=.2,color=RED)
	    BPB = Polygon(self.coords_to_point(0,3),self.coords_to_point(0,4.5),self.coords_to_point(200,4.5),self.coords_to_point(200,3),stroke_width=0,fill_opacity=.2,color=BLUE_B)
	    BMB = Polygon(self.coords_to_point(0,6),self.coords_to_point(0,8),self.coords_to_point(200,8),self.coords_to_point(200,6),stroke_width=0,fill_opacity=.2,color=BLUE_B)
	    self.play(
	        ShowCreation(graph),
	        run_time = 2
	    )
	    self.wait()
	    self.play(ShowCreation(h_dashed))
	    self.play(ShowCreation(Equivalence))
	    self.play(Uncreate(h_dashed))
	    self.wait()
	    self.play(ShowCreation(h_dashed2),ShowCreation(h_dashed3))
	    self.play(FadeIn(Pheno))
	    self.wait(2)
	    self.play(FadeOut(h_dashed2),FadeOut(h_dashed3),FadeOut(Pheno))
	    self.wait()
	    self.play(ShowCreation(h_dashed4),ShowCreation(h_dashed5))
	    self.play(FadeIn(BPB))
	    self.wait()
	    self.play(FadeOut(h_dashed4),FadeOut(h_dashed5),FadeOut(BPB))
	    self.wait()
	    self.play(ShowCreation(h_dashed6),ShowCreation(h_dashed7))
	    self.play(FadeIn(BMB))
	    self.play(Indicate(Equivalence))
	    self.wait()
	    self.play(FadeOut(h_dashed6),FadeOut(h_dashed7),FadeOut(BMB))
	    self.wait()
	    self.play(FadeOut(Equivalence),FadeOut(graph),FadeOut(self.y_axis),FadeOut(self.x_axis))
	    self.wait(2)


	def setup_axes(self):
	    GraphScene.setup_axes(self)
	    # Custom parametters
	    self.x_axis.add_numbers(*range(0,225,25))
	    # Y parametters
	    self.y_axis.label_direction = LEFT
	    self.y_axis.add_numbers(*[0,7,13])
	    self.play(Write(self.x_axis),Write(self.y_axis))