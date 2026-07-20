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
from pathlib import Path

MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXT = {'.pdf', '.docx'}


def load_config(path: Path):
    with path.open(encoding='utf-8') as f:
        return json.load(f)


def validate_input_file(path: Path):
    if not path.exists():
        print(f"ERRO: arquivo não encontrado: {path}")
        return False
    if path.suffix.lower() not in ALLOWED_EXT:
        print(f"ERRO: extensão não permitida: {path.suffix}. Permitidas: {', '.join(ALLOWED_EXT)}")
        return False
    size = path.stat().st_size
    if size > MAX_FILE_SIZE_BYTES:
        print(f"ERRO: arquivo muito grande ({size} bytes). Máx: {MAX_FILE_SIZE_BYTES} bytes")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description='Executa auditoria forense jurídica (teste).')
    parser.add_argument('--input', '-i', required=True, help='Caminho para o documento principal (pdf/docx)')
    parser.add_argument('--process', '-p', required=True, help='Número do processo')
    parser.add_argument('--config', '-c', default='audit.json', help='Arquivo de configuração (padrao: audit.json)')
    args = parser.parse_args()

    config_path = Path(__file__).with_name(args.config)
    if not config_path.exists():
        print(f"Aviso: arquivo de configuração não encontrado: {config_path}. Usando parâmetros mínimos.")
    else:
        cfg = load_config(config_path)
        print(f"Carregado config: {cfg.get('name', 'N/A')} v{cfg.get('version', 'N/A')}")

    input_path = Path(args.input)
    if not validate_input_file(input_path):
        print("Validação do arquivo de entrada falhou. Corrija e tente novamente.")
        sys.exit(2)

    # Aviso de confidencialidade
    print("\n=== AVISO DE CONFIDENCIALIDADE ===")
    print("Documentos processados podem conter dados sensíveis. Assegure autorização e supervisão por advogado habilitado.")

    # Execução de análise (placeholder)
    print("\n=== Auditor Forense - Execução de Teste ===")
    print(f"Processo: {args.process}")
    print(f"Documento: {input_path.name} ({input_path.suffix})")
    print("Resultado: análise de teste concluída (saída exemplificativa).")


if __name__ == '__main__':
    main()
