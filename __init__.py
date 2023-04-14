bl_info = {
    "name": "empty_utility",
    "author": "Toast",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Empty Utility",
    "description": "Generate and manipulate empties with mesh verts",
    "category": "Object",
}

import bpy

from .eu_operator import CreateEmpties
from .eu_operator import MoveEmpty
from .eu_panel import EU_Panel

classes = (
    CreateEmpties,
    MoveEmpty,
    EU_Panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
