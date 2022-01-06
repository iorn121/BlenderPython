import bpy

for i,m in enumerate(bpy.data.meshes):
    print(f'Mesh {i}: {m.name} have {len(m.polygons)}')
    for j,v in enumerate(m.vertices):
        print(f'Vertex {j} exists at ({v.co.x}, {v.co.y}, {v.co.z})')