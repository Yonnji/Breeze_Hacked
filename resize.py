#!/usr/bin/env python3
import os


def resize(lines):
    new_lines = []

    for line in lines:
        params = line.split(' ')
        old_size = int(params[0])
        new_size = int(old_size * 1.5)
        params[0:3] = list(map(lambda x: str(int(int(x) * 1.5)), params[0:3]))
        params[3] = params[3].replace(f'{old_size}/', f'{new_size}/')
        new_lines.append(' '.join(params))

    return new_lines


def main():
    dirname = 'src/config'
    for filename in os.listdir(dirname):
        filepath = os.path.join(dirname, filename)

        lines24 = []
        lines48 = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if line.startswith('24 '):
                    lines24.append(line.replace(' x1/', ' 24/').strip('\n'))
                elif line.startswith('48 '):
                    lines48.append(line.replace(' x2/', ' 48/').strip('\n'))

        lines36 = resize(lines24)
        lines72 = resize(lines48)

        with open(filepath, 'w') as f:
            for line in (lines24 + lines36 + lines48 + lines72):
                f.write(line + '\n')


if __name__ == '__main__':
    main()
