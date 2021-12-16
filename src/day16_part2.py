from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import IntEnum
from functools import reduce
from typing import TextIO, Any, Optional, List

from src.common.base_day import BaseDay


class PacketType(IntEnum):
    sum = 0
    product = 1
    minimum = 2
    maximum = 3
    literal = 4
    greater = 5
    less = 6
    equal = 7


@dataclass
class Packet(ABC):
    packet_version: int
    packet_type: PacketType
    value: Optional[int]
    length: int
    children: List[Packet]

    @abstractmethod
    def apply(self) -> int:
        pass


class LiteralPacket(Packet):

    def __init__(self, packet_version: int, input_binary: str):
        self.packet_version = packet_version
        self.packet_type = PacketType.literal
        self.children = []

        count = 0
        nums = ""
        while True:
            num_str = input_binary[count * 5: count * 5 + 5]
            keep_reading = num_str[0] == "1"
            nums += num_str[1:]
            count += 1
            if not keep_reading:
                break

        value = int(nums, 2)
        length = count * 5 + 6
        super().__init__(packet_version, 4, value, length, [])

    def apply(self) -> int:
        return self.value


class OperatorPacket(Packet):

    def __init__(self, packet_version: int, packet_type: int, input_binary: str):

        length_type = input_binary[0]
        max_bits = None
        max_children = None
        if length_type == "0":
            max_bits = int(input_binary[1:16], 2)
            child_start = 16
            prefix_length = 6 + 1 + 15
        elif length_type == "1":
            max_children = int(input_binary[1:12], 2)
            child_start = 12
            prefix_length = 6 + 1 + 11
        else:
            raise ValueError(f"Unknown length type: {length_type}")

        children = []
        while True:
            child_packet = parse_packet(input_binary[child_start:])
            child_start += child_packet.length
            children.append(child_packet)

            num_children = len(children)
            length_of_children = sum(c.length for c in children)
            if max_children is not None and num_children == max_children:
                break
            if max_bits is not None and length_of_children == max_bits:
                break

        length = sum(c.length for c in children) + prefix_length

        super().__init__(packet_version, packet_type, None, length, children)

    def apply(self) -> int:
        applied_children = [c.apply() for c in self.children]
        if self.packet_type == PacketType.sum:
            return sum(applied_children)
        elif self.packet_type == PacketType.product:
            return reduce(lambda a, b: a * b, applied_children)
        elif self.packet_type == PacketType.minimum:
            return min(applied_children)
        elif self.packet_type == PacketType.maximum:
            return max(applied_children)
        elif self.packet_type == PacketType.greater:
            if len(applied_children) != 2:
                raise ValueError(f"'Greater than' packets should only have two children, not {len(applied_children)}")
            return 1 if applied_children[0] > applied_children[1] else 0
        elif self.packet_type == PacketType.less:
            if len(applied_children) != 2:
                raise ValueError(f"'Less than' packets should only have two children, not {len(applied_children)}")
            return 1 if applied_children[0] < applied_children[1] else 0
        elif self.packet_type == PacketType.equal:
            if len(applied_children) != 2:
                raise ValueError(f"'Equals' packets should only have two children, not {len(applied_children)}")
            return 1 if applied_children[0] == applied_children[1] else 0
        else:
            raise ValueError(f"Unknown packet type: {self.packet_type}")


def parse_packet(input_binary: str) -> Optional[Packet]:
    packet_version = int(input_binary[:3], 2)
    packet_type = int(input_binary[3:6], 2)
    packet_data = input_binary[6:]

    if packet_type == 4:
        return LiteralPacket(packet_version, packet_data)
    else:
        return OperatorPacket(packet_version, packet_type, packet_data)


class Day16(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        binary = "".join([bin(int(c, 16))[2:].zfill(4) for c in input_file.readline().strip()])
        packet = parse_packet(binary)
        return packet.apply()


if __name__ == '__main__':
    Day16().run()
