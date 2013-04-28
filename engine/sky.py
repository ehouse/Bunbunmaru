class clouds:
    def __init__(self,pic):
        self.cloudpic = pic
        self.cloudlist = []

    def create(self,x,y):
        if not self.cloudlist:
            self.cloudlist.append(_cloud(0,x,y))
        else:
            self.cloudlist.append(_cloud(self.cloudlist[-1],x,y))


class _cloud:
    def __init__(self,num,x,y):
        self.num = num
        self.x = x
        self.y = y
