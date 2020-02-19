import argparse


def filename_to_str(fname, slice=None):
    with open(fname) as f:
        if not slice:
            return f.read()
        return '\n'.join(f.read().split('\n')[slice])

def insert_str_at_pos(str1, str2, pos, line=None):
    if not line:
        return str1[pos:] + str2 + str1[:pos]
    k = line.split('\n')
    k[line] = insert_str_at_pos(k[line], str2, pos)
    return '\n'.join(k)

def replace_str(str1, substr1, str2):
    return str2.join(str1.split(substr1))


def replace_pos(str1, str2, slice):
    k = str1.split('\n')
    return '\n'.join(k[:slice[0]] + [str2] +  k[slice[1]:])

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', help='insert, replace or delete')
    parser.add_argument('--file1', help='Main file')
    parser.add_argument('--file2', help='File to insert')
    parser.add_argument('--string_i', help='String to insert')
    parser.add_argument('--string_d', help='String to delete')
    parser.add_argument('--pos1', help='First position')
    parser.add_argument('--pos2', help='Second position')
    parser.add_argument('--line1', help='First line')
    parser.add_argument('--line2', help='Second line')
    
    parser.add_argument('--itrajext', help='input traj ext')

    i

    parser.parse_args()

if __name__ == "__main__":
    main()