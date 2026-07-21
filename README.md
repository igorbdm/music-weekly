# Music Weekly

Uma newsletter semanal, simples, com apresentações musicais completas publicadas no YouTube.

O projeto lê os feeds RSS oficiais dos canais, seleciona os vídeos desejados e envia um e-mail em HTML. Não utiliza a API do YouTube.

## Como funciona

1. Lê os canais definidos em `src/channels.py`.
2. Mantém títulos que contenham alguma palavra em `keep` e descarta os que contenham uma palavra em `ignore`.
3. Considera apenas vídeos publicados nos últimos sete dias que ainda não foram enviados.
4. Gera o e-mail, envia-o e só então registra os vídeos no histórico.

## Configuração do e-mail

Copie `.env.example` para um arquivo chamado `.env` e preencha os dados do seu provedor de e-mail. Esse arquivo não é enviado ao GitHub.

> Para Gmail, use uma senha de aplicativo — não a sua senha normal.

Antes de executar, disponibilize essas variáveis no terminal com `set -a; source .env; set +a`.

## Executar manualmente

Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```

Depois de definir as configurações de e-mail, execute:

```bash
python3 src/main.py
```

O arquivo `newsletter.html` também é criado localmente como uma cópia para conferência. Se o envio falhar, nenhum vídeo é adicionado ao histórico.

## Adicionar ou ajustar canais

Edite `src/channels.py`. Cada canal tem o ID do YouTube, palavras para manter (`keep`) e palavras para ignorar (`ignore`).
