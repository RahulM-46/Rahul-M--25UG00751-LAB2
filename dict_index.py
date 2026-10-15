class Node:
    def __init__(self, line):
        self.line = line
        self.next = None


class LineQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, line):
        if self.tail is not None and self.tail.line == line:
            return
        node = Node(line)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def text(self):
        result = ""
        cur = self.head
        while cur is not None:
            if result != "":
                result = result + ", "
            result = result + str(cur.line)
            cur = cur.next
        return result


def get_words(line):
    for sep in ".,:;":
        line = line.replace(sep, " ")
    return line.split()


def build(filename):
    index = {}
    f = open(filename)
    num = 0
    for line in f:
        num = num + 1
        for word in get_words(line):
            if word not in index:
                index[word] = LineQueue()
            index[word].add(num)
    f.close()
    return index


def search(index, word):
    if word in index:
        return index[word]
    return None


def write(index, outname):
    out = open(outname, "w")
    for word in sorted(index):
        out.write(word + ": " + index[word].text() + "\n")
    out.close()


if __name__ == "__main__":
    infile = input("Input file name: ")
    outfile = input("Output file name: ")
    write(build(infile), outfile)
