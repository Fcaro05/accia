import bpy
import math
import os

# Pulisci la scena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Crea il corpo della borraccia
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=4)
bottle = bpy.context.active_object
bottle.name = 'Bottle_Body'

# Aggiungi il collo della borraccia
bpy.ops.mesh.primitive_cylinder_add(radius=0.4, depth=0.8)
neck = bpy.context.active_object
neck.location = (0, 0, 2.2)
neck.name = 'Bottle_Neck'

# Aggiungi il tappo
bpy.ops.mesh.primitive_cylinder_add(radius=0.45, depth=0.4)
cap = bpy.context.active_object
cap.location = (0, 0, 2.8)
cap.name = 'Bottle_Cap'

# Unisci gli oggetti
bpy.ops.object.select_all(action='DESELECT')
cap.select_set(True)
neck.select_set(True)
bottle.select_set(True)
bpy.context.view_layer.objects.active = bottle
bpy.ops.object.join()

# Aggiungi smooth shading
bpy.ops.object.shade_smooth()

# Aggiungi un materiale base
material = bpy.data.materials.new(name="Bottle_Material")
material.use_nodes = True
material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.169, 0.298, 0.494, 1)  # Blu primario
bottle.data.materials.append(material)

# Esporta in GLB
bpy.ops.export_scene.gltf(
    filepath=os.path.join(os.path.dirname(bpy.data.filepath), "models", "bottle.glb"),
    export_format='GLB',
    use_selection=True
)

# Esporta in USDZ per iOS/macOS
bpy.ops.wm.usd_export(
    filepath=os.path.join(os.path.dirname(bpy.data.filepath), "models", "bottle.usdz"),
    selection_only=True,
    visible_only=True
) 