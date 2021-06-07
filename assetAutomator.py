# assetAutomator
# generate renderballs, apply appended materials, and mark as assets.

import bpy

C = bpy.context
renderball = bpy.data.objects["Renderball"]
base = bpy.data.objects["Base"]
ballX = renderball.location[0] + 2 #moved "offscreen", so it doesn't get in the way of renders
ballY = renderball.location[1]
ballZ = renderball.location[2]
baseX = base.location[0] + 2 #moved "offscreen", so it doesn't get in the way of renders
baseY = base.location[1]
baseZ = base.location[2]
rows = 0
maxCols = 17

match_str = "-AssetAutomator"
materials = []
mats = bpy.data.materials

for x in range (0, len(mats)):
    if match_str not in mats[x].name:
        materials.append(mats[x])

while (rows < len(materials) / maxCols):
    cols = 0
    while (cols < maxCols):
        new_renderball = renderball.copy()
        new_base = base.copy()
        new_renderball.data = renderball.data.copy()
        new_base.data = base.data.copy()
        new_renderball.location = (ballX + (cols * 2), ((ballY + -abs(rows * 3))), ballZ)
        new_base.location = (baseX + (cols * 2), ((baseY + -abs(rows * 3))), baseZ)
        appliedMaterial = materials[(rows * maxCols) + cols]
        new_renderball.name = appliedMaterial.name
        new_renderball.data.materials[0] = appliedMaterial
        # bpy.ops.outliner.id_operation(appliedMaterial, 'MARK_ASSET')
        new_renderball.animation_data_clear()
        new_base.animation_data_clear()
        C.collection.objects.link(new_renderball)
        C.collection.objects.link(new_base)
        cols += 1
    rows += 1