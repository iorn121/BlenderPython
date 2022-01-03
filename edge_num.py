import bpy
import bmesh


objects = [o for o in bpy.data.objects if o.type =="MESH"]

for i,obj in enumerate(objects):
    bpy.context.view_layer.objects.active=obj
    bpy.ops.object.mode_set(mode="EDIT")

    me=obj.data
    bm=bmesh.from_edit_mesh(me)
    print(f'Mesh {i}: {obj.name} have {len(bm.edges)}')
