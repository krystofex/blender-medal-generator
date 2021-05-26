medalHeight = 0.1
medalRadius = 1
textExtrude = 0.05
yourText = "congratulations"
level = 1

# generate cylinder
bpy.ops.mesh.primitive_cylinder_add(
    vertices=256, radius=medalRadius, depth=medalHeight, enter_editmode=False, align='WORLD', location=(0, 0, 0))
activeObject = bpy.context.active_object
material = bpy.data.materials.new(name="MedalMaterial")
activeObject.data.materials.append(material)
bpy.context.object.active_material.use_nodes = True
# medal color
if (level == 0):
    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (
        0.8, 0.524811, 0.0285806, 1)

if (level == 1):
    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (
        0.8, 0.636062, 0.730513, 1)
else:
    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (
        0.8, 0.15289, 0.00437057, 1)

material.node_tree.nodes["Principled BSDF"].inputs[4].default_value = 1
material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.145455


bpy.ops.curve.primitive_bezier_circle_add(
    radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))

# create congratulation text
bpy.ops.object.text_add()
text = bpy.context.object
text.data.body = yourText
textSize = medalRadius * 2 - 0.1
text.dimensions[0] = textSize
text.dimensions[1] = text.scale[0]
text.data.extrude = 0.05
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
text.location[0] = 0
text.location[2] = medalHeight/2
text.data.materials.append(material)
text.location[2] = medalHeight/2 + textExtrude
