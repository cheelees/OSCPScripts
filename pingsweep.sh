#!/bin/bash

for ip in {1..254};
do
	ping -c 1 10.11.1.$ip;
done

