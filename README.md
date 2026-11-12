# Página Pombo AI

Site institucional (landing page) do aplicativo **Pombo AI** — app de nutrição com inteligência artificial que estima calorias e macronutrientes a partir de uma foto da refeição.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | A página inteira: HTML, CSS e JavaScript em um só arquivo |
| `robots.txt` | Libera a indexação para Google e para as IAs (ChatGPT, Gemini, Perplexity, Claude) |
| `sitemap.xml` | Mapa do site para os buscadores |

## Como publicar

O site é estático, então basta subir os três arquivos em qualquer hospedagem. Na Vercel, é só conectar este repositório e fazer o deploy — não precisa configurar nada.

## O que falta preencher

Antes de colocar no ar, troque estes marcadores:

- `SEU-DOMINIO.com.br` — aparece no `index.html`, no `robots.txt` e no `sitemap.xml`
- Links da App Store e do Google Play (estão como `#`)
- Usuários do Instagram e do TikTok (`SEU_USUARIO`)
- Prints das telas do app (os retângulos marcados como `[Print do app: ...]`)
- Depoimentos reais de usuários, com autorização deles
- Destino do formulário de imprensa (o `action` está como `#`)
- E-mail de contato no FAQ

## Recursos da página

- Três temas: claro, escuro e azul, com o botão no topo guardando a escolha
- Layout responsivo
- SEO: título, descrição, canonical, Open Graph, JSON-LD (SoftwareApplication) e hierarquia de títulos H1 → H2 → H3
