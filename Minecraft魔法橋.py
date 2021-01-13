from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mcid = mc.getPlayerEntityId ('QQhelpme')

AIR = mc.getBlock(0,255,0)

blockID = 166
while True:
    x,y,z = mc.entity.getTilePos(mcid)
    ba = mc.getBlock(x,y-1,z)
    if ba == AIR:
        mc.setBlock(x,y-1,z,blockID)