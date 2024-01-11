class Arrow:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, 600)
    def move(self):
        self.pos = self.pos.move(0, -10)
        if self.pos.top > 0:
            self.pos.bottom = 400
			
			

		

		
