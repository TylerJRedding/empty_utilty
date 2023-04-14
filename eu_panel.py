import bpy

class EU_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_empty_utility"
    bl_label = "Empty Utility"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Empty Utility"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.operator("object.create_empties", text="Create Empty(s)")

        col = row.column()
        col.operator("object.move_empty", text="Move Empty(s)")