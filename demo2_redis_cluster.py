# coding:utf-8
from rediscluster import StrictRedisCluster


def demo():
    startup_nodes = [
        {"ip": "119.3.13.110", "port": 7000},
        {"ip": "119.3.13.110", "port": 7001},
        {"ip": "119.3.13.110", "port": 7002}
    ]
    src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    src.set("name", "li")
