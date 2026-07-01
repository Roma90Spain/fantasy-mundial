#!/usr/bin/env python3
"""
Script para regenerar APP_VERSION en index.html
Ejecutar cada vez antes de subir a GitHub
"""
import re
import time
import hashlib
import sys

def update_app_version(html_file='index.html'):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Opción 1: Usar timestamp actual
    timestamp = int(time.time())
    
    # Opción 2: Usar hash del contenido (más robusto)
    # Calcula hash del DATA para detectar cambios reales
    data_match = re.search(r'let DATA = (\{.*?\});\n', content, re.DOTALL)
    if data_match:
        data_str = data_match.group(1)
        content_hash = int(hashlib.md5(data_str.encode()).hexdigest()[:8], 16)
    else:
        content_hash = timestamp
    
    # Reemplaza la versión anterior (o añade si no existe)
    old_pattern = r'const APP_VERSION = \d+;'
    new_version = f'const APP_VERSION = {content_hash};'
    
    if re.search(old_pattern, content):
        new_content = re.sub(old_pattern, new_version, content)
    else:
        # Inserta después del primer <script>
        insert_pos = content.find('<script>') + 8
        new_content = content[:insert_pos] + f'\n{new_version}\n' + content[insert_pos:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ APP_VERSION actualizado a {content_hash}")
    return content_hash

if __name__ == '__main__':
    html_file = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
    update_app_version(html_file)
