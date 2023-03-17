#!/bin/bash
set -x
TOP=$1
CODE=$2
yosys -p "prep $TOP; write_json output.json" /content/$CODE 