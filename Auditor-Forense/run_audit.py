#!/usr/bin/env python3
"""
run_audit.py
Script simples que lê Auditor-Forense/audit.json e imprime um resumo de execução.
Melhorias: validação básica das entradas (extensão e tamanho), parâmetros de linha de comando e aviso de confidencialidade.
Uso: python3 run_audit.py --input path/to/peça.pdf --process 0000000-00.0000.0.00.0000
"""
import argparse
import json
import sys
import re
from pathlib import Path

MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXT = {'.pdf', '.docx'}


def load_config(path: Path):
    try:
        with path.open(encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"AVISO: arquivo de configuração inválido ({path}): {e}")
        return None


def validate_input_file(path: Path):
    try:
        p = path.resolve()
    except Exception:
        p = path
    if not p.exists() or not p.is_file():
        print(f"ERRO: arquivo inexistente ou inválido: {p}")
        return False
    if p.suffix.lower() not in ALLOWED_EXT:
        print(f"ERRO: extensão não permitida: {p.suffix}. Permitidas: {', '.join(sorted(ALLOWED_EXT))}")
        return False
    try:
        size = p.stat().st_size
    except OSError as e:
        print(f"ERRO ao acessar arquivo: {e}")
        return False
    if size > MAX_FILE_SIZE_BYTES:
        print(f"ERRO: arquivo muito grande ({size} bytes). Máx: {MAX_FILE_SIZE_BYTES} bytes")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description='Executa auditoria forense jurídica (teste).')
    parser.add_argument('--input', '-i', required=True, help='Caminho para o documento principal (pdf/docx)')
    parser.add_argument('--process', '-p', required=True, help='Número do processo')
    parser.add_argument('--config', '-c', default='audit.json', help='Arquivo de configuração (padrao: audit.json)')
    parser.add_argument('--quiet', '-q', action='store_true', help='Minimiza saída')
    parser.add_argument('--json-output', action='store_true', help='Imprime resumo em JSON (para integração)')
    args = parser.parse_args()

    config_path = Path(__file__).with_name(args.config)
    cfg = load_config(config_path)
    if cfg is None:
        if not args.quiet:
            print(f"Aviso: arquivo de configuração não encontrado ou inválido: {config_path}. Usando parâmetros mínimos.")
    else:
        if not args.quiet:
            print(f"Carregado config: {cfg.get('name', 'N/A')} v{cfg.get('version', 'N/A')}")

    input_path = Path(args.input)
    if not validate_input_file(input_path):
        print("Validação do arquivo de entrada falhou. Corrija e tente novamente.")
        sys.exit(2)

    # Validação simples do número do processo (evita valores óbvios inválidos)
    # Aceita dígitos, pontos e hífens; veja SKILL.md para formato esperado
    if not re.match(r'^[\d.\-\\/]{5,}$', args.process):
        print("AVISO: formato de número de processo aparentemente inválido. Confirme o valor.")

    # Aviso de confidencialidade
    if not args.quiet:
        print("\n=== AVISO DE CONFIDENCIALIDADE ===")
        print("Documentos processados podem conter dados sensíveis. Assegure autorização e supervisão por advogado habilitado.")

    # Execução de análise (placeholder)
    result = {
        "process": args.process,
        "document": input_path.name,
        "status": "analise_teste_concluida"
    }
    if args.json_output:
        import json as _json
        print(_json.dumps(result, ensure_ascii=False))
    else:
        print("\n=== Auditor Forense - Execução de Teste ===")
        print(f"Processo: {args.process}")
        print(f"Documento: {input_path.name} ({input_path.suffix})")
        print("Resultado: análise de teste concluída (saída exemplificativa).")


if __name__ == '__main__':
    main()
