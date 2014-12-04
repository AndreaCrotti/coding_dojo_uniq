import sys
import argparse
import unittest


def uniq(lines, with_count=False, only_repeated=False):
    counter = 1
    last = lines[0]

    for line in lines[1:] + ['\n']:
        if line != last:
            if with_count:
                result = "{} {}".format(counter, last)
            else:
                result = last

            if (not only_repeated) or counter > 1:
                yield result
            counter = 1
        else:
            counter += 1

        last = line


class TestUniq(unittest.TestCase):
    def test_simple_uniq(self):
        inp, out = ["line", "line", "test", "line"], ["line", "test", "line"]
        self.assertEqual(list(uniq(inp)), out)

    def test_counting_occurrences(self):
        inp = ["line", "line", "hello"]
        desired = ["2 line", "1 hello"]
        self.assertEqual(list(uniq(inp, with_count=True)), desired)

    def test_only_repeated(self):
        inp = ["line", "line", "hello"]
        desired = ["line"]
        self.assertEqual(list(uniq(inp, only_repeated=True)), desired)


def parser():
    parser = argparse.ArgumentParser(description='See man uniq for more info')
    parser.add_argument('input_file', nargs=1)
    parser.add_argument('output_file', nargs='?')
    parser.add_argument('-c', dest='counter', action='store_true')
    parser.add_argument('-d', dest='only_repeated', action='store_true')

    return parser.parse_args()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        ns = parser()
        with open(ns.input_file[0]) as input:
            lines = input.readlines()
            result = ''.join(uniq(lines, with_count=ns.counter,
                                  only_repeated=ns.only_repeated))

            output = open(ns.output_file, 'w') if ns.output_file else sys.stdout
            output.write(result)
