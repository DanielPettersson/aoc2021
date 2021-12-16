from __future__ import annotations

from dataclasses import dataclass
from typing import TextIO, Any, Optional, List

from src.common.base_day import BaseDay


@dataclass
class Packet:
    packet_version: int
    packet_type: int
    value: Any
    length: int
    children: List[Packet]


class LiteralPacket(Packet):

    def __init__(self, packet_version: int, input_binary: str):
        self.packet_version = packet_version
        self.packet_type = 4
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


def parse_packet(input_binary: str) -> Optional[Packet]:
    packet_version = int(input_binary[:3], 2)
    packet_type = int(input_binary[3:6], 2)
    packet_data = input_binary[6:]

    if packet_type == 4:
        return LiteralPacket(packet_version, packet_data)
    else:
        return OperatorPacket(packet_version, packet_type, packet_data)


def packet_version_sum(packet: Packet) -> int:
    return packet.packet_version + sum(packet_version_sum(p) for p in packet.children)


class Day16(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        binary = "".join([bin(int(c, 16))[2:].zfill(4) for c in input_file.readline().strip()])
        packet = parse_packet(binary)
        return packet_version_sum(packet)


if __name__ == '__main__':
    Day16().run()
