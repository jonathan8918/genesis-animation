#!/usr/bin/env python3
"""Ponto de entrada do pipeline Genesis Animation.
Uso:
  python scripts/main.py --help
  python scripts/main.py --render
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets"


def render_with_blender(blend_path: Path):
    """Tenta chamar o Blender em modo headless para renderizar um arquivo .blend."""
    blender_cmd = ["blender", "-b", str(blend_path), "-P", str(ROOT / "scripts" / "blender_render.py")]
    try:
        subprocess.check_call(blender_cmd)
    except FileNotFoundError:
        print("Blender não encontrado no PATH. Instale o Blender ou use o script dentro do Blender.")
    except subprocess.CalledProcessError as e:
        print("Blender retornou um erro:", e)


def render_placeholder():
    print("Executando etapa de render (placeholder)")
    example_blend = ASSETS_DIR / "scene.blend"
    if example_blend.exists():
        print(f"Arquivo .blend detectado: {example_blend}. Tentando render via Blender...")
        render_with_blender(example_blend)
    else:
        print("Nenhum scene.blend em assets/ — apenas exibindo mensagem de placeholder.")


def main():
    p = argparse.ArgumentParser(description="Genesis Animation pipeline")
    p.add_argument("--render", action="store_true", help="Executar etapa de render")
    args = p.parse_args()
    if args.render:
        render_placeholder()
    else:
        print("Uso: --render para executar a etapa de render. --help para ver opções.")


if __name__ == "__main__":
    main()
