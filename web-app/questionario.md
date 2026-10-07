# GitHub Actions — 180 questões de estudo GH-200

Questões autorais para estudo; não são itens reais nem oficiais do exame. Pesos não equivalem ao método de pontuação oficial.

Revisão: 2026-10-06. [Guia oficial](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200).

Uma alternativa correta por questão. Os IDs são estáveis. Nesta revisão, foram esclarecidos enunciados, alternativas e comentários, mantendo as letras dos gabaritos.

Terminologia: workflow é o fluxo de automação; job é um conjunto de etapas executadas em um runner; step é uma dessas etapas. Runner é a máquina ou ambiente que executa o job. Inputs são entradas, outputs são saídas e artifacts são arquivos armazenados por uma execução. Um workflow reutilizável é chamado por outro workflow, referido nas questões como chamador.

## Domínio 1 Autoria e gerenciamento de workflows

### GH200-001 · Básico

Em qual diretório do repositório devem ficar os arquivos de workflow do GitHub Actions?

- **A.** .github/workflows
- **B.** .github/actions
- **C.** .git/workflows
- **D.** actions/workflows

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O GitHub descobre workflows em .github/workflows e aceita arquivos .yml ou .yaml.

Objetivo: `workflow-diretorio`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-002 · Básico

Qual evento permite iniciar um workflow manualmente pela interface, pela CLI ou pela API?

- **A.** deployment_status
- **B.** repository_dispatch
- **C.** workflow_call
- **D.** workflow_dispatch

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** workflow_dispatch define um workflow manual e pode declarar inputs tipados.

Objetivo: `manual-dispatch`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-003 · Básico

Qual chave define o executor usado por um job?

- **A.** machine
- **B.** host
- **C.** runs-on
- **D.** runner

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** runs-on seleciona a imagem hospedada, os rótulos ou o grupo de runner aplicável.

Objetivo: `runs-on-selecao`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-004 · Básico

Qual contexto contém informações sobre o evento e o repositório que dispararam a execução?

- **A.** github
- **B.** runner
- **C.** strategy
- **D.** vars

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O contexto github contém informações da execução, do evento, do repositório e do ator.

Objetivo: `github-context`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-005 · Básico

Um step precisa definir uma variável de ambiente para os próximos steps do mesmo job. Em qual arquivo indicado pelo GitHub Actions ele deve gravar NOME=valor?

- **A.** GITHUB_STEP_SUMMARY
- **B.** GITHUB_PATH
- **C.** GITHUB_ENV
- **D.** GITHUB_OUTPUT

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A gravação em GITHUB_ENV disponibiliza a variável para steps posteriores do mesmo job.

Objetivo: `env-steps`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-006 · Intermediário

Um workflow de pull_request possui filtros branches: [main] e paths: ['src/**']. Um PR para main altera apenas README.md. O que ocorre?

- **A.** O workflow inicia porque a branch coincide
- **B.** O workflow inicia sem secrets
- **C.** O workflow não inicia porque os dois filtros precisam coincidir
- **D.** Apenas o primeiro job inicia

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Quando filtros de branch e caminho são combinados, ambos devem ser satisfeitos.

Objetivo: `filtros-branch-path`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-007 · Intermediário

O job build expõe outputs.versao. Como o job deploy deve consumir esse valor?

- **A.** Ler o resumo de build
- **B.** Ler GITHUB_ENV criado em build
- **C.** Declarar needs: build e usar needs.build.outputs.versao
- **D.** Usar runner.outputs.versao

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Outputs de job atravessam jobs por meio de needs após o mapeamento do output no produtor.

Objetivo: `job-output-needs`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-008 · Intermediário

Uma matriz combina os: [ubuntu-latest, windows-latest] com node: [20, 22]. O campo exclude remove a combinação windows-latest com Node 20, e include acrescenta macos-latest com Node 22. Quantas combinações de job serão executadas?

- **A.** 6
- **B.** 5
- **C.** 3
- **D.** 4

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A matriz base gera quatro combinações; exclude reduz para três e include adiciona uma, totalizando quatro.

Objetivo: `matrix-cartesiano`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-009 · Intermediário

Um job executa diretamente no runner ubuntu-latest, sem container de job. Ele declara um serviço PostgreSQL com ports: ["5432:5432"]. Qual endereço um script desse job deve usar para se conectar ao banco?

- **A.** postgres:5432
- **B.** localhost:5432
- **C.** runner:5432
- **D.** github:5432

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O mapeamento 5432:5432 publica a porta 5432 do container na porta 5432 do host. Como o script roda diretamente no runner, ele se conecta por localhost:5432.

Objetivo: `service-host-network`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-010 · Intermediário

Qual mecanismo produz um relatório Markdown visível na página de resumo da execução?

- **A.** GITHUB_PATH
- **B.** GITHUB_ENV
- **C.** ACTIONS_CACHE_URL
- **D.** GITHUB_STEP_SUMMARY

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Steps podem acrescentar Markdown a GITHUB_STEP_SUMMARY para formar o resumo do job.

Objetivo: `job-summary`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-011 · Avançado

Um workflow manual recebe o input booleano executar: false. Qual condição preserva corretamente o tipo do input?

- **A.** if: $EXECUTAR
- **B.** if: ${{ inputs.executar }}
- **C.** if: ${{ 'false' }}
- **D.** if: ${{ github.event.inputs.executar }}

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O contexto inputs preserva tipos em workflow_dispatch e workflow_call; github.event.inputs representa valores como strings.

Objetivo: `boolean-input`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-012 · Avançado

Um workflow faz deploy de uma branch. Quando uma nova execução dessa mesma branch começar, a equipe quer cancelar o deploy anterior que ainda estiver em andamento. Qual configuração atende a esse requisito?

- **A.** strategy.fail-fast
- **B.** timeout-minutes: 0
- **C.** concurrency com group por branch e cancel-in-progress
- **D.** continue-on-error

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Concurrency agrupa execuções ou jobs e pode cancelar uma execução anterior ainda em andamento.

Objetivo: `concurrency-cancel`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-013 · Avançado

Dois jobs precisam reutilizar o mesmo mapa env dentro de um único arquivo YAML. Qual par de recursos reduz a duplicação sem criar um workflow reutilizável?

- **A.** âncora & e alias *
- **B.** environments e secrets
- **C.** cache e artifacts
- **D.** needs e outputs

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Âncoras e aliases YAML reutilizam nós no mesmo documento. Seu resultado deve ser interpretado após a expansão.

Objetivo: `yaml-anchor-reuso`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

</details>

### GH200-014 · Avançado

Um cache usa uma chave exata e restore-keys. A restauração encontra apenas uma correspondência por prefixo. Qual afirmação é correta?

- **A.** O job é cancelado
- **B.** O cache é restaurado, mas não houve correspondência exata
- **C.** cache-hit será necessariamente true
- **D.** O cache existente é modificado no lugar

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Uma correspondência parcial pode restaurar dados, mas cache-hit indica true somente para correspondência exata da chave.

Objetivo: `cache-prefix-hit`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching).

</details>

### GH200-015 · Avançado

Um job gera um relatório em arquivo e um número de versão. Outro job precisa baixar o relatório e usar a versão em uma expressão do workflow. Como disponibilizar cada informação?

- **A.** Ambos em GITHUB_STEP_SUMMARY
- **B.** Relatório em artifact e valor curto em job output
- **C.** Relatório em secret e valor em cache
- **D.** Ambos em GITHUB_ENV

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Artefatos transferem arquivos; outputs são adequados para valores curtos entre jobs.

Objetivo: `artifact-vs-output`. [Referência](https://github.com/actions/upload-artifact).

</details>

### GH200-076 · Básico

Uma ferramenta externa precisa iniciar uma automação no repositório e enviar um payload JSON de negócio. Qual evento foi projetado para esse cenário?

- **A.** check_run
- **B.** repository_dispatch
- **C.** workflow_call
- **D.** pull_request_review

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** repository_dispatch permite integrar eventos externos por API e disponibiliza client_payload ao workflow.

Objetivo: `evento-externo`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-077 · Básico

Um agendamento usa cron '30 6 * * 1-5', sem configuração adicional de fuso. Qual é a interpretação em UTC?

- **A.** Às 18h30, de segunda a sexta-feira
- **B.** Às 06h30, de segunda a sexta-feira
- **C.** Às 06h30, somente aos domingos
- **D.** A cada 30 minutos, todos os dias

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Os campos são minuto, hora, dia do mês, mês e dia da semana; o intervalo 1-5 representa segunda a sexta.

Objetivo: `cron-utc`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-078 · Intermediário

Um workflow de pull_request deve executar um job apenas quando a branch de origem começa com 'hotfix/'. Qual expressão consulta essa branch?

- **A.** startsWith(github.repository, 'hotfix/')
- **B.** startsWith(github.base_ref, 'hotfix/')
- **C.** startsWith(github.workflow, 'hotfix/')
- **D.** startsWith(github.head_ref, 'hotfix/')

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** head_ref identifica a branch de origem do PR; base_ref identifica a branch de destino.

Objetivo: `branch-origem-pr`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-079 · Básico

Uma automação deve rodar somente quando uma issue recebe uma nova etiqueta. Qual gatilho atende ao requisito?

- **A.** issues com types: [opened]
- **B.** push com branches: [labeled]
- **C.** label com types: [created]
- **D.** issues com types: [labeled]

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** issues.labeled corresponde à aplicação de uma etiqueta a uma issue; label.created corresponde à criação da etiqueta.

Objetivo: `filtro-atividade`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-080 · Intermediário

Os testes são obrigatórios para uma merge queue e já rodam em pull_request. Qual evento deve ser incluído para validar os grupos da fila?

- **A.** merge_group com types: [checks_requested]
- **B.** workflow_dispatch com input queue
- **C.** pull_request_review com types: [submitted]
- **D.** release com types: [published]

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** A fila solicita verificações para o grupo de merge, que precisa de um gatilho próprio.

Objetivo: `merge-queue`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-081 · Intermediário

Uma equipe quer publicar pacotes quando uma release, inclusive uma pré-release, é publicada. Qual atividade de release atende a ambos os casos?

- **A.** created
- **B.** published
- **C.** edited
- **D.** deleted

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** published cobre a publicação de releases estáveis e pré-releases; created não representa necessariamente publicação.

Objetivo: `evento-release`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-082 · Básico

Em um workflow, a variável de ambiente MODE é definida no bloco env do workflow com o valor "global". No job de testes, ela é redefinida em env como "job" e, em um step desse job, como "step". Esse step executa em Bash o comando echo "$MODE", sem alterar a variável no script. Qual valor será exibido?

- **A.** step
- **B.** global
- **C.** Uma concatenação dos três valores
- **D.** job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O valor exibido é "step". Durante esse step, o env definido nele prevalece sobre o env do job ("job") e sobre o env do workflow ("global"). Os valores não são concatenados; essa declaração do step não altera o env dos demais steps.

Objetivo: `precedencia-env`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-083 · Básico

Todos os steps run de um job devem iniciar na pasta backend, que já existe no workspace. Qual configuração, declarada no nível desse job, define esse diretório padrão?

- **A.** env.working-directory: backend
- **B.** defaults.run.working-directory: backend
- **C.** strategy.directory: backend
- **D.** permissions.backend: write

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** defaults.run define padrões para os comandos run; o diretório deve existir no runner.

Objetivo: `diretorio-run`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-084 · Intermediário

Um job executa dentro de container e declara o serviço redis. Qual endereço usa para alcançar a porta padrão do serviço na rede compartilhada?

- **A.** localhost:6379 dentro do container do job
- **B.** redis:6379
- **C.** O endereço da API pública do GitHub
- **D.** github.redis:6379

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Os containers do job e dos serviços compartilham uma rede em que o identificador do serviço funciona como hostname.

Objetivo: `servico-container`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-085 · Intermediário

O teste inicia antes de o PostgreSQL aceitar conexões. Que configuração do serviço ajuda a verificar sua prontidão?

- **A.** Uma variável que muda o nome do job
- **B.** continue-on-error no teste
- **C.** permissions: contents: write
- **D.** options com um health check Docker apropriado

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Um health check permite avaliar a saúde do container antes do consumo do serviço, usando uma verificação adequada ao banco.

Objetivo: `healthcheck-servico`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-086 · Intermediário

Uma matriz deve terminar todas as variantes para coletar incompatibilidades, mesmo que uma falhe. Qual ajuste é apropriado?

- **A.** strategy.max-parallel: 1
- **B.** continue-on-error: true em todos os testes
- **C.** strategy.fail-fast: false
- **D.** needs: [] em cada step

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Desativar fail-fast evita cancelar as outras variantes por falha na matriz, preservando seus resultados individuais.

Objetivo: `matriz-fail-fast`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-087 · Intermediário

Uma matriz tem 12 combinações, mas um serviço de testes aceita no máximo três execuções simultâneas. Que ajuste limita os jobs dessa matriz?

- **A.** matrix.include: [3]
- **B.** strategy.max-parallel: 3
- **C.** strategy.fail-fast: 3
- **D.** timeout-minutes: 3

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** max-parallel limita a concorrência dentro da matriz sem remover combinações de teste.

Objetivo: `matriz-max-parallel`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-088 · Avançado

O job prepare publica o output matrix com um objeto JSON válido que descreve os eixos de uma matriz. O job consumidor declara needs: prepare. Qual expressão em strategy.matrix converte esse output de texto em uma matriz?

- **A.** strategy.matrix: ${{ hashFiles(needs.prepare.outputs.matrix) }}
- **B.** strategy.matrix: ${{ contains(needs.prepare.outputs.matrix, 'os') }}
- **C.** strategy.matrix: ${{ toJSON(needs.prepare.outputs.matrix) }}
- **D.** strategy.matrix: ${{ fromJSON(needs.prepare.outputs.matrix) }}

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** fromJSON converte o texto em objeto; toJSON serializa, enquanto as outras funções não produzem a estrutura necessária.

Objetivo: `matriz-dinamica`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

</details>

### GH200-089 · Intermediário

Um step de testes termina com falha e não usa continue-on-error. Um step posterior do mesmo job deve enviar uma notificação somente se houver falha anterior. Qual condição if atende a esse requisito?

- **A.** if: ${{ cancelled() }}
- **B.** if: ${{ success() }}
- **C.** if: ${{ failure() }}
- **D.** if: ${{ always() }}

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** failure() testa a falha anterior; always() também executaria em outras situações.

Objetivo: `status-failure`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

</details>

### GH200-090 · Avançado

O job build foi ignorado (skipped) porque sua condição if resultou em falso. O job deploy declara needs: build e não define uma condição if própria. O que acontece com deploy?

- **A.** Receberá sucesso automaticamente e executará
- **B.** Também será ignorado
- **C.** O YAML será inválido por usar needs
- **D.** Executará sem esperar build

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A dependência ignorada impede a execução normal dos jobs dependentes, salvo condição que permita prosseguir.

Objetivo: `dependencia-ignorada`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-091 · Básico

Um step com id: version deve publicar o output tag com valor v2, para ser lido depois como steps.version.outputs.tag no mesmo job. Em qual arquivo indicado pelo GitHub Actions ele deve gravar tag=v2?

- **A.** GITHUB_WORKSPACE
- **B.** GITHUB_EVENT_PATH
- **C.** GITHUB_PATH
- **D.** GITHUB_OUTPUT

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Gravar tag=v2 em GITHUB_OUTPUT cria um output do step. Com id: version, os steps posteriores podem consultá-lo pela expressão steps.version.outputs.tag. GITHUB_ENV seria usado para uma variável de ambiente, não para esse output.

Objetivo: `output-step`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-092 · Intermediário

Um step Bash acrescenta a linha MODE=prod ao arquivo indicado por GITHUB_ENV. Em seguida, tenta ler "$MODE" no mesmo script, sem atribuir nem exportar MODE no shell. Por que essa gravação, sozinha, não disponibiliza o novo valor nesse script?

- **A.** O runner reinicia o processo imediatamente com MODE atualizado
- **B.** A gravação em GITHUB_ENV é aplicada aos próximos steps; ela não atribui MODE no shell que está executando
- **C.** GITHUB_ENV só funciona entre jobs
- **D.** A variável será convertida em secret automaticamente

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O arquivo de ambiente é processado para os steps seguintes, sem alterar retroativamente o ambiente do processo escritor.

Objetivo: `env-mesmo-step`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-093 · Básico

Uma ferramenta foi instalada em uma pasta fora do PATH. Qual arquivo permite acrescentar essa pasta ao PATH dos próximos steps?

- **A.** GITHUB_STATE
- **B.** GITHUB_OUTPUT
- **C.** GITHUB_STEP_SUMMARY
- **D.** GITHUB_PATH

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** GITHUB_PATH registra diretórios para a resolução de executáveis nos steps seguintes.

Objetivo: `path-ferramenta`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-094 · Avançado

Dependências mudaram, mas a chave fixa 'linux-deps' continua restaurando um cache antigo. Qual melhoria vincula o cache às dependências declaradas?

- **A.** Trocar apenas o nome visual do step
- **B.** Repetir a mesma chave em restore-keys
- **C.** Mover o cache para GITHUB_ENV
- **D.** Incluir o hash do lockfile na chave

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Uma chave dependente do lockfile distingue conjuntos de dependências; uma chave fixa não acompanha essas alterações.

Objetivo: `cache-lockfile`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching).

</details>

### GH200-095 · Intermediário

Um workflow reutilizável declara, em on.workflow_call.inputs, o input tentativas com type: number. Como o job que chama esse workflow deve passar o número de tentativas?

- **A.** Por um artifact chamado tentativas
- **B.** Por um step run que escreve no GITHUB_ENV do caller
- **C.** Pelo with do job chamador, com valor do tipo number
- **D.** Pelo campo permissions do job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Inputs de workflows reutilizáveis são passados no with do job e devem respeitar o tipo declarado.

Objetivo: `reusable-input-type`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-096 · Avançado

Um workflow reutilizável calcula um identificador em um step. Como publicá-lo como output do workflow chamado?

- **A.** Usar somente o nome do artifact
- **B.** Declarar o valor somente em defaults.run
- **C.** Escrever apenas em GITHUB_ENV e encerrar
- **D.** Mapear output do step para output do job e depois para on.workflow_call.outputs

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O contrato de saída do reusable workflow aponta para outputs dos jobs, que podem mapear outputs de steps.

Objetivo: `reusable-output-chain`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-097 · Avançado

O workflow A chama o workflow reutilizável B usando secrets: inherit. B chama o workflow reutilizável C, mas não declara secrets nessa chamada. Considerando apenas os secrets recebidos por B de A, eles são repassados automaticamente a C?

- **A.** Sim, a herança se propaga por toda a cadeia
- **B.** Somente quando C executar antes de B
- **C.** Não; B precisa repassá-los explicitamente ou herdar novamente quando permitido
- **D.** Sim, se C usar ubuntu-latest

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A transmissão de secrets vale para a chamada direta, não para toda a cadeia de workflows.

Objetivo: `reusable-secrets-chain`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-098 · Básico

Qual chave personaliza o título de cada execução, por exemplo com o ambiente escolhido em um input?

- **A.** run-name
- **B.** jobs.name-template
- **C.** display-run
- **D.** workflow-title

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** run-name pode usar inputs para distinguir visualmente execuções do mesmo workflow.

Objetivo: `nome-execucao`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-099 · Intermediário

Um job executa diretamente no runner e declara um serviço com identificador postgres e ports: ["5432"], sem especificar a porta do host. Qual expressão do contexto job informa a porta do host atribuída ao serviço?

- **A.** runner.ports.postgres
- **B.** ${{ job.services.postgres.ports['5432'] }}
- **C.** env.GITHUB_PORT
- **D.** github.services.postgres.port

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Ao publicar apenas a porta do container, o runner atribui uma porta livre do host. O contexto job.services.postgres.ports informa esse mapeamento; não se deve presumir que a porta do host também seja 5432.

Objetivo: `service-port-dinamica`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-100 · Avançado

Um workflow define env: {REGION: x} no nível do workflow e chama um workflow reutilizável. O workflow chamado recebe automaticamente essa variável de ambiente definida pelo chamador?

- **A.** Não; deve receber a configuração por uma interface adequada, como input
- **B.** Sim, todo env do caller é copiado para todos os jobs chamados
- **C.** Somente quando o workflow estiver em outro repositório
- **D.** Sim, mas apenas para secrets

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Variáveis env definidas no nível do workflow caller não são propagadas automaticamente ao workflow chamado.

Objetivo: `reusable-env-boundary`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

</details>

### GH200-101 · Intermediário

hashFiles('**/arquivo-inexistente.lock') não encontra arquivos. Qual resultado a expressão produz?

- **A.** Uma falha obrigatória no job
- **B.** O hash do repositório inteiro
- **C.** Uma string vazia
- **D.** O nome literal do padrão

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Sem correspondências, hashFiles retorna string vazia; uma chave de cache deve considerar esse cenário.

Objetivo: `hashfiles-sem-match`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

</details>

### GH200-102 · Avançado

Um comando de integração pode travar indefinidamente. Qual configuração limita a duração total do job a 20 minutos?

- **A.** concurrency: 20
- **B.** timeout-minutes: 20 no job
- **C.** strategy.max-parallel: 20
- **D.** retention-days: 20

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** timeout-minutes estabelece o limite de execução do job, diferente de retenção, fila ou paralelismo.

Objetivo: `timeout-job`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

## Domínio 2 Consumo e diagnóstico de workflows

### GH200-016 · Básico

Onde o usuário encontra os logs de cada job e step de uma execução no GitHub?

- **A.** Apenas no arquivo README
- **B.** Somente no registro de pacotes
- **C.** Na aba Wiki
- **D.** Na aba Actions, abrindo a execução e o job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A página da execução em Actions organiza logs por job e step.

Objetivo: `ui-logs`. [Referência](https://docs.github.com/en/rest/actions/workflow-runs).

</details>

### GH200-017 · Básico

Qual resultado indica que um job não executou porque sua condição foi falsa?

- **A.** stale
- **B.** timed_out
- **C.** skipped
- **D.** failure

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Um job ou step cuja condição não é atendida aparece como ignorado, ou skipped.

Objetivo: `job-skipped`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-018 · Básico

Qual ação preserva a definição do workflow, mas impede novos disparos até sua reativação?

- **A.** Cancelar um job
- **B.** Desabilitar o workflow
- **C.** Excluir um artifact
- **D.** Excluir o arquivo

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Desabilitar interrompe novos disparos e permite reativação posterior.

Objetivo: `workflow-disable`. [Referência](https://docs.github.com/en/rest/actions/workflow-runs).

</details>

### GH200-019 · Básico

A REST API retorna status=completed e conclusion=failure para uma execução. Como interpretar esses campos?

- **A.** A execução terminou, mas falhou
- **B.** O workflow está desabilitado
- **C.** A execução foi bem-sucedida porque está completed
- **D.** A execução ainda está na fila

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** status descreve o estágio da execução, enquanto conclusion informa seu resultado após o término.

Objetivo: `status-vs-conclusion`. [Referência](https://docs.github.com/en/rest/actions/workflow-runs).

</details>

### GH200-020 · Básico

Qual mecanismo permite baixar um arquivo produzido por uma execução depois que o job termina?

- **A.** Contexto runner
- **B.** Variável env
- **C.** Artifact
- **D.** Condição if

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Artifacts preservam arquivos associados à execução durante o período de retenção.

Objetivo: `artifact-persistencia`. [Referência](https://github.com/actions/upload-artifact).

</details>

### GH200-021 · Intermediário

Uma variante Windows da matriz falhou e as variantes Linux passaram. Qual investigação inicial é mais precisa?

- **A.** Apagar o workflow
- **B.** Reexecutar indefinidamente
- **C.** Elevar permissions para write-all
- **D.** Correlacionar a variante, a imagem do runner e o log do step

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A combinação da matriz e o inventário da imagem ajudam a isolar diferenças de ambiente e ferramenta.

Objetivo: `matrix-diag`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-022 · Intermediário

Ao reexecutar apenas um job de um workflow, o que pode ocorrer com jobs dependentes?

- **A.** Eles nunca podem ser reexecutados
- **B.** O arquivo YAML é reescrito
- **C.** O GitHub pode reexecutar o job e os dependentes
- **D.** Todos os workflows do repositório são reexecutados

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A API e a interface oferecem reexecução de job com seus dependentes conforme a operação selecionada.

Objetivo: `rerun-dependent`. [Referência](https://docs.github.com/en/rest/actions/workflow-runs).

</details>

### GH200-023 · Intermediário

Um workflow atual foi corrigido, mas uma execução antiga ainda mostra o erro anterior. Qual evidência deve ser verificada?

- **A.** O tema visual do repositório
- **B.** A versão atual da branch apenas
- **C.** O SHA e o arquivo de workflow associados à execução antiga
- **D.** O último README

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A execução usa a revisão registrada para ela; alterar o arquivo atual não modifica retroativamente o YAML executado.

Objetivo: `revision-executada`. [Referência](https://docs.github.com/en/rest/actions/workflow-runs).

</details>

### GH200-024 · Intermediário

Qual distinção entre starter workflow e reusable workflow está correta?

- **A.** Ambos sempre sincronizam cópias
- **B.** Starter workflow exige Docker
- **C.** Reusable workflow só contém um step
- **D.** Starter é uma cópia; reusable workflow é uma definição central chamada por workflow_call

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Starter workflows fornecem scaffolding independente; reusable workflows centralizam jobs versionados e chamados.

Objetivo: `starter-vs-reusable`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-025 · Intermediário

Um artifact expirou conforme a política de retenção. Qual é a consequência?

- **A.** O workflow deixa de existir
- **B.** O arquivo não pode mais ser baixado daquela execução
- **C.** O repositório é arquivado
- **D.** O GITHUB_TOKEN se torna permanente

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Após expirar ou ser removido, o artifact deixa de estar disponível para download nessa execução.

Objetivo: `artifact-expirado`. [Referência](https://docs.github.com/en/rest/actions/artifacts).

</details>

### GH200-026 · Avançado

No mesmo arquivo de workflow, um job declara env: &config {MODE: teste}. Mais adiante, outro job declara env: *config. Qual configuração de ambiente o segundo job recebe ao resolver o alias YAML?

- **A.** Os outputs do primeiro job
- **B.** Uma variável chamada config com o texto MODE
- **C.** O mapa com MODE: teste
- **D.** Um mapa vazio

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O alias reutiliza o nó YAML ancorado; não executa uma transferência de outputs entre jobs. Este exemplo não depende de merge keys.

Objetivo: `yaml-alias-expansao`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

</details>

### GH200-027 · Avançado

Um reusable workflow privado não é acessível pelo caller, embora o caminho esteja correto. Qual combinação deve ser conferida?

- **A.** Cor do status badge
- **B.** Política de acesso do repositório chamado e permissões de Actions do caller
- **C.** Tamanho do artifact
- **D.** Apenas o nome do job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O repositório que hospeda o workflow precisa permitir o acesso, e o caller precisa permitir o uso da automação.

Objetivo: `reusable-private-access`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-028 · Avançado

Um job solicita um rótulo de runner que não existe entre as imagens hospedadas disponíveis nem entre os runners próprios autorizados. Ele não chega a executar nenhum step. Qual configuração deve ser corrigida?

- **A.** Erro no conteúdo do artifact
- **B.** Falta de GITHUB_STEP_SUMMARY
- **C.** Cache expirado
- **D.** Seleção de runner ou rótulo incompatível

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Falha de roteamento antes dos steps aponta para indisponibilidade, rótulos, grupo ou seleção de runner.

Objetivo: `runner-routing`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-029 · Avançado

Em um mesmo job, um step executa testes e o seguinte envia os logs como artifact. O envio deve ocorrer mesmo se os testes falharem, e o job deve continuar indicando a falha dos testes. Como configurar o envio?

- **A.** Remover os testes
- **B.** Converter logs em cache
- **C.** continue-on-error no job de teste e nenhum controle
- **D.** Configurar if: always() no step de upload e não usar continue-on-error no step de testes

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** always() permite coletar evidências; preservar o resultado de falha evita um falso sucesso.

Objetivo: `upload-failure`. [Referência](https://github.com/actions/upload-artifact).

</details>

### GH200-030 · Avançado

Qual abordagem distingue uma falha de autorização em GitHub Script de um erro de sintaxe JavaScript?

- **A.** Aumentar retenção
- **B.** Excluir o histórico
- **C.** Alterar max-parallel
- **D.** Verificar status da API, mensagem, permissões efetivas e stack trace

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Status e mensagem de API apontam autorização, enquanto a stack trace e o parse apontam erro de código.

Objetivo: `api-vs-syntax-error`. [Referência](https://github.com/actions/toolkit).

</details>

### GH200-103 · Básico

Os logs usuais de um step são insuficientes. Qual variável ou secret ativa mensagens adicionais de depuração dos steps?

- **A.** ACTIONS_STEP_DEBUG=true
- **B.** RUNNER_VERBOSE=false
- **C.** ACTIONS_CACHE_DEBUG=true
- **D.** GITHUB_LOG_LEVEL=trace

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** ACTIONS_STEP_DEBUG controla a verbosidade adicional dos steps na execução.

Objetivo: `debug-step`. [Referência](https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging).

</details>

### GH200-104 · Intermediário

A investigação precisa dos logs dos processos runner e worker, e não apenas da saída do script. O que habilitar?

- **A.** ACTIONS_ARTIFACT_DEBUG=true
- **B.** ACTIONS_STEP_SUMMARY=true
- **C.** ACTIONS_RUNNER_DEBUG=true
- **D.** GITHUB_TRACE_TOKEN=true

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A depuração do runner acrescenta logs de diagnóstico ao arquivo de logs baixado.

Objetivo: `debug-runner`. [Referência](https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging).

</details>

### GH200-105 · Intermediário

Um step com id: teste termina com código de saída 1 e está configurado com continue-on-error: true. No contexto steps.teste, quais serão os valores de outcome e conclusion?

- **A.** outcome=success e conclusion=success
- **B.** outcome=success e conclusion=failure
- **C.** outcome=failure e conclusion=success
- **D.** outcome=skipped e conclusion=cancelled

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** outcome registra o resultado antes de continue-on-error; conclusion reflete o resultado após seu tratamento.

Objetivo: `step-outcome-conclusion`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-106 · Intermediário

Um script git precisa comparar commits antigos, mas o checkout padrão trouxe apenas um commit. Qual ajuste atende ao requisito de histórico completo?

- **A.** permissions: actions: write
- **B.** timeout-minutes: 0 no job
- **C.** persist-credentials: false no checkout
- **D.** fetch-depth: 0 no checkout

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** fetch-depth controla a profundidade do histórico; zero busca todo o histórico de branches e tags.

Objetivo: `checkout-historico`. [Referência](https://github.com/actions/checkout).

</details>

### GH200-107 · Básico

Qual comando da GitHub CLI ajuda a consultar apenas logs de steps que falharam em uma execução conhecida?

- **A.** gh run view RUN_ID --log-failed
- **B.** gh repo view RUN_ID --logs
- **C.** gh workflow list --failed-only
- **D.** gh run delete RUN_ID --failed

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** gh run view permite inspecionar uma execução; --log-failed restringe a exibição aos steps com falha.

Objetivo: `cli-logs-falha`. [Referência](https://cli.github.com/manual/gh_run_view).

</details>

### GH200-108 · Avançado

Outro colaborador reexecuta uma execução. Para entender os privilégios utilizados, qual identidade deve ser considerada?

- **A.** Uma identidade anônima com acesso público
- **B.** Exclusivamente a identidade de quem clicou em reexecutar
- **C.** Sempre a identidade do proprietário da organização
- **D.** A identidade de quem disparou a execução original

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Uma reexecução usa os privilégios do ator original, embora o ator que solicitou a reexecução possa ser diferente.

Objetivo: `rerun-identidade`. [Referência](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs).

</details>

### GH200-109 · Intermediário

Como distinguir, nos metadados de uma execução, a tentativa original de suas reexecuções?

- **A.** github.event_name
- **B.** github.job
- **C.** github.repository_owner
- **D.** github.run_attempt

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** run_attempt aumenta a cada tentativa; run_id identifica a execução que está sendo tentada novamente.

Objetivo: `run-attempt`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-110 · Intermediário

Um workflow obrigatório não foi disparado porque um filtro paths excluiu os arquivos alterados. Por que o PR pode continuar bloqueado?

- **A.** O workflow excluído torna o repositório privado
- **B.** O check esperado pode permanecer Pending por não ter sido executado
- **C.** Todo filtro paths marca o check como failure
- **D.** O filtro concede aprovação de merge automaticamente

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Checks obrigatórios esperados podem continuar pendentes quando filtros impedem a execução do workflow.

Objetivo: `workflow-check-pending`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-111 · Avançado

Um workflow usa workflow_run com types: [completed]. Como executar seu job apenas quando o workflow anterior foi bem-sucedido?

- **A.** Definir continue-on-error no workflow anterior
- **B.** Testar apenas github.event_name == 'push'
- **C.** Presumir que completed significa success
- **D.** Testar github.event.workflow_run.conclusion == 'success'

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** completed indica término, não sucesso; a conclusão deve ser verificada no payload.

Objetivo: `workflow-run-conclusion`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-112 · Intermediário

Um teste funciona em branches internas, mas não recebe um secret em pull_request de um fork público. Qual causa deve ser investigada primeiro?

- **A.** A impossibilidade de usar env em pull_request
- **B.** A expiração obrigatória de todos os secrets a cada PR
- **C.** A restrição de secrets para execuções originadas em forks
- **D.** A quantidade de commits do fork

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Secrets normalmente não são fornecidos a workflows disparados por PRs de forks; não se deve contornar isso executando código não confiável com privilégios.

Objetivo: `pr-secrets-ausentes`. [Referência](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).

</details>

### GH200-113 · Intermediário

Um script usa sintaxe específica do Bash. Ele funciona diretamente em um runner Ubuntu, mas apresenta erro de sintaxe em um job que usa container e não configura shell. Qual diferença de shell pode explicar o problema?

- **A.** O shell no container sempre é PowerShell
- **B.** O container ignora a imagem declarada
- **C.** O shell padrão de run no container é sh, podendo exigir shell: bash e Bash instalado
- **D.** Containers não permitem nenhum comando run

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A sintaxe de Bash pode não ser válida em sh; a imagem também precisa conter o shell solicitado.

Objetivo: `shell-job-container`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-114 · Avançado

Com upload-artifact v4, vários jobs da matriz tentam enviar arquivos para o mesmo nome de artifact. Qual correção evita o conflito entre produtores?

- **A.** Usar o mesmo nome e aumentar timeout
- **B.** Ativar continue-on-error para consolidar os arquivos
- **C.** Usar nomes distintos por variante da matriz
- **D.** Trocar o nome visual dos jobs sem mudar o artifact

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Na v4, múltiplos jobs não podem contribuir para o mesmo artifact como antes; nomes por variante evitam colisões.

Objetivo: `artifact-nome-matriz`. [Referência](https://github.com/actions/upload-artifact).

</details>

### GH200-115 · Intermediário

Um workflow usa actions/download-artifact para baixar um artifact de uma execução anterior em outro repositório privado. Além do nome do artifact, quais informações devem ser fornecidas à action?

- **A.** Apenas GITHUB_ENV da execução antiga
- **B.** Um token OIDC de qualquer provedor de nuvem
- **C.** github-token com acesso de leitura a Actions no repositório de origem, run-id da execução e repository no formato proprietário/repositório
- **D.** Somente o nome da branch de origem

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O download fora da execução atual exige identificar a origem e autenticar com acesso ao artifact.

Objetivo: `artifact-outra-execucao`. [Referência](https://github.com/actions/download-artifact).

</details>

### GH200-116 · Básico

O badge de um workflow mostra falha em uma branch diferente da que a equipe acompanha. O que revisar no endereço do badge?

- **A.** A duração do cache
- **B.** O shell de cada step
- **C.** A permissão packages: write
- **D.** Os filtros branch e event usados no badge

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O badge pode ser parametrizado para representar uma branch ou evento específico.

Objetivo: `badge-contexto`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-117 · Intermediário

Uma action remota falha na resolução antes de executar; sua tag v9 não existe. Qual correção é pertinente?

- **A.** Referenciar uma revisão existente da action
- **B.** Definir mais eixos na matriz
- **C.** Aumentar a retenção de logs
- **D.** Adicionar um sleep ao primeiro step

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O código precisa ser resolvido em uma referência existente antes de a action ser executada.

Objetivo: `acao-nao-encontrada-ref`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-118 · Avançado

Um relatório via REST retorna apenas a primeira página do histórico e conclui que execuções antigas sumiram. Qual ajuste evita essa conclusão incorreta?

- **A.** Percorrer a paginação antes de avaliar o conjunto completo
- **B.** Aumentar o timeout dos jobs antigos
- **C.** Ordenar localmente apenas a primeira página
- **D.** Recriar o workflow com outro nome

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Listagens paginadas não representam todo o histórico em uma única resposta; a coleta precisa seguir as páginas disponíveis.

Objetivo: `paginar-api-historico`. [Referência](https://docs.github.com/en/rest/actions/workflow-runs).

</details>

### GH200-119 · Intermediário

Um workflow novo contém uma chave digitada incorretamente. Que recurso ajuda a detectar o problema antes de executá-lo?

- **A.** Executar git log sem examinar o YAML
- **B.** Publicar uma release do repositório
- **C.** Apenas renomear o arquivo para .yaml
- **D.** Validação pelo schema e extensão de GitHub Actions no editor

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Ferramentas de edição podem validar estrutura e oferecer preenchimento; isso complementa testes reais, sem substituí-los.

Objetivo: `editor-validacao`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-120 · Avançado

O YAML contém env: *shared_env, mas nenhuma âncora &shared_env foi declarada antes no documento. Qual é a causa do erro?

- **A.** O runner precisa ter mais memória
- **B.** Aliases exigem secrets de organização
- **C.** O alias referencia uma âncora inexistente no documento
- **D.** O nome env é proibido em jobs

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Um alias precisa apontar para uma âncora definida; não importa variáveis de outros arquivos automaticamente.

Objetivo: `yaml-alias-indefinido`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

</details>

## Domínio 3 Autoria e manutenção de actions

### GH200-031 · Básico

Qual arquivo descreve entradas, saídas e implementação de uma action?

- **A.** workflow.json
- **B.** action.yml ou action.yaml
- **C.** package-lock.json
- **D.** runner.yml

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Os metadados da action ficam em action.yml ou action.yaml.

Objetivo: `action-metadata-file`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-032 · Básico

Quais são os três tipos de action personalizada do GitHub Actions?

- **A.** Hosted, private e cache
- **B.** Workflow, job e runner
- **C.** Python, Java e Ruby
- **D.** JavaScript, Docker e composite

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Actions personalizadas podem ser implementadas em JavaScript, em um container Docker ou como composite actions, que reúnem steps.

Objetivo: `action-types`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-033 · Básico

Qual valor de runs.using identifica uma composite action?

- **A.** composite
- **B.** node
- **C.** workflow_call
- **D.** docker

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Composite actions declaram runs.using: composite e uma lista de steps.

Objetivo: `composite-using`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-034 · Básico

Em uma action JavaScript que usa o pacote @actions/core, qual função registra uma mensagem de erro e define um código de saída de falha?

- **A.** core.exportVariable
- **B.** core.getInput
- **C.** core.setFailed
- **D.** core.setOutput

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** core.setFailed registra a mensagem e define código de saída de falha.

Objetivo: `js-setfailed`. [Referência](https://github.com/actions/toolkit).

</details>

### GH200-035 · Básico

Qual arquivo normalmente define a imagem de uma Docker container action construída pelo repositório?

- **A.** dependabot.yml
- **B.** CODEOWNERS
- **C.** README.md
- **D.** Dockerfile

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O Dockerfile descreve a construção da imagem usada pela action quando os metadados apontam para ele.

Objetivo: `dockerfile`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-036 · Intermediário

Em uma composite action, o step com id: gerar grava resultado=ok no arquivo indicado por GITHUB_OUTPUT. Como declarar, em action.yml, um output público que exponha esse resultado ao workflow que usa a action?

- **A.** Declarar outputs no action.yml com value: ${{ steps.gerar.outputs.resultado }}
- **B.** Criar um secret
- **C.** Somente imprimir resultado
- **D.** Usar needs.gerar

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** A interface pública da action mapeia o output interno no arquivo de metadados.

Objetivo: `composite-output`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-037 · Intermediário

Um job em um runner novo tenta usar uses: ./.github/actions/teste. A action está no repositório, mas seus arquivos ainda não foram baixados para o workspace. Qual step deve ser executado antes?

- **A.** Login no Azure
- **B.** Checkout do repositório
- **C.** Upload de artifact
- **D.** Exclusão do cache

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O checkout coloca os arquivos do repositório no workspace para que a referência local exista.

Objetivo: `local-action-checkout`. [Referência](https://github.com/actions/checkout).

</details>

### GH200-038 · Intermediário

Uma action JavaScript declara runs.main: dist/index.js, mas esse arquivo não está no commit referenciado. Qual correção trata a causa?

- **A.** Aumentar permissions
- **B.** Usar continue-on-error
- **C.** Gerar e incluir dist/index.js no commit distribuído da action
- **D.** Anexar somente um ZIP à release sem alterar o commit

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O caminho runs.main precisa existir no conteúdo da referência consumida; um asset de release isolado não coloca esse arquivo no checkout da action.

Objetivo: `js-main-distribuido`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-039 · Intermediário

Qual informação deve constar no README de uma action para apoiar seu consumo seguro?

- **A.** Apenas o logotipo
- **B.** Entradas, saídas, secrets, variáveis, requisitos e exemplo de uso
- **C.** Senhas de exemplo reais
- **D.** Lista de usuários do repositório

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A documentação deve explicar o contrato, as dependências e um uso reproduzível sem expor credenciais.

Objetivo: `action-readme`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-040 · Intermediário

Uma action Docker configura entrypoint.sh para execução direta como ENTRYPOINT, sem chamar um interpretador como sh. O arquivo existe, mas não tem permissão de execução. O que deve ocorrer ao iniciar o container?

- **A.** Publicação automática no Marketplace
- **B.** Criação de um runner Windows
- **C.** Aumento automático do cache
- **D.** Falha ao iniciar o entrypoint

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O contêiner não consegue executar o ponto de entrada quando permissões ou formato do script estão incorretos.

Objetivo: `entrypoint-permission`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-041 · Avançado

Por que uma action Docker não é a escolha direta para um job em runner hospedado Windows?

- **A.** Porque container actions exigem ambiente Linux com Docker
- **B.** Porque inputs não são suportados
- **C.** Porque action.yml não funciona no Windows
- **D.** Porque outputs só existem no macOS

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Actions de contêiner Docker requerem runner Linux e Docker disponível.

Objetivo: `docker-linux`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-042 · Avançado

Uma equipe quer impedir que a referência de uma action de terceiros passe a apontar para outro código sem revisão, mas também deseja receber propostas de atualização. Qual estratégia atende aos dois objetivos?

- **A.** Fixar SHA completo verificado e automatizar a revisão de atualizações
- **B.** Usar write-all
- **C.** Referenciar @main
- **D.** Copiar o código sem licença

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O SHA completo fixa o conteúdo; um processo de atualização mantém correções sob revisão.

Objetivo: `sha-pinning`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-043 · Avançado

Uma release imutável de action já foi publicada. O mantenedor precisa corrigir um arquivo distribuído. Qual abordagem é apropriada?

- **A.** Publicar uma nova versão com a correção
- **B.** Mover a tag protegida
- **C.** Substituir silenciosamente o asset
- **D.** Editar o commit associado

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Assets e tag vinculados a uma release imutável não devem ser alterados; a correção exige nova versão.

Objetivo: `immutable-release`. [Referência](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/release-and-maintain-actions).

</details>

### GH200-044 · Avançado

Uma action vai substituir um input antigo, mas ainda precisa aceitá-lo durante a migração. Qual campo de metadados permite avisar quem continua usando esse input?

- **A.** runs.post-if no input antigo
- **B.** deprecationMessage no input antigo
- **C.** outputs.deprecated
- **D.** permissions.warning

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** deprecationMessage emite um aviso quando o input é utilizado, permitindo comunicar a substituição antes de remover a compatibilidade.

Objetivo: `input-deprecation`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-045 · Avançado

Qual escolha diferencia corretamente reusable workflow de composite action?

- **A.** Reusable workflow pode definir jobs; composite action encapsula steps no job chamador
- **B.** Ambos só podem conter um comando
- **C.** Composite action orquestra runners separados
- **D.** Reusable workflow não aceita inputs

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O nível de composição é diferente: jobs no reusable workflow e steps na composite action.

Objetivo: `composite-vs-reusable`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

</details>

### GH200-121 · Básico

Uma action recebe um parâmetro opcional e deve usar 'info' quando ele não for fornecido. Onde declarar esse padrão?

- **A.** jobs.<nome>.needs no action.yml
- **B.** permissions.default no workflow
- **C.** outputs.<nome>.required no action.yml
- **D.** inputs.<nome>.default no action.yml

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Metadados de inputs podem declarar um default para o valor não fornecido pelo consumidor.

Objetivo: `metadata-input-default`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-122 · Intermediário

Em action.yml, o autor declara um input com required: true, sem valor default. Essa declaração, sozinha, faz o runner rejeitar automaticamente a execução da action quando o input é omitido?

- **A.** Não; a implementação deve validar o input obrigatório
- **B.** Sim; o runner sempre bloqueia antes de iniciar a action
- **C.** Sim; o GitHub cria um secret com o mesmo nome
- **D.** Não; required só pode ser usado em outputs

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** required documenta a exigência, mas não gera por si só o erro de ausência; a action deve verificar o contrato.

Objetivo: `input-required-validacao`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-123 · Básico

Uma action JavaScript importa o pacote @actions/core como core. Qual função lê o valor do input chamado caminho?

- **A.** core.addPath('caminho')
- **B.** core.setOutput('caminho')
- **C.** core.exportVariable('caminho')
- **D.** core.getInput('caminho')

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** getInput lê parâmetros; as outras funções publicam saídas ou alteram o ambiente.

Objetivo: `toolkit-getinput`. [Referência](https://github.com/actions/toolkit).

</details>

### GH200-124 · Intermediário

Uma composite action declara o input destino e tenta lê-lo no Bash como "$INPUT_DESTINO", sem criar essa variável. Como disponibilizar explicitamente o input ao script?

- **A.** Mapear ${{ inputs.destino }} para uma variável env do step e ler essa variável entre aspas no Bash
- **B.** Usar secrets.INPUT_DESTINO sem declaração
- **C.** Converter a composite action em workflow_dispatch
- **D.** Definir needs.destino no script

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Composite actions não recebem automaticamente INPUT_* como outros tipos; o contexto inputs pode ser mapeado para o ambiente do step.

Objetivo: `composite-input-env`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-125 · Básico

Um step run de uma composite action precisa indicar como executar seu script. Qual propriedade deve declarar?

- **A.** workflow_call
- **B.** services
- **C.** shell
- **D.** runs-on

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Nos metadados de composite actions, steps run especificam o shell de execução.

Objetivo: `composite-shell`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-126 · Intermediário

Uma composite action precisa executar um script que acompanha seu próprio repositório. Qual contexto aponta para o diretório da action?

- **A.** github.action_path
- **B.** github.event_path
- **C.** github.head_ref
- **D.** runner.tool_cache

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** action_path identifica a localização da composite action, evitando depender do diretório do repositório consumidor.

Objetivo: `composite-action-path`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-127 · Intermediário

Uma Docker action deve receber um input como argumento de seu entrypoint. Onde mapear esse valor nos metadados?

- **A.** runs.args
- **B.** permissions.args
- **C.** strategy.args
- **D.** jobs.with

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** runs.args define os argumentos encaminhados ao container e pode referenciar os inputs da action.

Objetivo: `docker-args`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-128 · Avançado

O Dockerfile declara um ENTRYPOINT, mas action.yml também define runs.entrypoint. Qual é usado pela action?

- **A.** Nenhum; a combinação é sempre inválida
- **B.** Os dois são executados em paralelo
- **C.** Sempre o ENTRYPOINT do Dockerfile
- **D.** O entrypoint declarado nos metadados da action

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** runs.entrypoint substitui o ENTRYPOINT da imagem para essa execução.

Objetivo: `docker-entrypoint-override`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-129 · Intermediário

Uma Docker action quer produzir um arquivo para steps seguintes. Onde deve gravá-lo para compartilhar pelo workspace montado?

- **A.** Somente em /tmp privado do container
- **B.** No diretório apontado por GITHUB_WORKSPACE dentro do container
- **C.** No arquivo action.yml da instalação do runner
- **D.** Na camada da imagem original no registry

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O workspace é montado no container; arquivos gravados ali podem ser consumidos pelos steps seguintes do job.

Objetivo: `docker-workspace-mount`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-130 · Avançado

Uma action JavaScript precisa reservar um recurso antes de main e liberá-lo ao final. Quais campos descrevem esses scripts de ciclo de vida?

- **A.** on.before e on.after
- **B.** strategy.setup e strategy.cleanup
- **C.** runs.pre e runs.post
- **D.** jobs.start e jobs.finish

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Actions JavaScript podem declarar scripts pre e post; as condições correspondentes controlam sua execução.

Objetivo: `js-pre-post`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).

</details>

### GH200-131 · Avançado

Uma action JavaScript possui scripts runs.main e runs.post. O script principal precisa guardar um identificador para seu próprio script de limpeza, sem expô-lo como output público. Qual mecanismo permite essa comunicação?

- **A.** Um output de workflow_call obrigatório
- **B.** GITHUB_STEP_SUMMARY
- **C.** GITHUB_STATE ou core.saveState/core.getState
- **D.** Uma variável global no código entre processos

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O estado da action permite comunicação entre suas fases; não é uma variável global compartilhada entre processos.

Objetivo: `state-action-post`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-132 · Básico

Uma action emite dezenas de linhas de diagnóstico e quer agrupá-las em uma seção recolhível. Que comandos atendem ao objetivo?

- **A.** ::group:: e ::endgroup::
- **B.** ::set-env:: e ::set-output::
- **C.** ::add-mask:: e ::save-state::
- **D.** ::warning:: e ::error::

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Grupos organizam a apresentação dos logs sem transformar seu conteúdo em segredo nem alterar o resultado.

Objetivo: `toolkit-log-group`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-133 · Intermediário

Um step Bash, sem continue-on-error, imprime a anotação ::error::Falha detectada, mas termina com exit 0. O que o script precisa fazer para que o step seja registrado como falha?

- **A.** Emitir apenas mais uma anotação ::error::
- **B.** Adicionar um título à anotação
- **C.** Trocar a anotação por ::notice::
- **D.** Encerrar com código não zero quando houver falha

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A anotação comunica um erro visual; o processo precisa sinalizar falha com seu código de saída.

Objetivo: `error-annotation-exit`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-134 · Intermediário

Uma action JavaScript funciona no desenvolvimento, mas falha no consumidor por não encontrar um módulo npm. Como distribuir a dependência necessária?

- **A.** Solicitar packages: write ao token
- **B.** Incluir as dependências na distribuição, por bundle ou arquivos versionados adequados
- **C.** Presumir que o runner executará npm install para toda action
- **D.** Colocar package.json apenas em uma issue

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O consumidor precisa receber a implementação executável e suas dependências; instalar no ambiente do autor não as distribui.

Objetivo: `js-deps-distribuicao`. [Referência](https://github.com/actions/toolkit).

</details>

### GH200-135 · Intermediário

Uma action remove um input público usado pelos consumidores. Que mudança de versão comunica a quebra de compatibilidade segundo SemVer?

- **A.** Incrementar a versão major
- **B.** Incrementar apenas patch
- **C.** Manter exatamente a mesma versão
- **D.** Alterar somente o nome do README

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Remover uma interface pública é uma mudança incompatível; o versionamento deve permitir migração consciente.

Objetivo: `semver-breaking`. [Referência](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/release-and-maintain-actions).

</details>

### GH200-136 · Básico

Uma equipe quer publicar sua action no GitHub Marketplace. Qual característica do repositório é necessária?

- **A.** Ser público
- **B.** Ser obrigatoriamente um fork privado
- **C.** Pertencer necessariamente a uma conta pessoal
- **D.** Conter apenas arquivos binários

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** A publicação no Marketplace exige repositório público e outros requisitos de metadados e publicação.

Objetivo: `marketplace-publico`. [Referência](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace).

</details>

### GH200-137 · Avançado

O mantenedor muda o tratamento de espaços em um input de caminho. Qual teste é mais útil antes da release?

- **A.** Executar a action como consumidor com caminhos válidos, espaços e entradas inválidas
- **B.** Verificar apenas a quantidade de estrelas
- **C.** Executar somente um linter no nome da tag
- **D.** Testar apenas se README.md existe

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Um teste de contrato exercita a interface real e os casos afetados, além da análise estática.

Objetivo: `action-contrato-testes`. [Referência](https://github.com/actions/toolkit).

</details>

### GH200-138 · Avançado

Uma action JavaScript deve funcionar em Linux e Windows, mas chama um binário exclusivo do Linux. Qual conclusão é correta?

- **A.** Basta mudar o nome da action para universal
- **B.** Metadados outputs tornam o binário compatível com Windows
- **C.** A portabilidade depende também dos comandos e dependências usados, não só de ser JavaScript
- **D.** Toda action JavaScript é automaticamente portátil

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O runtime JavaScript não elimina restrições de plataforma de ferramentas externas; adapte a implementação e teste os sistemas suportados.

Objetivo: `js-multiplataforma`. [Referência](https://github.com/actions/toolkit).

</details>

## Domínio 4 Administração do GitHub Actions para empresas

### GH200-046 · Básico

Qual recurso restringe quais repositórios podem usar determinados runners auto-hospedados?

- **A.** Runner groups
- **B.** Job summaries
- **C.** Status badges
- **D.** Artifacts

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Runner groups aplicam políticas de acesso a conjuntos de runners.

Objetivo: `runner-group-access`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-047 · Básico

Qual tipo de dado deve ser armazenado em vars, em vez de secrets?

- **A.** Senha de produção
- **B.** Região padrão não confidencial
- **C.** Chave privada
- **D.** Token de acesso

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Variables armazenam configuração não confidencial; secrets protegem valores confidenciais.

Objetivo: `vars-vs-secrets`. [Referência](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).

</details>

### GH200-048 · Básico

Em qual modelo de runner a própria equipe é responsável por manter o sistema operacional da máquina que executa os jobs?

- **A.** GitHub-hosted
- **B.** Starter workflow
- **C.** Reusable workflow
- **D.** Self-hosted

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Em runners auto-hospedados, o operador mantém host, sistema, ferramentas, isolamento e capacidade.

Objetivo: `selfhost-maintenance`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-049 · Básico

Uma action precisa acessar o token automático do job por um contexto, sem criar um PAT. Qual expressão o disponibiliza?

- **A.** ${{ runner.token }}
- **B.** ${{ vars.GITHUB_TOKEN }}
- **C.** ${{ inputs.token }}
- **D.** ${{ github.token }}

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** github.token contém o GITHUB_TOKEN disponibilizado durante os steps, sujeito às permissões do job.

Objetivo: `github-token-context`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

</details>

### GH200-050 · Básico

Qual repositório especial costuma hospedar starter workflows de uma organização?

- **A.** .github
- **B.** marketplace
- **C.** .git
- **D.** runners

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O repositório .github da organização pode conter workflow-templates e seus metadados.

Objetivo: `org-template-repo`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/create-workflow-templates).

</details>

### GH200-051 · Intermediário

Uma política da empresa restringe quais actions podem ser usadas pelos repositórios da organização. Um administrador tenta liberar todas as actions nas configurações de um desses repositórios. Qual política limita essa alteração?

- **A.** A do usuário que abriu o PR
- **B.** A do runner
- **C.** A do repositório
- **D.** A restrição corporativa

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Configurações locais não ampliam o que uma política superior restringe.

Objetivo: `policy-hierarchy`. [Referência](https://docs.github.com/en/rest/actions/permissions).

</details>

### GH200-052 · Intermediário

Um runner que funcionava aparece Offline após reiniciar o servidor. Qual verificação é prioritária?

- **A.** Aumentar a retenção de artifacts
- **B.** Verificar se o serviço do runner iniciou e consegue se conectar ao GitHub
- **C.** Recriar todos os secrets do repositório
- **D.** Adicionar novos eixos à matriz

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O estado Offline exige investigar processo, serviço e conectividade do agente antes de alterar a lógica dos jobs.

Objetivo: `runner-offline-diag`. [Referência](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/monitor-and-troubleshoot).

</details>

### GH200-053 · Intermediário

Como verificar a versão de uma ferramenta preinstalada em um runner hospedado?

- **A.** Abrir o Marketplace
- **B.** Ler um secret
- **C.** Presumir a versão de latest
- **D.** Consultar o log Set up job e o inventário da imagem

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O log identifica a imagem, e o inventário ou release correspondente lista ferramentas e versões.

Objetivo: `image-inventory`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-054 · Intermediário

Uma organização oferece um workflow template não público, mas um colaborador não consegue acessá-lo. O que verificar primeiro?

- **A.** O acesso do colaborador ao repositório que contém o template e a disponibilidade do recurso no contexto da organização
- **B.** A porta Docker do runner
- **C.** A versão do Node no projeto de destino
- **D.** O nome da chave de cache

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Templates não públicos dependem de acesso ao repositório que os distribui; não são automaticamente visíveis a qualquer visitante.

Objetivo: `template-private-access`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations).

</details>

### GH200-055 · Intermediário

Qual afirmação sobre atualização de runner auto-hospedado é correta?

- **A.** Atualizar o aplicativo runner atualiza todo o sistema
- **B.** Aplicativo runner, sistema operacional e ferramentas são camadas distintas
- **C.** O GitHub mantém todos os pacotes do host
- **D.** O runner nunca precisa de atualização

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A atualização do agente não substitui a manutenção do host e de suas ferramentas.

Objetivo: `runner-update-layers`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-056 · Avançado

Uma empresa exige que actions sejam fixadas por SHA completo. Qual propriedade de política administrativa expressa esse requisito na API atual?

- **A.** runner_latest
- **B.** sha_pinning_required
- **C.** summary_required
- **D.** cache_enabled

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A política de Actions pode exigir pinning por SHA completo por meio de sha_pinning_required.

Objetivo: `api-sha-policy`. [Referência](https://docs.github.com/en/rest/actions/permissions).

</details>

### GH200-057 · Avançado

Um runner auto-hospedado em repositório público executa código de PRs de forks. Qual risco é mais crítico?

- **A.** Código não confiável pode comprometer o host persistente e seus recursos
- **B.** O YAML fica menor
- **C.** Artifacts sempre expiram
- **D.** O status badge pode mudar de cor

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Um host persistente pode reter estado e oferecer acesso a rede ou credenciais; o uso com repositórios públicos exige forte isolamento e controle.

Objetivo: `untrusted-selfhost`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-058 · Avançado

Uma organização precisa permitir acesso de runners hospedados a um serviço com allow list estática. Qual decisão deve ser avaliada?

- **A.** Desabilitar TLS
- **B.** Usar opção de rede ou runner com endereçamento controlado e manter a lista
- **C.** Imprimir todos os intervalos no log
- **D.** Assumir que ubuntu-latest tem um IP fixo

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Runners padrão usam faixas que podem mudar. Soluções com rede privada, IP estático ou runners controlados são mais adequadas ao requisito.

Objetivo: `static-network`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-059 · Avançado

Qual processo de API é necessário para definir um secret de repositório sem transmitir o valor em texto aberto no corpo?

- **A.** Publicar o valor em um artifact
- **B.** Colocar o valor em GITHUB_STEP_SUMMARY
- **C.** Gravar o valor em vars
- **D.** Obter a chave pública, criptografar o valor e enviar encrypted_value com key_id

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A REST API de secrets usa a chave pública do escopo e sealed box para o valor criptografado.

Objetivo: `secret-encryption-api`. [Referência](https://docs.github.com/en/rest/actions/secrets).

</details>

### GH200-060 · Avançado

Cinquenta repositórios chamam um workflow central por SHA. Como introduzir uma nova versão com menor risco operacional?

- **A.** Validar em consumidores piloto e atualizar as referências dos demais por mudanças revisadas
- **B.** Reescrever silenciosamente o conteúdo do SHA antigo
- **C.** Presumir atualização automática de todos os callers
- **D.** Copiar um PAT administrativo para cada caller

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Referências fixas tornam a adoção explícita; um rollout gradual permite validar compatibilidade antes de ampliar a mudança.

Objetivo: `reusable-rollout`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-139 · Básico

Vários repositórios de uma organização precisam compartilhar uma frota de runners. Em qual escopo registrá-la para esse uso?

- **A.** Um único step
- **B.** Um artifact de repositório
- **C.** Organização
- **D.** Uma release individual

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Runners no escopo da organização podem atender repositórios autorizados por suas políticas de acesso.

Objetivo: `runner-escopo-org`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-140 · Intermediário

Um job solicita um runner auto-hospedado com runs-on: [self-hosted, linux, gpu]. Entre os runners autorizados para o repositório, quais rótulos um runner deve possuir para atender ao job?

- **A.** Somente o último rótulo é considerado
- **B.** O runner deve satisfazer todos os rótulos solicitados
- **C.** Basta satisfazer qualquer um dos rótulos
- **D.** Cada rótulo cria um job separado

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A lista de labels é uma interseção de requisitos, não uma matriz nem uma escolha alternativa.

Objetivo: `runner-label-and`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-141 · Avançado

Um job deve usar um runner Linux no grupo deploy-prod. Como combinar controle de acesso e capacidade?

- **A.** Criar um artifact com o nome deploy-prod
- **B.** Usar somente env: {GROUP: deploy-prod}
- **C.** Usar runs-on com group: deploy-prod e labels: linux
- **D.** Adicionar deploy-prod ao nome visual do step

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** group seleciona o conjunto autorizado e labels restringe os runners elegíveis dentro dele.

Objetivo: `runner-group-label`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-142 · Intermediário

Qual comportamento caracteriza o registro de um runner com --ephemeral?

- **A.** Ele não precisa de autenticação ao registrar
- **B.** Ele se torna um runner hospedado pelo GitHub
- **C.** Ele processa infinitos jobs sem manter logs
- **D.** O serviço o desregistra depois de processar um job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O runner efêmero é destinado a um job; a infraestrutura ainda deve descartar ou limpar o ambiente após o uso.

Objetivo: `runner-ephemeral`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-143 · Avançado

Uma frota destrói a VM ao terminar cada job. Como preservar evidências para investigar falhas do agente?

- **A.** Encaminhar logs do runner para armazenamento externo antes do descarte
- **B.** Desativar a destruição para todos os jobs indefinidamente
- **C.** Usar apenas o nome do runner como registro
- **D.** Guardar tudo somente no disco da VM destruída

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O descarte elimina arquivos locais; a coleta externa precisa fazer parte da operação de runners efêmeros.

Objetivo: `ephemeral-logs-externos`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-144 · Básico

A equipe já opera Kubernetes e quer escalar runners de acordo com a demanda. Qual componente do ecossistema GitHub atende a essa função?

- **A.** Actions Runner Controller
- **B.** GitHub Pages
- **C.** Git LFS
- **D.** Dependabot Core

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** ARC é um operador Kubernetes para orquestrar e escalar runners auto-hospedados.

Objetivo: `arc-operador`. [Referência](https://docs.github.com/en/actions/concepts/runners/actions-runner-controller).

</details>

### GH200-145 · Avançado

Um autoscaler próprio precisa reagir à entrada e conclusão de jobs. Qual webhook fornece essas transições?

- **A.** release
- **B.** workflow_job
- **C.** member
- **D.** repository_dispatch

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** workflow_job informa estados como queued, in_progress e completed, úteis para controlar capacidade.

Objetivo: `autoscale-webhook`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-146 · Intermediário

Um runner fica offline quando o operador fecha a sessão de terminal. Como permitir que ele continue ativo no host?

- **A.** Adicionar continue-on-error a todos os jobs
- **B.** Renomear a branch principal
- **C.** Criar um novo secret de environment
- **D.** Instalar e executar o aplicativo runner como serviço conforme o sistema operacional

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O processo do runner deve permanecer ativo independentemente da sessão interativa do operador.

Objetivo: `runner-servico`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-147 · Intermediário

Um firewall bloqueia toda saída de um host runner. O que deve ser planejado para ele receber jobs e baixar componentes?

- **A.** Um registro DNS que substitua a autenticação
- **B.** Conectividade HTTPS de saída aos endpoints necessários do GitHub e dependências
- **C.** Apenas uma porta HTTP de entrada exposta à internet
- **D.** Somente acesso local ao arquivo YAML

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O agente inicia comunicação com os serviços e precisa alcançar endpoints usados por jobs e actions.

Objetivo: `runner-rede-saida`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-148 · Avançado

Após instalar um proxy corporativo com inspeção TLS, o runner apresenta erros de certificado. Qual correção preserva a verificação TLS?

- **A.** Mudar o workflow de YAML para JSON
- **B.** Publicar o token do runner para depuração
- **C.** Configurar proxy e confiança na CA corporativa nos componentes afetados
- **D.** Desativar globalmente a validação de certificados

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O agente e ferramentas precisam confiar na cadeia legítima usada pela rede; desativar validação elimina uma proteção necessária.

Objetivo: `runner-proxy-tls`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-149 · Intermediário

Um job exige uma versão específica do Python que não deve depender da versão padrão da imagem. Qual abordagem é adequada?

- **A.** Adicionar a versão ao nome do artifact
- **B.** Configurar a versão com uma action setup apropriada e validada
- **C.** Presumir que latest sempre contém a versão desejada
- **D.** Usar apenas o nome Python no título do job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Actions de configuração de runtime permitem declarar a versão usada pelo job e reduzir dependência da imagem padrão.

Objetivo: `runner-tool-install`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-150 · Avançado

A organização quer reduzir surpresas durante a migração de windows-latest para outra imagem. Qual plano é apropriado?

- **A.** Presumir que latest nunca muda
- **B.** Fixar uma imagem já descontinuada para sempre
- **C.** Ignorar diferenças de ferramentas entre imagens
- **D.** Testar a nova imagem explicitamente e fixar temporariamente uma imagem suportada na produção

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Uma transição controlada separa validação e adoção; imagens explicitamente nomeadas também precisam de manutenção e atualização.

Objetivo: `runner-latest-migration`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-151 · Básico

Um teste precisa executar instruções ARM64 nativas. Qual requisito de seleção é essencial?

- **A.** Escolher um runner compatível com ARM64 e disponível no plano ou infraestrutura
- **B.** Definir uma variável ARCH sem mudar o executor
- **C.** Usar x64 e renomear o job para arm64
- **D.** Adicionar uma tag Git chamada arm64

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O nome do job e variáveis não alteram a arquitetura real do executor.

Objetivo: `runner-arm-label`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-152 · Intermediário

Um secret de organização deve estar disponível apenas a três repositórios autorizados. Que configuração atende a isso?

- **A.** Copiar o secret para um README privado
- **B.** Marcar o secret como variável de workflow
- **C.** Política de acesso do secret para repositórios selecionados
- **D.** Disponibilizá-lo a todos e ocultar seu nome

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Secrets organizacionais permitem restringir quais repositórios podem consumi-los, conforme os recursos do plano.

Objetivo: `secret-org-selected`. [Referência](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).

</details>

### GH200-153 · Intermediário

Um job que referencia o environment prod tem secrets de mesmo nome no environment e no repositório. Qual valor prevalece quando o acesso ao environment é liberado?

- **A.** O secret do repositório sempre
- **B.** O secret com a data de criação mais antiga
- **C.** O secret do environment
- **D.** A concatenação dos valores

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Entre escopos de secrets, o escopo mais específico tem precedência; aqui, o environment.

Objetivo: `secret-precedencia`. [Referência](https://docs.github.com/en/actions/reference/security/secrets).

</details>

### GH200-154 · Básico

REGION foi cadastrada em Settings como variável de configuração do repositório, e não como secret ou variável env do YAML. Qual expressão acessa essa variável pelo contexto vars?

- **A.** ${{ secrets.REGION }}
- **B.** ${{ inputs.REGION }}
- **C.** ${{ vars.REGION }}
- **D.** ${{ runner.REGION }}

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Configurações cadastradas como variables são expostas pelo contexto vars, distinto de env, secrets e inputs.

Objetivo: `vars-context`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/variables).

</details>

### GH200-155 · Intermediário

O workflow consulta vars.DEPLOY_ZONE, mas essa variável não está definida em nenhum escopo aplicável. Qual valor recebe?

- **A.** O texto literal DEPLOY_ZONE
- **B.** String vazia
- **C.** Um objeto JSON com erro
- **D.** O nome da branch principal

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Uma referência a variável de configuração não definida retorna string vazia; requisitos devem ser validados.

Objetivo: `variable-unset`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/variables).

</details>

### GH200-156 · Avançado

Um job aguarda aprovação de environment e seu secret de environment é atualizado antes de iniciar. Em que momento esses secrets são lidos?

- **A.** Apenas na instalação do runner
- **B.** Quando o job que referencia o environment começa
- **C.** Sempre no commit que criou o workflow
- **D.** Somente no momento em que a conta foi criada

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Secrets de environment são lidos no início do job correspondente; os de organização e repositório são lidos ao enfileirar a execução.

Objetivo: `secret-read-time`. [Referência](https://docs.github.com/en/actions/reference/security/secrets).

</details>

### GH200-157 · Intermediário

O job que chama um workflow reutilizável concede contents: read ao GITHUB_TOKEN. Um workflow reutilizável chamado mais adiante nessa cadeia pode elevar, por conta própria, a permissão desse mesmo token para contents: write?

- **A.** Sim, se o workflow chamado for público
- **B.** Somente se usar uma composite action
- **C.** Sim, basta declarar write-all no chamado
- **D.** Não; as permissões podem ser mantidas ou reduzidas na cadeia

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A cadeia de reutilização não permite elevar os privilégios concedidos pelo caller.

Objetivo: `reusable-token-reduction`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

</details>

### GH200-158 · Intermediário

Um starter workflow deve adaptar seu filtro à branch padrão de cada repositório que o adotar. Qual placeholder foi criado para isso?

- **A.** $runner-os
- **B.** $repository-owner
- **C.** $workflow-sha
- **D.** $default-branch

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O placeholder do template é substituído pela branch padrão durante a criação do workflow no repositório consumidor.

Objetivo: `workflow-template-placeholder`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/create-workflow-templates).

</details>

### GH200-159 · Básico

Além do YAML de um workflow template, qual arquivo fornece nome, descrição e categorias para apresentá-lo aos usuários?

- **A.** Um arquivo correspondente .properties.json
- **B.** Um arquivo .gitmodules obrigatório
- **C.** Um secret contendo o título
- **D.** Um Dockerfile por categoria

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Os metadados do template descrevem sua apresentação e aplicabilidade na seleção de workflows.

Objetivo: `template-properties`. [Referência](https://docs.github.com/en/actions/how-tos/reuse-automations/create-workflow-templates).

</details>

### GH200-160 · Avançado

A organização define allowed_actions como selected. O que precisa complementar essa configuração para permitir uma action específica?

- **A.** A configuração do shell padrão
- **B.** Apenas um comentário no YAML
- **C.** A política de actions e workflows selecionados permitidos
- **D.** Um artifact com o código da action

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Selecionar o modo não equivale a permitir qualquer action; a lista e as categorias autorizadas completam a política.

Objetivo: `policy-selected-actions`. [Referência](https://docs.github.com/en/rest/actions/permissions).

</details>

### GH200-161 · Avançado

Uma automação consulta pela API um secret já cadastrado para recuperar sua senha original. O que deve esperar?

- **A.** Metadados do secret, sem recuperar o valor em texto aberto
- **B.** A senha codificada em base64 no campo name
- **C.** A chave privada da organização
- **D.** O valor original se acrescentar ?decrypt=true

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** A API permite gerenciar secrets sem oferecer leitura do valor original armazenado.

Objetivo: `api-secret-get`. [Referência](https://docs.github.com/en/rest/actions/secrets).

</details>

### GH200-162 · Intermediário

Uma ferramenta atualiza uma variável de configuração não confidencial via REST. Precisa usar a chave pública de secrets para criptografá-la como encrypted_value?

- **A.** Sim, mas somente se o valor contiver números
- **B.** Não; a API de variables recebe o valor de configuração no campo apropriado
- **C.** Sim, todas as variables usam sealed box
- **D.** Não, porque variables são somente leitura

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Variables e secrets têm contratos de API diferentes; variáveis não substituem o armazenamento de credenciais.

Objetivo: `api-variable-update`. [Referência](https://docs.github.com/en/rest/actions/variables).

</details>

### GH200-163 · Avançado

A empresa quer consultar e ajustar programaticamente a retenção de artifacts e logs de um repositório. Qual família de endpoints é pertinente?

- **A.** Configurações de retenção de artifacts e logs nas permissões de Actions
- **B.** Endpoints de reações a comentários
- **C.** Endpoints de Git trees
- **D.** Endpoints de criação de issues

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** A API de administração de Actions expõe configurações de retenção; a credencial precisa das permissões administrativas adequadas.

Objetivo: `retention-admin-api`. [Referência](https://docs.github.com/en/rest/actions/permissions).

</details>

### GH200-164 · Intermediário

Uma rotina deve excluir um artifact específico que já não precisa ser retido. Qual identificador deve usar no endpoint de exclusão de artifacts?

- **A.** O nome de qualquer runner
- **B.** O SHA de uma action de terceiros
- **C.** artifact_id no repositório correspondente
- **D.** O número de linha do log

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A API identifica o artifact pelo seu ID; o nome exibido não substitui esse identificador na rota de exclusão.

Objetivo: `artifact-delete-api`. [Referência](https://docs.github.com/en/rest/actions/artifacts).

</details>

### GH200-165 · Avançado

Em uma frota de runners auto-hospedados, os jobs ficam muito tempo na fila porque todos os runners compatíveis estão ocupados. Depois que conseguem um runner, executam rapidamente. Qual intervenção atua diretamente na causa da espera?

- **A.** Aumentar capacidade elegível ou ajustar o escalonamento da frota
- **B.** Aumentar o tempo máximo de cada step
- **C.** Reduzir o tamanho do README
- **D.** Adicionar cache a um step que já dura poucos segundos

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Tempo de fila elevado indica investigar capacidade e elegibilidade; otimizar somente o tempo de execução não resolve necessariamente a espera.

Objetivo: `runner-capacidade-vs-duracao`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-166 · Intermediário

Um runner Linux próprio executa scripts simples, mas falha ao iniciar uma container action por falta do daemon. O que falta preparar?

- **A.** Publicar um workflow template
- **B.** Definir secrets: inherit
- **C.** Adicionar apenas node-version ao workflow
- **D.** Instalar e disponibilizar Docker para o runner

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Container actions e serviços em runners próprios exigem a infraestrutura de containers correspondente.

Objetivo: `runner-docker-required`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

### GH200-167 · Avançado

Um repositório privado compartilha uma action com outros repositórios. Que implicação deve ser considerada antes de colocar conteúdo confidencial no código ou logs dela?

- **A.** A visibilidade privada torna qualquer saída automaticamente secreta
- **B.** Somente o autor da action consegue ler os logs de execução
- **C.** Colaboradores dos consumidores podem ter acesso indireto a conteúdo e logs da automação compartilhada
- **D.** O GitHub converte todos os arquivos da action em secrets

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Compartilhar automação amplia sua superfície de acesso; segredos não devem estar embutidos no código nem impressos nos logs.

Objetivo: `private-action-disclosure`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-168 · Avançado

Uma frota desabilitou atualizações automáticas do aplicativo runner e ficou mais de 30 dias sem aplicar uma versão disponibilizada. Que consequência documentada deve considerar?

- **A.** O GitHub atualiza obrigatoriamente todo o sistema operacional
- **B.** Os jobs passam automaticamente a runners hospedados pagos
- **C.** Somente o nome dos runners é alterado
- **D.** O serviço pode deixar de encaminhar jobs aos runners desatualizados

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Ao gerenciar atualizações manualmente, é preciso cumprir a janela de atualização do agente; atualizações críticas também podem impedir novos jobs até a correção.

Objetivo: `runner-update-prazo`. [Referência](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

</details>

## Domínio 5 Segurança e otimização da automação

### GH200-061 · Básico

Qual princípio deve orientar permissions do GITHUB_TOKEN?

- **A.** Acesso administrativo
- **B.** Permissão herdada sem revisão
- **C.** Menor privilégio
- **D.** Escrita em todos os escopos

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Conceda somente os escopos necessários e prefira leitura por padrão.

Objetivo: `least-privilege`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-062 · Básico

Qual permissão permite ao workflow solicitar um token OIDC?

- **A.** id-token: write
- **B.** contents: write
- **C.** actions: read
- **D.** packages: write

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** id-token: write permite solicitar o token OIDC; não concede por si só autorização no provedor.

Objetivo: `oidc-permission`. [Referência](https://docs.github.com/en/actions/concepts/security/openid-connect).

</details>

### GH200-063 · Básico

A equipe quer exigir revisão dos responsáveis pela automação quando arquivos em .github/workflows mudarem. Qual combinação é apropriada?

- **A.** CODEOWNERS para o caminho e uma regra aplicável que exija aprovação de code owners
- **B.** Adicionar uma estrela ao repositório
- **C.** Dar write-all a todos os jobs
- **D.** Apenas adicionar nomes em um comentário YAML

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** CODEOWNERS define responsáveis; a exigência efetiva de revisão depende das regras de proteção aplicáveis.

Objetivo: `codeowners-workflows`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-064 · Básico

Qual recurso pode exigir revisão antes de um job acessar secrets de produção?

- **A.** Proteção de environment
- **B.** Job summary
- **C.** Matrix
- **D.** Cache

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** As regras de proteção de environment podem exigir revisores, quando disponíveis no plano e configuradas.

Objetivo: `environment-review`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments).

</details>

### GH200-065 · Básico

Um atestado de artifact prova que o software não possui vulnerabilidades?

- **A.** Apenas se houver cache
- **B.** Sim, se o runner for Linux
- **C.** Sim, sempre
- **D.** Não; ele oferece evidência de proveniência e integridade

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** Atestados ajudam a verificar origem e integridade, mas não substituem testes e análise de segurança.

Objetivo: `attestation-purpose`. [Referência](https://docs.github.com/en/actions/concepts/security/artifact-attestations).

</details>

### GH200-066 · Intermediário

Um título de PR é interpolado diretamente em um bloco run. Qual correção reduz o risco de injeção?

- **A.** Desativar logs
- **B.** Passar o valor por env, aplicar quoting e validar conforme o uso
- **C.** Colocar o título no nome do job
- **D.** Dar write-all ao token

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Dados não confiáveis devem ser separados do código do shell e tratados conforme seu contexto.

Objetivo: `script-injection`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-067 · Intermediário

Qual distinção entre GITHUB_TOKEN e PAT está correta?

- **A.** Ambos são públicos
- **B.** GITHUB_TOKEN é temporário e ligado à execução; PAT representa identidade com escopo e vida próprios
- **C.** PAT sempre expira ao fim do job
- **D.** GITHUB_TOKEN acessa todos os repositórios

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** GITHUB_TOKEN é gerado para a execução e tem escopo controlado; PAT é uma credencial separada e deve ser evitado quando não necessário.

Objetivo: `token-vs-pat`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-068 · Intermediário

Uma equipe quer evitar credenciais de nuvem de longa duração. Qual desenho é recomendado?

- **A.** Federação OIDC com relação de confiança restrita
- **B.** Secret com senha sem expiração
- **C.** PAT clássico em todos os jobs
- **D.** Chave dentro do artifact

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** OIDC permite trocar uma identidade verificável do workflow por credencial temporária do provedor.

Objetivo: `oidc-federation`. [Referência](https://docs.github.com/en/actions/concepts/security/openid-connect).

</details>

### GH200-069 · Intermediário

Um cache inclui arquivos com tokens de acesso. Qual avaliação é correta?

- **A.** É seguro porque caches são secrets
- **B.** É obrigatório para acelerar
- **C.** É arriscado; dados sensíveis não devem entrar no cache
- **D.** O token é automaticamente revogado antes da gravação

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Caches podem ser acessíveis em contextos de baixa confiança conforme regras de escopo; nunca armazene credenciais neles.

Objetivo: `cache-secrets`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching).

</details>

### GH200-070 · Intermediário

Um build limitado por CPU demora muito. Como avaliar se um runner maior compensa?

- **A.** Diminuir a retenção dos logs para acelerar a CPU
- **B.** Presumir que o maior runner sempre é o mais barato
- **C.** Usar somente o número de steps como custo
- **D.** Comparar duração e custo total do mesmo workload em tamanhos adequados

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** O ganho de desempenho precisa ser comparado ao custo da capacidade; mais recursos não garantem menor custo total.

Objetivo: `runner-right-sizing`. [Referência](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

</details>

### GH200-071 · Avançado

Um workflow usa pull_request_target, faz checkout do código do fork e executa-o com token de escrita. Qual é o principal problema?

- **A.** A matriz tem uma variante
- **B.** Código não confiável recebe um contexto privilegiado
- **C.** O nome do workflow é longo
- **D.** O artifact tem retenção

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** pull_request_target pode ter privilégios no contexto base; executar código do fork nesse contexto cria risco crítico.

Objetivo: `pr-target`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-072 · Avançado

Qual conjunto de claims deve ser restringido na relação de confiança OIDC para um deploy de produção?

- **A.** Somente o nome do artifact
- **B.** Apenas o nome do runner
- **C.** Repositório, organização e branch ou environment esperados, além da audience
- **D.** Apenas o horário do job

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** A confiança deve vincular a identidade ao repositório e ao contexto de implantação autorizado, com audience adequada.

Objetivo: `oidc-trust-claims`. [Referência](https://docs.github.com/en/actions/concepts/security/openid-connect).

</details>

### GH200-073 · Avançado

Uma action tem selo de criador verificado no Marketplace. Isso dispensa revisar código, privilégios e versão antes de adotá-la?

- **A.** Somente quando usa Docker
- **B.** Sim; ela não pode acessar o token do job
- **C.** Não; a verificação do criador não equivale a uma auditoria completa do código
- **D.** Sim; toda action verificada é livre de vulnerabilidades

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** O selo informa sobre a identidade do criador, não garante ausência de comportamento inseguro ou vulnerabilidades.

Objetivo: `verified-not-audit`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-074 · Avançado

Uma pipeline gera atestado para um binário. Qual verificação é necessária antes do deploy?

- **A.** Apenas conferir o nome do arquivo
- **B.** Confirmar assinatura, digest, repositório, workflow e identidade esperados pela política
- **C.** Conferir a cor do badge
- **D.** Verificar se o cache foi hit

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A decisão deve validar o artifact e os atributos de proveniência contra a política de implantação.

Objetivo: `provenance-policy`. [Referência](https://docs.github.com/en/actions/concepts/security/artifact-attestations).

</details>

### GH200-075 · Avançado

Um upload define retention-days maior que o máximo permitido pela política aplicável ao repositório. Qual abordagem é correta?

- **A.** Adequar a retenção ao limite permitido ou solicitar ajuste autorizado da política
- **B.** Converter o arquivo em output de job para torná-lo permanente
- **C.** Presumir que o input ignora os limites administrativos
- **D.** Trocar o nome do artifact para estender a retenção

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** A retenção por artifact deve respeitar os limites aplicáveis; ela não é uma forma de contornar a política administrativa.

Objetivo: `retention-artifact-limite`. [Referência](https://github.com/actions/upload-artifact).

</details>

### GH200-169 · Intermediário

Um job declara permissions: {contents: read}. Qual é o efeito sobre escopos configuráveis não mencionados, como issues?

- **A.** Ficam sem permissão, em vez de manter escrita implicitamente
- **B.** Tornam-se iguais a contents: read
- **C.** Recebem write por padrão
- **D.** Herdam sempre o PAT do proprietário

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** Ao especificar permissões, os escopos não listados são definidos como none, observadas as regras documentadas do token.

Objetivo: `token-unspecified-none`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

### GH200-170 · Avançado

Um workflow faz push usando GITHUB_TOKEN, mas outro workflow de push não inicia. Qual regra explica esse caso?

- **A.** O segundo workflow precisa usar apenas Windows
- **B.** Push nunca pode iniciar workflows
- **C.** Todo push de bot é apagado automaticamente
- **D.** Eventos gerados por GITHUB_TOKEN normalmente não iniciam novas execuções, com exceções como dispatch

<details>
<summary>Gabarito e explicação</summary>

**Resposta: D.** A prevenção de recursão suprime novos disparos gerados pelo token; workflow_dispatch e repository_dispatch são exceções documentadas.

Objetivo: `token-push-recursion`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

</details>

### GH200-171 · Intermediário

Um step obtém uma credencial temporária de um serviço externo. Como reduzir sua exposição nos logs seguintes?

- **A.** Registrar o valor com add-mask antes de qualquer impressão e evitar logá-lo
- **B.** Escrever o valor no job summary
- **C.** Confiar que todo valor de API é mascarado automaticamente
- **D.** Transformar a credencial em nome do artifact

<details>
<summary>Gabarito e explicação</summary>

**Resposta: A.** O mascaramento precisa conhecer valores gerados dinamicamente; não substitui evitar sua saída nem protege arquivos anexados.

Objetivo: `mask-dynamic-secret`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).

</details>

### GH200-172 · Avançado

Uma credencial foi exposta em um log que outras pessoas puderam acessar. Qual resposta deve ser priorizada?

- **A.** Criar uma variável com o mesmo valor
- **B.** Apenas renomear o secret
- **C.** Revogar ou rotacionar a credencial e tratar os registros expostos
- **D.** Reexecutar o workflow sem alterar a credencial

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Apagar um log não invalida cópias já obtidas; revogação ou rotação contém o uso posterior da credencial comprometida.

Objetivo: `secret-leak-response`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-173 · Intermediário

Um deploy exige aprovação independente da pessoa que iniciou a execução. Qual proteção, quando disponível, atende a esse objetivo?

- **A.** Um input booleano chamado aprovado
- **B.** Prevent self-review nas regras do environment
- **C.** Uma matriz com dois sistemas operacionais
- **D.** continue-on-error no deploy

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Impedir autoaprovação separa solicitante e aprovador; um input não substitui uma regra de proteção.

Objetivo: `environment-prevent-self-review`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments).

</details>

### GH200-174 · Intermediário

Produção só deve receber deploys de branches ou tags autorizadas. Onde impor essa restrição adicional ao gatilho do workflow?

- **A.** Na cor do badge
- **B.** Nas regras de deployment branches and tags do environment
- **C.** No campo description do input
- **D.** No nome do artifact

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** O environment pode restringir as referências elegíveis para implantação, além de filtros presentes no YAML.

Objetivo: `environment-branch-rule`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments).

</details>

### GH200-175 · Avançado

Um workflow privilegiado disparado por workflow_run baixa um artifact de um PR e executa um script contido nele. Qual é o risco?

- **A.** Artifacts são sempre assinados pelo autor do repositório
- **B.** O artifact pode transportar código não confiável para o contexto privilegiado
- **C.** workflow_run remove todo conteúdo executável
- **D.** A única consequência possível é um cache miss

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** A origem de um arquivo importa tanto quanto a do código no checkout; cruzar essa fronteira requer validação e desenho seguro.

Objetivo: `workflow-run-untrusted-artifact`. [Referência](https://docs.github.com/en/actions/reference/security/secure-use).

</details>

### GH200-176 · Intermediário

Como propor atualizações periódicas de versões ou SHAs de actions por pull request?

- **A.** Trocar todas as referências por main
- **B.** Criar um job que aceite qualquer atualização sem revisão
- **C.** Configurar o ecossistema github-actions no Dependabot
- **D.** Habilitar apenas o ecossistema pip

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Dependabot oferece suporte a dependências de GitHub Actions, permitindo revisar mudanças propostas.

Objetivo: `dependabot-actions`. [Referência](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot).

</details>

### GH200-177 · Avançado

O provedor rejeita um token OIDC porque aud não corresponde à audiência esperada. Qual ajuste corrige a relação de confiança?

- **A.** Colocar o token OIDC no repositório
- **B.** Alinhar a audience solicitada e a esperada pelo provedor, preservando as restrições de identidade
- **C.** Conceder contents: write ao job
- **D.** Remover todos os testes de subject

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Audience indica o destinatário do token; a verificação deve corresponder ao uso autorizado sem ampliar indiscriminadamente a confiança.

Objetivo: `oidc-audience-mismatch`. [Referência](https://docs.github.com/en/actions/concepts/security/openid-connect).

</details>

### GH200-178 · Intermediário

Um cache leva mais tempo para compactar e transferir do que a instalação que substitui. Qual decisão é mais adequada?

- **A.** Manter o cache porque todo hit reduz necessariamente o tempo total
- **B.** Aumentar o número de arquivos armazenados sem medir
- **C.** Medir o fluxo completo e ajustar o conteúdo ou deixar de usar esse cache
- **D.** Converter logs e artifacts em dependências

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Cache tem custos de leitura, compressão e transferência; seu valor depende da economia líquida observada.

Objetivo: `cache-economia-medida`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching).

</details>

### GH200-179 · Avançado

Uma auditoria pede o inventário de componentes e dependências que compõem um binário. Que evidência atende especificamente a esse pedido?

- **A.** Apenas o nome do runner que executou o build
- **B.** Uma SBOM associada ao artifact
- **C.** Somente o horário de início do workflow
- **D.** Somente o número da tentativa da execução

<details>
<summary>Gabarito e explicação</summary>

**Resposta: B.** Uma SBOM descreve componentes e dependências; metadados sobre onde e quando o build ocorreu não substituem esse inventário.

Objetivo: `sbom-vs-proveniencia`. [Referência](https://docs.github.com/en/actions/concepts/security/artifact-attestations).

</details>

### GH200-180 · Intermediário

Um workflow tem um job de testes e outro de publicação de pacotes. Somente o job de publicação precisa da permissão packages: write no GITHUB_TOKEN. Em qual nível essa permissão deve ser declarada para limitar seu alcance?

- **A.** No nível global com write-all para todos
- **B.** Em uma variável de nome packages_write
- **C.** No job de publicação, mantendo os demais com os privilégios necessários
- **D.** No nome visual do step que faz upload

<details>
<summary>Gabarito e explicação</summary>

**Resposta: C.** Permissões por job permitem limitar o alcance da credencial de publicação em relação às etapas de teste.

Objetivo: `permissions-job-boundary`. [Referência](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

</details>

