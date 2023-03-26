import subprocess
import os


def count_lines():
    """
    prints file lengths statistic of git repo
    """
    fname = 'git_list.txt'  # used for creating temp file, deleted after execution
    total = 0
    files = 0
    ext = {}
    subprocess.run(f"git ls-files > {fname}", shell=True)
    with open(fname, 'rb') as flist:
        print(">" * 45)
        print("LINES BY NAME: ")
        print("<" * 45)
        for i, name in enumerate(flist):
            n = name.decode("utf-8").strip()
            with open(n, 'rb') as f:
                x = len(f.readlines())
                total += x
                files += 1
                try:
                    ext[os.path.splitext(n)[1]] += x
                except KeyError:
                    ext[os.path.splitext(n)[1]] = x
                n = n if len(n) < 35 else '...' + n[abs(35 - len(n)):]
                s = '{:^4}: '.format(i + 1) + n + ' ' * (2 - len(n) % 2) + ' _' * (20 - len(n) // 2) + ": " + str(x)
                print(s)
    os.remove(fname)
    print(">" * 45)
    print("LINES BY EXTENSION: ")
    print("<" * 45)
    for k in ext.keys():
        print(k + ' ' * (2 - len(k) % 2) + ' _' * (23 - len(k) // 2) + ": " + str(ext[k]))
    print(">" * 45)
    print(f"FILES:       {str(files)}\nTOTAL LINES: {str(total)}")
    print("<" * 45)


if __name__ == "__main__":
    count_lines()

