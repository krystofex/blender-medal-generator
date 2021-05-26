
medalHeight = 0.1
medalRadius = 1
yourText = "congratulations"

bpy.ops.mesh.primitive_cylinder_add(
    vertices=256, radius=medalRadius, depth=medalHeight, enter_editmode=False, align='WORLD', location=(0, 0, 0))

bpy.ops.curve.primitive_bezier_circle_add(
    radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))

bpy.ops.object.text_add()
ob = bpy.context.object
ob.data.body = yourText
textSize = medalRadius * 2 - 0.1
bpy.context.object.dimensions[0] = textSize
bpy.context.object.dimensions[1] = bpy.context.object.scale[0]
bpy.context.object.dimensions[2] = bpy.context.object.scale[0]

bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
bpy.context.object.location[0] = 0
bpy.context.object.location[2] = medalHeight/2
