from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcid = mc.getPlayerEntityId("QQhelpme")
x,y,z = mc.entity.getTilePos(mcid)

for Ya in range(1,21):
    block = []
    for Zc in range(-1,2):
        for Xb in range(-1,2):
            around = mc.getBlock(x+Xb,y-Ya,z+Zc)
            block.append(around)
        print(block)
        block = []
    print()
        
