from random import randint

class clouds:
    def __init__(self,pic,viewbox):
        self.cloudpic = pic
        self.cloudbox = viewbox
        self.cloudlist = []
        self.cloudlist.append(_cloud(self.cloudpic,self.cloudbox,0,100,1,1))

    def create(self,x,size,speed):
        if not self.cloudlist:
            self.cloudlist.append(_cloud(self.cloudpic,self.cloudbox,0,x,size,speed))
        else:
            self.cloudlist.append(_cloud(self.cloudpic,self.cloudbox,self.cloudlist[-1].num+1,x,size,speed))

    def destroy(self):
        for i,j in enumerate(self.cloudlist):
            if j.y >= 1000:
                print ('Delete Cloud: %d' % j.num)
                del self.cloudlist[i]

    def act(self):
        for i in self.cloudlist:
            i.act()

    def draw(self,screen):
        chance = randint(0,200)
        if chance  == 25:
            location = randint(0,800)
            print('New Cloud: %d' % location)
            self.create(location,100,1)
        self.destroy()
        for i in self.cloudlist:
            i.draw(screen)


class _cloud:
    def __init__(self,pic,viewBox,num,x,size,speed):
        self.num = num
        self.x = x
        self.y = -20
        self.size = size  ## size mod for cloud
        self.speed = speed
        self.cloudpic = pic
        self.viewBox = viewBox
        self.viewBox.move_ip(self.x,self.y)

    def act(self):
        self.y+=self.speed
        self.viewBox = self.viewBox.move(0,self.speed)

    def draw(self,screen):
        screen.blit(self.cloudpic,(self.viewBox))
