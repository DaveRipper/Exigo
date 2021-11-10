import random
from tree import Node, Tree
from color import Color

class Questioner:
    def __init__(self, filename):
        self.questions = Node("root")
        now = self.questions
        now_indent = 0
        previous_indent = 0
        lines = open(f"{filename}.txt", "r").read().splitlines()

        for line in lines:
            previous_indent = now_indent
            now_indent = len(line.split()[0]) + 1

            if now_indent > previous_indent:
                now = now.add(line[now_indent:])
            elif now_indent == previous_indent:
                now = now.parent.add(line[now_indent:])
            else:
                for i in range(previous_indent - now_indent):
                    now = now.parent

                now = now.parent.add(line[now_indent:])

    def start(self):
        self.question(self.questions.children)

    def question(self, candidates):
        if candidates == []:
            return

        for q in random.sample(candidates, random.randint(1, len(candidates))):
            print(f"{Color.BOLD}{'-' * q.depth()} {Color.COLORS[(q.depth() - 1) % len(Color.COLORS)]}{q.data}{Color.END}")

            if input() == "":
                self.question(q.children)