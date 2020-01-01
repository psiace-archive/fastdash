# -*- coding: utf-8 -*-

"""Main module."""

from fastapi import FastAPI
from fastdash.utils import *

app = FastAPI()


@app.get("/")
def fastdash_info():
    ipaddress = get_ipaddress()
    platform = get_platform()
    uptime = get_uptime()
    cpu = get_cpu_usage()
    cores = get_cpus()
    memory = get_mem()
    disk = get_disk()
    diskrw = get_disk_rw()
    loadavg = get_load()
    # Get traffic
    ip = ipaddress["interface"][0]
    traffic = get_traffic(ip)
    users = get_users()
    netstat = get_netstat()

    return {
        "ipaddress": ipaddress,
        "platform": platform,
        "uptime": uptime,
        "cpu": cpu,
        "cores": cores,
        "memory": memory,
        "disk": disk,
        "diskrw": diskrw,
        "loadavg": loadavg,
        "traffic": traffic,
        "users": users,
        "netstat": netstat,
    }
