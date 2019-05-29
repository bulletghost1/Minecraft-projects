#Base Project Format.
from mcpi import minecraft
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

#X=Foward and Backward, Y=up and down, Z=left and right

def init():
    mc = Minecraft.create("10.183.3.25", 4711)
    mc.postToChat("Front of Site B")
    x, y, z = mc.player.getPos()	
    return mc

def floor(mc,x,y,z):
	mc.setBlocks(x, y-1, z, x+13, y-1, z+13, 24)
	mc.setBlocks(x, y-1, z, x+13, y-1, z-13, 24)

def walls(mc,x,y,z):
	mc.setBlocks(x, y+0, z+13, x+13, y+0, z+13, 24)
	mc.setBlocks(x, y+0, z-13, x+13, y+0, z-13, 24)
	mc.setBlocks(x, y+1, z+13, x+13, y+1, z+13, 24)
	mc.setBlocks(x, y+1, z-13, x+13, y+1, z-13, 24)
	mc.setBlocks(x, y+2, z+13, x+13, y+1, z+13, 24)
	mc.setBlocks(x, y+2, z-13, x+13, y+1, z-13, 24)
	mc.setBlocks(x, y+3, z+13, x+13, y+1, z+13, 24)
	mc.setBlocks(x, y+3, z-13, x+13, y+1, z-13, 24)
	mc.setBlocks(x, y+4, z+13, x+13, y+1, z+13, 24)
	mc.setBlocks(x, y+4, z-13, x+13, y+1, z-13, 24)
	mc.setBlocks(x, y+5, z+13, x+13, y+1, z+13, 24)
	mc.setBlocks(x, y+5, z-13, x+13, y+1, z-13, 24)
	mc.setBlocks(x, y+6, z+13, x+13, y+1, z+13, 24)
	mc.setBlocks(x, y+6, z-13, x+13, y+1, z-13, 24)
	
def front(mc,x,y,z):
	mc.setBlocks(x, y+6, z+13, x, y+6, z-13, 24)
	mc.setBlocks(x, y+0, z+4, x, y+6, z+4, 24)
	mc.setBlocks(x, y+0, z+12, x, y+4, z+12, 24)
	mc.setBlocks(x, y+0, z+11, x, y+3, z+11, 24)
	mc.setBlocks(x, y+0, z-12, x, y+6, z-12, 24)
	mc.setBlocks(x, y+0, z-11, x, y+6, z-11, 24)
	mc.setBlocks(x, y+0, z-10, x, y+6, z-10, 24)
	mc.setBlocks(x, y+0, z-9, x, y+6, z-9, 24)
	mc.setBlocks(x, y+0, z-8, x, y+6, z-8, 24)
	mc.setBlocks(x, y+0, z-7, x, y+6, z-7, 24)
	mc.setBlocks(x, y+0, z-6, x, y+6, z-6, 24)
	mc.setBlocks(x, y+0, z-5, x, y+6, z-5, 24)
	mc.setBlocks(x, y+0, z-4, x, y+3, z-4, 5)
	mc.setBlocks(x, y+0, z-3, x, y+3, z-3, 5)
	mc.setBlocks(x, y+0, z-2, x, y+3, z-2, 5)
	mc.setBlocks(x+1, y+0, z-1, x+1, y+3, z-1, 5)
	mc.setBlocks(x, y+0, z+2, x, y+3, z+2, 5)
	mc.setBlocks(x, y+0, z+3, x, y+3, z+3, 5)
	mc.setBlocks(x, y+0, z+10, x, y+4, z+10, 24)
	mc.setBlocks(x, y+0, z+9, x, y+5, z+9, 24)
	mc.setBlocks(x, y+0, z+8, x, y+5, z+8, 24)
	mc.setBlocks(x, y+0, z+7, x, y+5, z+7, 24)
	mc.setBlocks(x, y+0, z+6, x, y+5, z+6, 24)
	mc.setBlocks(x, y+0, z+5, x, y+5, z+5, 24)
	mc.setBlocks(x, y+5, z+0, x, y+5, z+0, 24)
	mc.setBlocks(x, y+5, z+1, x, y+5, z+1, 24)
	mc.setBlocks(x, y+5, z+2, x, y+5, z+2, 24)
	mc.setBlocks(x, y+5, z+3, x, y+5, z+3, 24)
	mc.setBlocks(x, y+5, z-3, x, y+5, z-3, 24)
	mc.setBlocks(x, y+5, z-4, x, y+5, z-4, 24)
	mc.setBlocks(x, y+5, z-2, x, y+5, z-2, 24)
	mc.setBlocks(x, y+5, z-1, x, y+5, z-1, 24)
	mc.setBlocks(x, y+4, z-4, x, y+4, z-4, 24)
	mc.setBlocks(x, y+4, z-3, x, y+4, z-3, 24)
	mc.setBlocks(x, y+4, z-2, x, y+4, z-2, 24)
	mc.setBlocks(x, y+4, z-1, x, y+4, z-1, 24)
	mc.setBlocks(x, y+4, z+0, x, y+4, z+0, 24)
	mc.setBlocks(x, y+4, z+1, x, y+4, z+1, 24)
	mc.setBlocks(x, y+4, z+2, x, y+4, z+2, 24)
	mc.setBlocks(x, y+4, z+3, x, y+4, z+3, 24)
	
def site(mc,x,y,z):
	mc.setBlocks(x+1, y+3, z+12, x+1, y+3, z+12, 17)
	mc.setBlocks(x+1, y+2, z+12, x+1, y+2, z+12, 17)
	mc.setBlocks(x+1, y+1, z+12, x+1, y+1, z+12, 17)
	mc.setBlocks(x+1, y+0, z+12, x+1, y+0, z+12, 17)
	mc.setBlocks(x+1, y+3, z+11, x+1, y+3, z+11, 17)
	mc.setBlocks(x+1, y+2, z+11, x+1, y+2, z+11, 17)
	mc.setBlocks(x+1, y+1, z+11, x+1, y+1, z+11, 17)
	mc.setBlocks(x+1, y+0, z+11, x+1, y+0, z+11, 17)
	mc.setBlocks(x+2, y+3, z+12, x+2, y+3, z+12, 17)
	mc.setBlocks(x+2, y+2, z+12, x+2, y+2, z+12, 17)
	mc.setBlocks(x+2, y+1, z+12, x+2, y+1, z+12, 17)
	mc.setBlocks(x+2, y+0, z+12, x+2, y+0, z+12, 17)
	mc.setBlocks(x+3, y+3, z+12, x+3, y+3, z+12, 17)
	mc.setBlocks(x+3, y+2, z+12, x+3, y+2, z+12, 17)
	mc.setBlocks(x+3, y+1, z+12, x+3, y+1, z+12, 17)
	mc.setBlocks(x+3, y+0, z+12, x+3, y+0, z+12, 17)
	mc.setBlocks(x+2, y+3, z+11, x+2, y+3, z+12, 17)
	mc.setBlocks(x+2, y+2, z+11, x+2, y+2, z+12, 17)
	mc.setBlocks(x+2, y+1, z+11, x+2, y+1, z+12, 17)
	mc.setBlocks(x+2, y+0, z+11, x+2, y+0, z+12, 17)
	mc.setBlocks(x+3, y+3, z+11, x+3, y+3, z+11, 17)
	mc.setBlocks(x+3, y+2, z+11, x+3, y+2, z+11, 17)
	mc.setBlocks(x+3, y+1, z+11, x+3, y+1, z+11, 17)
	mc.setBlocks(x+3, y+0, z+11, x+3, y+0, z+11, 17)
	mc.setBlocks(x+1, y+2, z+10, x+1, y+2, z+10, 17)
	mc.setBlocks(x+1, y+1, z+10, x+1, y+1, z+10, 17)
	mc.setBlocks(x+1, y+0, z+10, x+1, y+0, z+10, 17)
	mc.setBlocks(x+2, y+1, z+10, x+2, y+1, z+10, 17)
	mc.setBlocks(x+2, y+0, z+10, x+2, y+0, z+10, 17)
	mc.setBlocks(x+3, y+0, z+10, x+3, y+0, z+10, 17)
	mc.setBlocks(x+1, y+0, z+4, x+1, y+0, z+4, 42)
	mc.setBlocks(x+1, y+0, z+5, x+1, y+0, z+5, 42)
	mc.setBlocks(x+1, y+0, z+6, x+1, y+0, z+6, 42)
	mc.setBlocks(x+1, y+0, z+7, x+1, y+0, z+7, 42)
	mc.setBlocks(x+1, y+1, z+4, x+1, y+1, z+4, 44)
	mc.setBlocks(x+1, y+1, z+5, x+1, y+1, z+5, 44)
	mc.setBlocks(x+1, y+1, z+6, x+1, y+1, z+6, 44)
	mc.setBlocks(x+1, y+1, z+7, x+1, y+1, z+7, 44)
	mc.setBlocks(x+6, y-1, z+10, x+6, y-1, z+10, 87)
	mc.setBlocks(x+7, y-1, z+10, x+7, y-1, z+10, 87)
	mc.setBlocks(x+8, y-1, z+10, x+8, y-1, z+10, 87)
	mc.setBlocks(x+7, y-1, z+11, x+7, y-1, z+11, 87)
	mc.setBlocks(x+7, y-1, z+9, x+7, y-1, z+9, 87)
	mc.setBlocks(x+7, y+0, z+10, x+7, y+0, z+10, 46)
	mc.setBlocks(x+10, y+0, z+8, x+10, y+0, z+8, 42)
	mc.setBlocks(x+11, y+0, z+8, x+11, y+0, z+8, 42)
	mc.setBlocks(x+10, y+1, z+8, x+10, y+1, z+8, 44)
	mc.setBlocks(x+11, y+1, z+8, x+11, y+1, z+8, 44)
	mc.setBlocks(x+4, y+0, z+7, x+4, y+0, z+7, 17)
	mc.setBlocks(x+4, y+0, z+6, x+4, y+0, z+6, 17)
	mc.setBlocks(x+5, y+0, z+6, x+5, y+0, z+6, 17)
	mc.setBlocks(x+5, y+0, z+7, x+5, y+0, z+7, 17)
	mc.setBlocks(x+4, y+1, z+7, x+4, y+1, z+7, 44)
	mc.setBlocks(x+4, y+1, z+6, x+4, y+1, z+6, 44)
	mc.setBlocks(x+5, y+1, z+6, x+5, y+1, z+6, 44)
	mc.setBlocks(x+5, y+1, z+7, x+5, y+1, z+7, 44)
	mc.setBlocks(x+7, y+0, z+4, x+7, y+1, z+4, 17)
	mc.setBlocks(x+8, y+0, z+3, x+8, y+2, z+3, 17)
	mc.setBlocks(x+7, y+0, z+3, x+7, y+2, z+3, 17)
	mc.setBlocks(x+8, y+0, z+4, x+8, y+2, z+4, 6)
	mc.setBlocks(x+4, y+0, z-12, x+8, y+0, z-12, 42)
	mc.setBlocks(x+4, y+0, z-11, x+8, y+0, z-11, 42)
	mc.setBlocks(x+5, y+1, z-12, x+7, y+1, z-12, 20)
	mc.setBlocks(x+5, y+1, z-11, x+7, y+1, z-11, 20)
	mc.setBlocks(x+11, y+0, z-12, x+11, y+1, z-12, 17)
	mc.setBlocks(x+12, y+0, z-12, x+13, y+2, z-12, 17)
	mc.setBlocks(x+11, y+0, z-11, x+11, y+2, z-11, 17)
	mc.setBlocks(x+12, y+0, z-11, x+13, y+2, z-11, 17)
	mc.setBlocks(x+10, y+0, z-12, x+10, y+0, z-12, 17)
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	print("position ",x,y,z)
	floor(mc, x,y,z)
	site(mc, x,y,z)
	walls(mc, x,y,z)
	front(mc, x,y,z)
	mc.player.setPos(x, y, z)


main()
# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
NETHERACK			 87
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
NETHER_BRICK		112
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
