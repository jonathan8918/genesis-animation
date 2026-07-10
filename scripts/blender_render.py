"""Script para rodar dentro do Blender (bpy).
Este script assume que será executado com:
  blender -b assets/scene.blend -P scripts/blender_render.py
Ele configura a saída para a pasta relative //renders/ e renderiza a animação completa.
"""
import bpy

# Defina saída relativa ao .blend
output_prefix = "//renders/frame_"
bpy.context.scene.render.filepath = output_prefix

# Formato de saída (PNG para frames, mais seguro para pós-produção)
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Opcional: substituir frame range aqui
# bpy.context.scene.frame_start = 1
# bpy.context.scene.frame_end = 120

# Garante que a pasta de saída exista (Blender interpreta // como relativa ao .blend)
# A função abaixo resolve o caminho real só quando executado dentro do Blender
try:
    import os
    blend_dir = os.path.dirname(bpy.data.filepath)
    if blend_dir:
        renders_dir = os.path.join(blend_dir, "renders")
        os.makedirs(renders_dir, exist_ok=True)
except Exception:
    # falha silenciosa - não é crítica
    pass

# Renderiza a animação inteira usando as configurações no .blend
bpy.ops.render.render(animation=True)
