import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Medal generator"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Medal'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "sample text", icon='CUBE')
        
        row = layout.row()
        row.operator("mesh.primitive_cube_add")

def register():
    bpy.utils.register_class(TestPanel)
    
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    
    
if __name__ == "__main__":
    register()