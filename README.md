# gerente360

Landing e materiais da marca **Sua Gerente IA** (@suagerente360).

## Conteúdo

- `index.html`: landing do teste grátis (https://projeto.gerente360.com.br). Página estática única, sem build.
- `cards/gen.py`: gerador dos cards do feed do Instagram (1080x1350, via Playwright).

## Publicação

Cloudflare Pages, projeto `gerente360` (https://gerente360.pages.dev), com o domínio `projeto.gerente360.com.br` via CNAME no GoDaddy.

Para publicar direto do GitHub: Workers & Pages > gerente360 > Settings > Builds, conectando este repositório, sem comando de build e com a raiz como diretório de saída. As imagens dos posts (`posts/*.jpg`) não ficam aqui: gere com `cards/gen.py` e converta para JPEG.

## Cards

```bash
pip install playwright pillow && playwright install chromium
cd cards && python3 gen.py
```
