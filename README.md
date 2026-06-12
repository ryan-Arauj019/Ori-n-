# ✦ Orion IA — Guia de Deploy no Render

## Arquivos do projeto

```
nova-flask/
├── app.py              ← servidor Flask (cérebro do projeto)
├── requirements.txt    ← bibliotecas necessárias
├── render.yaml         ← configuração do Render
└── static/
    └── index.html      ← interface do chat
```

---

## Passo 1 — Criar conta no Hugging Face

1. Acesse https://huggingface.co e crie uma conta grátis
2. Vá em **Settings → Access Tokens**
3. Clique em **New Token** → dê um nome → copie o token

---

## Passo 2 — Subir o projeto no GitHub

1. Crie uma conta em https://github.com (se não tiver)
2. Crie um repositório novo chamado `orion-ia`
3. Faça upload de todos os arquivos desta pasta

---

## Passo 3 — Deploy no Render

1. Acesse https://render.com e crie uma conta
2. Clique em **New → Web Service**
3. Conecte seu repositório GitHub `orion-ia`
4. Configure:
   - **Runtime:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Em **Environment Variables**, adicione:
   - Key: `HF_API_KEY`
   - Value: (cole seu token do Hugging Face)
6. Clique em **Deploy**

---

## Passo 4 — Acessar e compartilhar

Após o deploy, o Render vai gerar um link assim:
```
https://orion-ia.onrender.com
```

Compartilhe esse link com seus amigos! 🎉

---

## Custo

- Render (plano grátis): $0
- Hugging Face (Qwen): $0
- **Total: $0** 🎉

> ⚠️ No plano grátis do Render, o servidor "dorme" após 15 min sem uso.
> Na primeira mensagem depois disso, pode demorar ~30 segundos pra acordar.
