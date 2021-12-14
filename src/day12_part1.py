from pprint import pprint
from pprint import pprint
from typing import TextIO, Any, Set, Dict, List

from src.common.base_day import BaseDay


class Day12(BaseDay):
    graph: Dict[str, Set[str]] = dict()

    def execute(self, input_file: TextIO) -> Any:
        for line in input_file:
            a, b = line.strip().split("-")
            self.add_to_graph(a, b)

        pprint(self.graph, indent=2)

        paths = self.walk_graph("start", set())

        pprint(paths, indent=2)

        return len(paths)

    def walk_graph(self, node: str, visited_nodes: Set[str]) -> List[List[str]]:

        if node == "end":
            return [["end"]]

        if node.islower():
            visited_nodes.add(node)

        ret = []
        for target in self.graph[node]:
            if target not in visited_nodes:
                target_ret = self.walk_graph(target, visited_nodes.copy())
                for tr in target_ret:
                    ret.append([node] + tr)
        return ret

    def add_to_graph(self, a: str, b: str):
        if a not in self.graph:
            self.graph[a] = set()
        self.graph[a].add(b)
        if b not in self.graph:
            self.graph[b] = set()
        self.graph[b].add(a)


if __name__ == '__main__':
    Day12().run()
