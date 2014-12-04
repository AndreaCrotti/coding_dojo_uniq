import sys
import argparse
import unittest


def uniq(inp):
    seen = set()
    for line in inp.splitlines():
        if line not in seen:
            seen.add(line)
            yield line


class TestUniq(unittest.TestCase):
    def test_simple_uniq(self):
        inp = "line\nhello\nline"
        self.assertEqual(list(uniq(inp)), ["line", "hello"])


def parser():
    parser = argparse.ArgumentParser(description='uniq')
    parser.add_argument('input_file', nargs=1)
    parser.add_argument('output_file', nargs='?')

    return parser.parse_args()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        ns = parser()
        with open(ns.input_file[0]) as input:
            result = '\n'.join(uniq(input.read())) + '\n'
            output = open(ns.output_file, 'w') if ns.output_file else sys.stdout
            output.write(result)
