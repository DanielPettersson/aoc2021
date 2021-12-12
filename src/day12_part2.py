from collections import deque
from dataclasses import dataclass
from pprint import pprint
from typing import TextIO, Any, Optional, Set, Dict, List

from src.common.base_day import BaseDay


class Day12(BaseDay):

    graph: Dict[str, Set[str]] = dict()

    def execute(self, input_file: TextIO) -> Any:
        for line in input_file:
            a, b = line.strip().split("-")
            self.add_to_graph(a, b)

        pprint(self.graph, indent=2)

        paths = self.walk_graph("start", {})

        return len(paths)

    def walk_graph(self, node: str, visited_nodes: Dict[str, int]) -> List[List[str]]:

        if node == "end":
            return [["end"]]

        self.visit_node(node, visited_nodes)

        ret = []
        for target in sorted(self.graph[node]):
            if self.can_visit_node(target, visited_nodes):
                target_ret = self.walk_graph(target, visited_nodes.copy())
                for tr in target_ret:
                    ret.append([node] + tr)
        return ret

    @staticmethod
    def visit_node(node: str, visited_nodes: Dict[str, int]):
        if node.islower() and node != "start":
            if node not in visited_nodes:
                visited_nodes[node] = 0
            visited_nodes[node] += 1

    @staticmethod
    def can_visit_node(node: str, visited_nodes: Dict[str, int]):
        if node == "start":
            return False
        if node not in visited_nodes:
            return True
        else:
            for visits in visited_nodes.values():
                if visits > 1:
                    return False
            return True

    def add_to_graph(self, a: str, b: str):
        if a not in self.graph:
            self.graph[a] = set()
        self.graph[a].add(b)
        if b not in self.graph:
            self.graph[b] = set()
        self.graph[b].add(a)


if __name__ == '__main__':
    Day12().run()
