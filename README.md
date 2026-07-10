# genesis-animation
Animação Bíblica Cinematográfica - A Criação (Gênesis)

## Como executar (instruções rápidas)
Este repositório contém um esqueleto inicial para transformar o projeto em um projeto Python executável que pode servir como pipeline de automação/render.

Principais arquivos adicionados:
- scripts/main.py: ponto de entrada Python (CLI simples).
- scripts/blender_render.py: exemplo de script para rodar render em modo headless com Blender.
- requirements.txt: dependências opcionais.
- Makefile: comandos úteis (venv, instalar, rodar, render com Blender).
- assets/.gitkeep: placeholder para manter o diretório assets no repositório.

### Rodando localmente
1. Criar e ativar ambiente virtual:

```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

2. Instalar dependências (opcional):

```
pip install -r requirements.txt
```

3. Executar o pipeline Python:

```
python scripts/main.py --help
python scripts/main.py --render
```

4. Render com Blender (se houver assets/scene.blend):

```
blender -b assets/scene.blend -P scripts/blender_render.py
```

---

Se quiser, eu posso:
- adicionar mais etapas ao scripts/main.py (importar assets, converter, enviar para render);
- criar um arquivo pyproject.toml/entry-point para instalar um comando `genesis`;
- adicionar GitHub Actions para rodar builds/render em CI.
