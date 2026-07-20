#!/usr/bin/env python3
"""
generate_report.py
Função auxiliar para gerar um relatório simples a partir de um dicionário.
"""
from pathlib import Path
import json

def generate_report(data: dict, out_path: Path):
    lines = []
    lines.append('Relatório de Auditoria Forense')
    lines.append('')
    for k, v in data.items():
        lines.append(f"{k}: {v}")
    out_path.write_text('\n'.join(lines), encoding='utf-8')

if __name__ == '__main__':
    sample = {"skill": "auditor-forense", "summary": "Execução de teste"}
    generate_report(sample, Path(__file__).with_suffix('.report.txt'))
    print('Relatório gerado:', Path(__file__).with_suffix('.report.txt'))
