from direct.showbase.ShowBase import ShowBase

from app.pet import Phoenix


class PetRenderer(ShowBase):

    def __init__(self):
        super().__init__()

        self.disableMouse()

        self.camera.setPos(0, -120, 30)
        self.camera.lookAt(0, 50, 0)
        
        self.pet = Phoenix(self.render)
        #self.pet.play()