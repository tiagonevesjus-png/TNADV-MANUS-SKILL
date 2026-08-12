# TNADV MANUS SKILL

Plugin do Claude Code com as skills jurídicas do escritório **Tiago Neves Advocacia
Empresarial**. O repositório funciona ao mesmo tempo como *plugin* e como
*marketplace*, então pode ser instalado direto do GitHub.

## Instalação

No Claude Code:

```
/plugin marketplace add tiagonevesjus-png/tnadv-manus-skill
/plugin install tnadv-juridico@tnadv-manus-skill
```

Para desenvolver localmente, aponte o marketplace para o clone:

```
/plugin marketplace add ./caminho/para/tnadv-manus-skill
```

## Conteúdo

| Tipo | Nome | Descrição |
| --- | --- | --- |
| Skill | `auditor-forense-juridico` | Auditoria forense crítica de peças, recursos, contratos, pareceres e estratégias processuais. |
| Comando | `/tnadv-juridico:auditoria-forense` | Dispara a auditoria de um documento específico. |

A skill é acionada automaticamente quando o pedido envolve auditar, revisar
criticamente ou encontrar vulnerabilidades técnicas, probatórias e processuais em
material jurídico. O comando serve para acionar a auditoria de forma explícita sobre
um arquivo.

## Estrutura

```
.claude-plugin/
  plugin.json         manifesto do plugin
  marketplace.json    manifesto do marketplace
commands/
  auditoria-forense.md
skills/
  auditor-forense-juridico/
    SKILL.md          instrução permanente (Modo Crítico)
    README.md         uso, segurança e política de dados
    audit.json        configuração dos scripts
    run_audit.py      validação de entrada / execução de teste
    generate_report.py
```

## Avisos

- As análises são **técnicas e hipotéticas**, com base no material fornecido. Não
  substituem parecer formal de advogado habilitado.
- Não comite documentos sigilosos, autos ou peças reais neste repositório.
- Frases de desativação e demais segredos ficam em variáveis de ambiente
  (ex.: `SKILL_DEACTIVATION_PHRASE`), nunca no código.

Contato: tiagoneves.jus@gmail.com
