[![Workflow Dispatch](https://github.com/Dyego-Barros/gh-200/actions/workflows/workflow_dispatch.yml/badge.svg)](https://github.com/Dyego-Barros/gh-200/actions/workflows/workflow_dispatch.yml)

# GH-200 — Aplicação de estudos

Aplicação em Python 3.12+, Flask, SQLAlchemy, SQLite, Alembic e Bootstrap 5.3.8 (CSS local, com licença no cabeçalho). A organização orientada a objetos separa modelos, importador e serviço de estudos; a fábrica Flask configura as rotas e o banco.

## Executar localmente

Com Python 3.12 ou superior e `uv` instalado, execute na raiz deste repositório:

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python app.py
```

Ative o ambiente com `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`). Depois, basta executar `python app.py`. O comando aplica as migrações, importa o questionário e inicia o servidor em http://127.0.0.1:8080. Para escolher outra porta, use `PORT=8081 python app.py`. No Windows, substitua `.venv/bin/python` por `.venv/Scripts/python.exe`.

Alternativa sem uv: `python3 -m venv .venv` e `.venv/bin/python -m pip install -r requirements.txt`; os demais comandos são iguais.

Para preparar o banco sem iniciar o servidor, use `.venv/bin/python -m flask --app quiz setup`. Depois, também é possível iniciar com `.venv/bin/python -m flask --app quiz run --port 8080`.

O terminal exibe o caminho absoluto do banco criado em `instance/quiz.sqlite`. Abra a URL HTTP indicada; o arquivo `quiz/templates/index.html` depende do Flask e não deve ser aberto diretamente. A porta 6000 é bloqueada por navegadores e a 5000 pode conflitar com o AirPlay no macOS.

## Funcionamento

- Importa `questionario.md`: 180 questões (46 básicas, 75 intermediárias e 59 avançadas). Níveis, áreas, alternativas e comentários são extraídos do documento, sem classificação inventada.
- Valida numeração e total declarado no título, quatro alternativas A–D, gabarito de cada questão e pelo menos 20 questões por nível antes de gravar a transação.
- A reimportação da mesma fonte confere todos os campos e não duplica dados. Uma fonte alterada cria uma nova versão identificada por SHA-256 para novos sorteios; questões anteriores são preservadas para manter as rodadas e seus resultados.
- Na página inicial, selecione um ou mais níveis. Com os três, cada rodada sorteia 60 questões únicas, 20 por nível. Com dois, são 30 por nível. Com apenas um, são até 60 questões, limitadas ao total disponível (atualmente 46 básicas, 60 intermediárias ou 59 avançadas). O prazo permanece em 100 minutos.
- O prazo de 100 minutos é persistido no servidor. Recarregar ou fechar a página não reinicia o relógio. Após o prazo, respostas novas são rejeitadas; a rodada é encerrada no próximo acesso.
- As respostas são salvas ao selecionar, com indicação de sucesso ou falha. Sem JavaScript, utilize “Salvar respostas”. Somente respostas recebidas pelo servidor antes do prazo são consideradas.
- O resultado apresenta total de acertos, percentual sobre o total de questões da rodada, desempenho por domínio e nível e revisão com gabarito comentado. Questões em branco contam como erro.
- Uma rodada ativa com os mesmos níveis é retomada ao clicar em iniciar. Selecionar outros níveis cria outra rodada; as anteriores continuam acessíveis pelo histórico. Rodadas finalizadas são imutáveis. O histórico pertence ao navegador por cookie de sessão; não há cadastro ou autenticação de usuários. Limpar os cookies remove o acesso ao histórico daquele navegador.

## Dados e configuração

O banco fica em `instance/quiz.sqlite`. A chave de sessão é gerada em `instance/secret.key` com permissão restrita; preserve-a para manter acesso às sessões. Ambos são ignorados pelo Git. Para backup local, pare o servidor e copie o diretório `instance/`.

As variáveis de ambiente `DATABASE_URL` (URL SQLite) e `SECRET_KEY` podem substituir os padrões. O arquivo `.env` existente não é carregado automaticamente. O servidor Flask descrito acima destina-se ao uso local. Em uma publicação futura, utilize servidor WSGI e HTTPS, com `SESSION_COOKIE_SECURE=True`.

As migrações versionadas estão em `migrations/`. Para mudanças futuras de esquema, revise a migração gerada por `.venv/bin/python -m alembic revision --autogenerate -m "descrição"` e aplique com `flask --app quiz init-db`. O comando Flask usa a URL configurada; o CLI Alembic direto usa `alembic.ini`.

## Testes

```bash
uv pip install --python .venv/bin/python pytest
.venv/bin/python -m pytest -q
```

Os testes criam bancos temporários e executam as migrações reais. Cobrem a importação e seu bloqueio em caso de corrupção, correspondência dos dados persistidos com o documento, idempotência, sorteio, retomada, pontuação, imutabilidade, prazo, validação das respostas, isolamento entre sessões, ausência de gabarito durante a rodada e proteção CSRF.
