from random import randint

class clouds:
    def __init__(self,pic):
        self.cloudpic = pic
        self.cloudlist = []
        self.cloudlist.append(_cloud(self.cloudpic,0,100,1,1))

    def create(self,x,size,speed):
        if not self.cloudlist:
            self.cloudlist.append(_cloud(self.cloudpic,0,x,size,speed))
        else:
            self.cloudlist.append(_cloud(self.cloudpic,self.cloudlist[-1].num+1,x,size,speed))

    def destroy(self):
        for i,j in enumerate(self.cloudlist):
            if j.y >= 1000:
                del self.cloudlist[i]

    def act(self):
        for i in self.cloudlist:
            i.act()

    def draw(self,screen):
        chance = randint(0,200)
        if chance  == 25:
            location = randint(-100,800)
            layer = randint(0,2)
            if(layer == 0):
                speed = 1
                size = .5
            else:
                speed = 2
                size = 1
            self.create(location,size,speed)
        self.destroy()
        for i in self.cloudlist:
            i.draw(screen)


class _cloud:
    def __init__(self,pic,num,x,size,speed):
        self.num = num
        self.x = x
        self.y = -200
        self.size = size  ## size mod for cloud
        self.speed = speed
        self.cloudpic = pic
        self.viewBox = self.cloudpic.get_rect()
        self.viewBox.move_ip(self.x,self.y)

    def act(self):
        self.y+=self.speed
        self.viewBox = self.viewBox.move(0,self.speed)

    def draw(self,screen):
        screen.blit(self.cloudpic,(self.viewBox))
