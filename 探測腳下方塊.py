from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcid = mc.getPlayerEntityId("QQhelpme")
x,y,z = mc.entity.getTilePos(mcid)
blockaround = 0
blockRecord = []
counterBlockY = 0

while True :
    if counterBlockY >= 20:
        break
    blockaround = mc.getBlock(x-1,y-1,z)
    blockRecord.append(blockaround)
    blockaround = mc.getBlock(x,y-1,z)
    blockRecord.append(blockaround)
    blockaround = mc.getBlock(x+1,y-1,z)
    blockRecord.append(blockaround)
    x,y,z=x,y-1,z
    counterBlockY +=1
    print(blockRecord)
    blockRecord = []