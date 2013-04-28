from random import randint

class clouds:
    def __init__(self,pic,viewbox):
        self.cloudpic = pic
        self.cloudbox = viewbox
        self.cloudlist = []
        self.cloudlist.append(_cloud(self.cloudpic,self.cloudbox,0,100,1,1))

    def create(self,x,size,speed):
        self.cloudlist.append(_cloud(self.cloudpic,self.cloudbox,self.cloudlist[-1],x,size,speed))

    def destroy(self,num):
        for i,j in enumerate(self.cloudlist):
            if j.num == num:
                del self.cloudlist[i]

    def act(self):
        chance = randint(0,50)
        if chance % 10 == 0:
            self.create(randint(0,800),1,1)
        for i in self.cloudlist:
            i.act()

    def draw(self,screen):
        for i in self.cloudlist:
            i.draw(screen)


class _cloud:
    def __init__(self,pic,viewBox,num,x,size,speed):
        self.num = num
        self.x = x
        self.size = size  ## size mod for cloud
        self.speed = speed
        self.cloudpic = pic
        self.viewBox = viewBox
        self.viewBox.move_ip(x,-20)

    def act(self):
        self.viewBox = self.viewBox.move(0,self.speed)

    def draw(self,screen):
        screen.blit(self.cloudpic,(self.viewBox))
