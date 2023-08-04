#!/usr/bin/env python3

from path import Path


def main():
    try:
        Path.makedirs('teste make diretorio')
    except FileExistsError as e:
        print(e)
    Path.touch('teste/caminho')
    f = Path('teste/caminho')
    f.write_lines(['bruno', 'shiroma', 'mini', 'piscina', '42'])
    print(f.read_text())


if __name__ == '__main__':
    main()