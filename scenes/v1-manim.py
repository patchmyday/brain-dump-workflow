"""
Brain Dump Workflow — Manim CE v0.20.1 Animation Scenes
Neon tech style intro/explainer for the Brain Dump Workflow video.
"""

from manim import *
import numpy as np

# ── Palette ──────────────────────────────────────────────
BG      = "#0A0A0A"
CYAN    = "#00F5FF"
MAGENTA = "#FF00FF"
GREEN   = "#39FF14"
WHITE   = "#FFFFFF"
MONO    = "Monospace"

# ── Helpers ──────────────────────────────────────────────

def neon_rect(width=2.0, height=1.0, color=CYAN, corner_radius=0.15):
    """Rounded rectangle with neon glow look."""
    r = RoundedRectangle(
        corner_radius=corner_radius, width=width, height=height,
        stroke_color=color, stroke_width=3, fill_color=BG, fill_opacity=0.85,
    )
    return r


def neon_text(label, font_size=28, color=WHITE):
    return Text(label, font=MONO, font_size=font_size, color=color)


def brain_shape():
    """Stylised brain out of circles — simple iconic form."""
    left = Circle(radius=0.55, stroke_color=CYAN, stroke_width=3, fill_opacity=0).shift(LEFT * 0.3)
    right = Circle(radius=0.55, stroke_color=CYAN, stroke_width=3, fill_opacity=0).shift(RIGHT * 0.3)
    stem = Line(DOWN * 0.55, DOWN * 1.0, stroke_color=CYAN, stroke_width=3)
    # squiggle lines inside
    s1 = Line(LEFT * 0.25 + UP * 0.15, LEFT * 0.05 + DOWN * 0.2, stroke_color=MAGENTA, stroke_width=2)
    s2 = Line(RIGHT * 0.05 + UP * 0.2, RIGHT * 0.25 + DOWN * 0.15, stroke_color=MAGENTA, stroke_width=2)
    return VGroup(left, right, stem, s1, s2)


def doc_shape():
    """Simple document icon."""
    body = RoundedRectangle(
        corner_radius=0.08, width=1.0, height=1.4,
        stroke_color=GREEN, stroke_width=3, fill_color=BG, fill_opacity=0.8,
    )
    lines = VGroup(*[
        Line(LEFT * 0.3 + UP * (0.35 - i * 0.25),
             RIGHT * 0.3 + UP * (0.35 - i * 0.25),
             stroke_color=GREEN, stroke_width=2, stroke_opacity=0.7)
        for i in range(4)
    ])
    fold = Polygon(
        body.get_corner(UR),
        body.get_corner(UR) + DOWN * 0.3,
        body.get_corner(UR) + LEFT * 0.3,
        stroke_color=GREEN, stroke_width=2, fill_color=BG, fill_opacity=0.9,
    )
    return VGroup(body, lines, fold)


# ═════════════════════════════════════════════════════════
# Scene 1 — BrainDumpIntro
# ═════════════════════════════════════════════════════════

class BrainDumpIntro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Brain icon ──
        brain = brain_shape().scale(1.2).move_to(ORIGIN)

        # ── Title text ──
        title = Text(
            "Brain Dump Workflow", font=MONO, font_size=48,
            color=CYAN,
        ).next_to(brain, DOWN, buff=0.8)

        subtitle = Text(
            "capture every idea, automatically",
            font=MONO, font_size=22, color=WHITE,
        ).next_to(title, DOWN, buff=0.4).set_opacity(0.6)

        # ── Animate brain drawing ──
        self.play(Create(brain, run_time=2))
        self.wait()

        # ── Flash glow ──
        self.play(
            brain.animate.set_stroke(color=MAGENTA, width=5),
            rate_func=there_and_back,
            run_time=0.6,
        )
        self.wait()

        # ── Morph brain → document ──
        doc = doc_shape().scale(1.2).move_to(brain.get_center())
        self.play(ReplacementTransform(brain, doc, run_time=1.5))
        self.wait()

        # ── Title appears ──
        self.play(Write(title, run_time=1.2))
        self.wait()
        self.play(FadeIn(subtitle, shift=UP * 0.2))
        self.wait(1.5)

        # ── Fade out ──
        self.play(FadeOut(VGroup(doc, title, subtitle), run_time=0.8))
        self.wait()


# ═════════════════════════════════════════════════════════
# Scene 2 — WorkflowDiagram
# ═════════════════════════════════════════════════════════

class WorkflowDiagram(Scene):
    def construct(self):
        self.camera.background_color = BG

        header = Text(
            "The Pipeline", font=MONO, font_size=36, color=MAGENTA,
        ).to_edge(UP, buff=0.5)
        self.play(Write(header, run_time=0.8))
        self.wait()

        # ── Node definitions ──
        labels = ["Voice", "Dictate\nText", "Format\nDate", "Save to\niCloud", ".md\nFile"]
        icons  = ["🎤", "📝", "📅", "☁️", "📄"]
        colors = [CYAN, CYAN, MAGENTA, GREEN, GREEN]

        nodes = []
        node_groups = VGroup()

        # Build nodes horizontally
        for i, (lbl, ico, col) in enumerate(zip(labels, icons, colors)):
            box = neon_rect(width=2.0, height=1.3, color=col)
            icon_t = Text(ico, font_size=28).move_to(box.get_center() + UP * 0.2)
            label_t = Text(
                lbl, font=MONO, font_size=18, color=WHITE,
            ).move_to(box.get_center() + DOWN * 0.25)
            g = VGroup(box, icon_t, label_t)
            nodes.append(g)
            node_groups.add(g)

        node_groups.arrange(RIGHT, buff=0.6).move_to(ORIGIN + DOWN * 0.3)

        # Scale to fit if needed
        if node_groups.width > 13:
            node_groups.scale_to_fit_width(13)

        # ── Arrows ──
        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = Arrow(
                nodes[i].get_right(), nodes[i + 1].get_left(),
                buff=0.1, stroke_color=WHITE, stroke_width=2,
                max_tip_length_to_length_ratio=0.2,
            ).set_opacity(0.7)
            arrows.add(a)

        # ── Sequential reveal ──
        for i, node in enumerate(nodes):
            self.play(FadeIn(node, scale=0.7), run_time=0.6)
            self.wait(0.3)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.4)
                self.wait(0.2)

        # ── Pulse the whole pipeline ──
        pipeline = VGroup(node_groups, arrows)
        self.play(
            pipeline.animate.set_opacity(0.5),
            rate_func=there_and_back,
            run_time=0.8,
        )
        self.wait(1)

        # ── Fade out ──
        self.play(FadeOut(VGroup(header, pipeline), run_time=0.8))
        self.wait()


# ═════════════════════════════════════════════════════════
# Scene 3 — BeforeAfterScene
# ═════════════════════════════════════════════════════════

class BeforeAfterScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        divider = DashedLine(
            UP * 3.5, DOWN * 3.5,
            stroke_color=WHITE, stroke_width=1, stroke_opacity=0.15,
        )

        # ── Labels ──
        before_lbl = Text(
            "BEFORE", font=MONO, font_size=30, color=MAGENTA,
        ).move_to(LEFT * 3.5 + UP * 3).set_opacity(0.9)
        after_lbl = Text(
            "AFTER", font=MONO, font_size=30, color=GREEN,
        ).move_to(RIGHT * 3.5 + UP * 3).set_opacity(0.9)

        self.play(
            Create(divider),
            FadeIn(before_lbl, shift=DOWN * 0.2),
            FadeIn(after_lbl, shift=DOWN * 0.2),
            run_time=0.8,
        )
        self.wait()

        # ── LEFT: Chaotic thought bubbles ──
        np.random.seed(42)
        thoughts_text = [
            "todo...", "idea?!", "call X", "buy milk",
            "blog post", "meeting??", "password", "fix bug",
        ]
        bubbles = VGroup()
        for i, t in enumerate(thoughts_text):
            bubble = RoundedRectangle(
                corner_radius=0.15, width=1.6, height=0.55,
                stroke_color=MAGENTA, stroke_width=1.5,
                fill_color=BG, fill_opacity=0.7,
            )
            txt = Text(t, font=MONO, font_size=18, color=WHITE).move_to(bubble)
            g = VGroup(bubble, txt)
            angle = np.random.uniform(-0.4, 0.4)
            g.rotate(angle)
            x = np.random.uniform(-5.5, -1.5)
            y = np.random.uniform(-2.5, 2.0)
            g.move_to([x, y, 0])
            g.set_opacity(np.random.uniform(0.4, 1.0))
            bubbles.add(g)

        for b in bubbles:
            self.play(FadeIn(b, scale=0.5), run_time=0.15)
        self.wait(0.5)

        # ── RIGHT: Neat organised files ──
        files = VGroup()
        file_names = [
            "2025-04-13.md", "2025-04-12.md", "2025-04-11.md",
            "2025-04-10.md", "2025-04-09.md",
        ]
        for i, fn in enumerate(file_names):
            card = RoundedRectangle(
                corner_radius=0.1, width=3.0, height=0.55,
                stroke_color=GREEN, stroke_width=2,
                fill_color=BG, fill_opacity=0.85,
            )
            icon = Text("📄", font_size=20).move_to(card.get_left() + RIGHT * 0.35)
            name = Text(fn, font=MONO, font_size=20, color=WHITE).next_to(icon, RIGHT, buff=0.2)
            g = VGroup(card, icon, name)
            g.move_to(RIGHT * 3.5 + UP * (1.5 - i * 0.75))
            files.add(g)

        for f in files:
            self.play(FadeIn(f, shift=DOWN * 0.3), run_time=0.3)
            self.wait(0.1)

        self.wait(0.5)

        # ── Transform: chaos fades, order pulses ──
        self.play(
            bubbles.animate.set_opacity(0.08),
            files.animate.set_stroke(color=CYAN, width=3),
            run_time=1.2,
        )
        self.wait()

        # Check mark
        check = Text("✓", font_size=64, color=GREEN).move_to(RIGHT * 3.5 + DOWN * 2.5)
        self.play(FadeIn(check, scale=2), run_time=0.5)
        self.wait(1)

        # ── Fade out everything ──
        all_mobs = VGroup(divider, before_lbl, after_lbl, bubbles, files, check)
        self.play(FadeOut(all_mobs, run_time=0.8))
        self.wait()
