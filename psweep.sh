#!/bin/bash
for x in $(seq 1 255)
do
    ip=10.2.2.$x
    ping -c 1 -w 1 $ip | grep "bytes from" | cut -d ":" -f 1 | cut -d " " -f 4 &
done

