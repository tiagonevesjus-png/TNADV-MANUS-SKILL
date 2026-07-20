#!/usr/bin/env python3
"""
run_audit.py
Script simples que lê Auditor-Forense/audit.json e imprime um resumo de execução.
Uso: python3 run_audit.py
"""
import json
from pathlib import Path

def load_config(path: Path):
    with path.open(encoding='utf-8') as f:
        return json.load(f)

def main():
    cfg_path = Path(__file__).with_name('audit.json')
    if not cfg_path.exists():
        print(f"Config file not found: {cfg_path}")
        return
    cfg = load_config(cfg_path)
    print("=== Auditor Forense - Execução de Teste ===")
    print(f"Skill: {cfg.get('name')}")
    print(f"Versão: {cfg.get('version')}")
    print(f"Autor: {cfg.get('author')}")
    print(f"Modo de teste: {cfg.get('test')}")
    # Aqui você integraria a execução real da skill

if __name__ == '__main__':
    main()
