# Página Pombo AI

Site institucional (landing page) do aplicativo **Pombo AI** — app de nutrição com inteligência artificial que estima calorias e macronutrientes a partir de uma foto da refeição.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | A página inicial |
| `imprensa.html` | Página de imprensa e sugestões, com o formulário de contato |
| `politica-de-privacidade.html` | Política de privacidade, escrita a partir do que o app realmente coleta |
| `termos-de-uso.html` | Termos de uso |
| `politica-de-reembolso.html` | Como cancelar e pedir reembolso na App Store e na Google Play |
| `politica-de-cookies.html` | Política de cookies do site e do aplicativo |
| `assets/site.css` | Todo o visual do site (cores, tipografia, espaçamentos) |
| `assets/pombo-icon.png` | Logo do Pombo AI, usada no topo, no rodapé e nas redes sociais |
| `assets/favicon.png` | Ícone que aparece na aba do navegador |
| `robots.txt` | Libera a indexação para Google e para as IAs (ChatGPT, Gemini, Perplexity, Claude) |
| `sitemap.xml` | Mapa do site para os buscadores |

## Como publicar

O site é estático, então basta subir a pasta inteira em qualquer hospedagem. Na Vercel, é só conectar este repositório e fazer o deploy — não precisa configurar nada.

## Os selos da App Store e do Google Play

Os dois selos já estão na pasta `assets/`, recortados de uma imagem enviada pelo próprio dono do app, com o fundo das bordas transparente.

Eles vieram de uma captura de tela pequena, então estão um pouco menos nítidos do que o original. Se quiser a versão perfeita, baixe a arte oficial e substitua os arquivos mantendo os mesmos nomes:

| Substituir | Onde baixar |
|---|---|
| `assets/selo-app-store.png` | Apple, em `developer.apple.com/app-store/marketing/guidelines/` |
| `assets/selo-google-play.png` | Google, em `play.google.com/intl/pt-BR/badges/` |

A Apple e o Google pedem que a arte deles seja usada sem alterações de cor, proporção ou texto.

## O que falta preencher

Antes de colocar no ar, troque estes marcadores:

- `SEU-DOMINIO.com.br` — aparece no `index.html`, no `imprensa.html`, no `robots.txt` e no `sitemap.xml`
- Links da App Store e do Google Play (os `href` estão como `#`)
- Usuários do Instagram e do TikTok (`SEU_USUARIO`)
- Prints das telas do app (os retângulos marcados como `[Print do app ...]`), inclusive os três da seção de temas: um no modo claro, um no escuro e um no azul
- **CNPJ, endereço e encarregado de dados da Dandtecno** — procure por `[PREENCHER` nas páginas legais
- Depoimentos reais de usuários, com autorização de quem escreveu. A seção está comentada no `index.html`, com as instruções dentro
- Destino do formulário de imprensa (o `action` está como `#`)
- E-mail de contato, nas perguntas frequentes

## Decisões de design

- **Cores** tiradas do próprio mascote: cinza-ardósia, verde e roxo iridescentes, sobre um fundo creme.
- **Tipografia**: Fraunces nos títulos (dá personalidade) e Instrument Sans no texto corrido (boa leitura em tela). Carregadas do Google Fonts.
- **Espaçamentos** seguem uma escala fixa de 4 em 4 pixels, declarada no topo do CSS.
- O site tem **um tema só**, o claro. Os três modos (claro, escuro e azul) são do aplicativo e aparecem no site apenas como exemplo, na seção de temas.
