
from direct.showbase.ShowBase import ShowBase


class PhoenixPet(ShowBase):
    def __init__(self):
        super().__init__()

        # Disable the default mouse camera
        self.disableMouse()

        # Load the model
        self.pet = self.loader.loadModel("../assets/phoenix.glb")
        self.pet.reparentTo(self.render)
        self.pet.setScale(0.5)
        self.pet.setPos(0, 10, 0)

        # Play the first animation if it exists
        try:
            self.pet.loop("Take 001")
        except Exception:
            print("No animation named 'Take 001' found.")

        # Camera
        self.camera.setPos(0, -20, 5)
        self.camera.lookAt(self.pet)


app = PhoenixPet()
app.run()