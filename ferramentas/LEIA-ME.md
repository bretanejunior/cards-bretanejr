# Gerador de cards — Bretane Júnior Sociedade Individual de Advocacia

- `conteudo.py`, `conteudo2.py`, ... : banco de posts (cada arquivo define uma lista `POSTS...`). Para um novo lote, crie `conteudoN.py` com `POSTSN = [...]` seguindo o mesmo formato (tipos: carrossel, post, story).
- `icons.py`: ilustrações vetoriais e o mapa área → ícone (`AREA_ICON`).
- `build.py`: gera os PNGs em `out/`. Uso: `python3 build.py P41 P42 ...` (sem argumentos gera todos).
- Requisitos: `pip install playwright pillow`, Chrome/Chromium, e as fontes Playfair Display, Cormorant Garamond e Montserrat (google/fonts no GitHub) em `~/.fonts`.
- Depois de gerar: converter para JPEG (qualidade 92) em `../cards/` e fazer push para `main`.
- Regras: conteúdo apenas educativo (Provimento 205/2021 OAB); nada de nomes de clientes, números de processos ou resultados do escritório; sem promessa de resultado.
