# Music Weekly

Uma newsletter semanal, simples, com apresentações musicais completas publicadas no YouTube.

O projeto usa a YouTube Data API v3 para ler os uploads de cada canal, seleciona os vídeos desejados e envia um e-mail em HTML.

> Antes usava o feed RSS público do YouTube, mas esse feed só retorna os 15 uploads mais recentes de cada canal, então vídeos podiam ficar de fora quando o canal postava bastante coisa na semana. A API resolve isso porque permite paginar e buscar todos os uploads dos últimos 7 dias, não só os 15 mais recentes.

## Como funciona

1. Lê os canais definidos em `src/channels.py`.
2. Para cada canal, busca os uploads recentes via YouTube Data API.
3. Mantém títulos que contenham alguma palavra em `keep` e descarta os que contenham uma palavra em `ignore`.
4. Considera apenas vídeos publicados nos últimos sete dias que ainda não foram enviados.
5. Gera o e-mail, envia-o e só então registra os vídeos no histórico.

## Configuração da API do YouTube

1. Crie uma chave de API gratuita no Google Cloud Console (veja o passo a passo que te enviei junto com este código).
2. Copie `.env.example` para um arquivo chamado `.env` e cole a chave em `YOUTUBE_API_KEY`.
3. No GitHub, adicione a mesma chave como um "Repository secret" chamado `YOUTUBE_API_KEY` (Settings → Secrets and variables → Actions).

## Configuração do e-mail

Copie `.env.example` para um arquivo chamado `.env` e preencha os dados do seu provedor de e-mail. Esse arquivo não é enviado ao GitHub.

> Para Gmail, use uma senha de aplicativo — não a sua senha normal.

Antes de executar, disponibilize essas variáveis no terminal com `set -a; source .env; set +a`.

## Executar manualmente

Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```

Depois de definir as configurações de e-mail e da API, execute:

```bash
python3 src/main.py
```

O arquivo `newsletter.html` também é criado localmente como uma cópia para conferência. Se o envio falhar, nenhum vídeo é adicionado ao histórico.

## Adicionar ou ajustar canais

Edite `src/channels.py`. Cada canal tem o ID do YouTube, palavras para manter (`keep`) e palavras para ignorar (`ignore`).
