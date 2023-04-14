import bpy
import mathutils

class CreateEmpties(bpy.types.Operator):
    bl_idname = "object.create_empties"
    bl_label = "Create Empties"
    bl_description = "Create an empty per vertex of selected objects."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_List = context.selected_objects
        for obj in selected_List:
            if obj.type == 'MESH':
                mesh = obj.data
                for vert in mesh.vertices:
                    matrix_world = obj.matrix_world
                    vert_world_pos = matrix_world @ vert.co
                    bpy.ops.object.empty_add(location=vert_world_pos)
        return {'FINISHED'}

class MoveEmpty(bpy.types.Operator):
    bl_idname = "object.move_empty"
    bl_label = "Move Empty(s)"
    bl_description = "Move all selected empties to nearest vertex of selected mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the selected meshes and empties
        selected_meshes = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        selected_empties = [obj for obj in bpy.context.selected_objects if obj.type == 'EMPTY']

        for mesh in selected_meshes:
            mesh_vertices = mesh.data.vertices
            for vertex in mesh_vertices:
                if len(selected_empties) <= 0:
                    self.report({'WARNING'}, "Too few empties in selection for vertex count.")
                    return {'CANCELLED'} 
                
                empty = selected_empties.pop(0)
                location = mesh.matrix_world @ vertex.co
                empty.location = location
                
        return {'FINISHED'}