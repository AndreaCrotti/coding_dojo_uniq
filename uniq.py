import sys
import argparse
import unittest

from collections import Counter


def count(inp):
    pass


def uniq(inp, with_count=False):
    counter = 1
    last = None

    for line in inp.splitlines() + ['\n']:
        if last is None:
            last = line
            continue

        if line != last:
            if with_count:
                result = "{} {}".format(counter, last)
            else:
                result = last

            yield result
            counter = 1
        else:
            counter += 1

        last = line


class TestUniq(unittest.TestCase):
    def test_simple_uniq(self):
        inp, out = "line\nline\ntest\nline", ["line", "test", "line"]
        self.assertEqual(list(uniq(inp)), out)

    def test_counting_occurrences(self):
        inp = "line\nline\nhello"
        desired = ["2 line", "1 hello"]
        self.assertEqual(list(uniq(inp, with_count=True)), desired)


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







