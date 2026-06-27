from direct.actor.Actor import Actor


class Phoenix:
    def __init__(self, render):
        # Load the animated model
        self.actor = Actor("assets/phoenix.glb")

        # Attach it to the scene
        self.actor.reparentTo(render)

        # Position
        self.actor.setPos(0, 10, 0)

        # Scale
        self.actor.setScale(0.5)

    def play(self):
        # We'll discover the animation names shortly.
        # For now this won't crash if none exist.
        try:
            self.actor.loop("Take 001")
        except Exception:
            print("Animation not found.")