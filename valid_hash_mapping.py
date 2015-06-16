# coding: utf-8

import random
import libmc
import uuid


mc_nodes = [
    "localhost:21211",
    "localhost:21212",
    "localhost:21213",
    "localhost:21214",
    "localhost:21215",
    "localhost:21216",
    "localhost:21217",
    "localhost:21218",
    "localhost:21219",
    "localhost:21220",
    "localhost:21221",
    "localhost:21222",
    "localhost:21223",
    "localhost:21224",
    "localhost:21225",
    "localhost:21226",
    "localhost:21227",
    "localhost:21228",
    "localhost:21229",
    "localhost:21230",
    "localhost:11211",
]


def set_and_valid(mc1, mc2):
    key = "valid:%s" % uuid.uuid4()
    target_node = mc1.get_host_by_key(key)
    sec_val = str(random.random())
    assert mc1.set(key, sec_val), "fail to set %s %s to %s" % (key, sec_val, target_node)
    assert mc2.get(key) == sec_val
    mc1.delete(key)
    return target_node


def main():
    mc1 = libmc.Client(["localhost:19102"])
    mc2 = libmc.Client(mc_nodes)
    visited_nodes = set()
    for i in range(10000):
        set_and_valid(mc1, mc2)
        visited_nodes.add(set_and_valid(mc2, mc1))
    assert visited_nodes == set(mc_nodes)


if __name__ == '__main__':
    main()
