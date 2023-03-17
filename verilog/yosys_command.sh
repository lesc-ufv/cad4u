#!/bin/bash
#set -x
TOP=$1
CODE=$2
yosys -p "prep -top $TOP; write_json output.json" /content/$CODE 