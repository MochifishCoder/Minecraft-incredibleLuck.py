from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y + 100
z = pos.z
mc.player.setTilePos(x, y, z)
pos2 = mc.player.getTilePos()
x = pos2.x
y = pos2.y - 100
z = pos2.z
blockType = 165
mc.setBlock(x, y, z, blockType)
