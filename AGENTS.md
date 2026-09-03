# Agentes — validate-docbr

## Contextos

O recorte deste repositório, lido pelo `/review-pr`. Um agente que atua num
contexto está apto a revisar **qualquer coisa** daquele contexto — código, doc,
migration, config, teste. A revisão de um PR é a união dos contextos que o diff
toca, mais os transversais, cortada no teto de 5 revisores.

A coluna Agentes contém só nomes — é ela que o `task ai:agents-doc MODE=check`
valida contra `.claude/agents/`. Instrução vai na Lente.

| Contexto | O que pertence a ele | Agentes | Lente |
|---|---|---|---|
| biblioteca | `validate_docbr/`, `pyproject.toml` | `python-expert`, `reviewer` | É biblioteca pública: mudança de assinatura ou de retorno é breaking change e precisa de nota no CHANGELOG. Validador de documento brasileiro tem regra de negócio legal — máscara e dígito verificador não se ajustam por conveniência. |
| testes | `tests/` | `test-runner`, `python-expert` | Documento novo suportado precisa de caso válido, inválido e de borda (tudo zero, tamanho errado, com e sem máscara). |
| empacotamento | `Dockerfile`, `docker-compose.yml`, `Taskfile.yml`, `.github/`, `uv.lock` | `python-expert` | Dependência nova numa lib pública é custo pra quem instala: justifique. `uv.lock` acompanha o `pyproject.toml` no mesmo PR. |
| docs | `docs/`, `README.md`, `CONTRIBUTING.md`, `CLAUDE.md` | `reviewer` | README é a porta de entrada da lib: exemplo que não roda é bug. Doc em pt-BR. |

## Transversais

Entram numa revisão quando o **gatilho** dispara, não por padrão — revisor acordado
por reflexo é ruído no veredito e come o teto de 5 do `/review-pr`. `sempre` é o
gatilho de quem entra em toda revisão; glob casa contra os arquivos do diff;
palavra casa, sem distinguir maiúscula, contra caminhos e texto do diff.

| Agente | Gatilho | Lente |
|---|---|---|
| `reviewer` | `sempre` | repositório **público** de biblioteca instalada por terceiros: API estável, sem segredo, sem dado de exemplo que seja documento real de alguém. |

## Catálogo

<!-- catálogo gerado por `task ai:agents-doc` — não edite à mão -->

| Agente | Contexto (do frontmatter) |
|---|---|
| `python-expert` | Python development expert for validate-docbr. |
| `reviewer` | Reviews validate-docbr code for conformance with project patterns. |
| `test-runner` | Runs project tests via Docker and reports results. |
