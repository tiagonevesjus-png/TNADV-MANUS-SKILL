# Auditor Forense Jurídico - Uso e Segurança

Este diretório contém a skill "Auditor Forense Jurídico" (modo crítico permanente) para análise técnica de peças jurídicas.

Avisos importantes
- Esta ferramenta fornece análises TÉCNICAS e HIPOTÉTICAS com base no material fornecido. Não substitui parecer formal de advogado habilitado.
- Nunca envie documentos sigilosos sem autorização.

Recomendações rápidas antes de rodar localmente
- Use virtualenv/venv:
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt  # adicionar requirements.txt conforme necessidade

- Não comite arquivos de entrada nem documentos sigilosos. Adicione uma linha em .gitignore (ex.: /tests_inputs/ ou /samples/).

- Rodando com saída JSON (para integração):
  python3 Auditor-Forense/run_audit.py --input path/to/peça.pdf --process 0000000-00.0000.0.00.0000 --json-output

O que validar localmente
- Que o arquivo de entrada exista e seja .pdf ou .docx
- Que o arquivo não exceda 10 MB (limite de teste)

Checklist para revisão antes do merge
- [ ] Inserir política de tratamento de dados/confidencialidade no repo
- [ ] Confirmar required_inputs no SKILL.md
- [ ] Rever run_audit.py para sanitização mais robusta (ex.: conversão/extração em sandbox)
- [ ] Revisão por advogado sênior e por engenheiro de segurança

Contato
- Responsável pelo conteúdo: tiagoneves.jus@gmail.com

Sugestão: adicionar workflow de CI para lint (ruff/flake8) e testes unitários (pytest).
