from direct.actor.Actor import Actor

class Phoenix:
    def __init__(self, render):
        self.actor = Actor("../assets/phoenix.glb")

        print(self.actor)

        self.actor.reparentTo(render)

        self.actor.setScale(25)
        self.actor.setPos(0, 50, 0)

    def play(self):
        # We'll discover the animation names shortly.
        # For now this won't crash if none exist.
        try:
            self.actor.loop("Take 001")
        except Exception:
            print("Animation not found.")