import bpy

num = len(bpy.data.materials)

print(f'There are {num} materials')

for i, m in enumerate(bpy.data.materials):
    print(f'{i} Material: {m.name} ')


objects = [o for o in bpy.data.objects if o.type == 'MESH']

for o in objects:
    print(f'{o.name} Material')
    for m in o.material_slots:
        print(f'{m.name}')
