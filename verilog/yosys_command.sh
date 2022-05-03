#!/bin/bash
TOP=$1
yosys -p "prep $TOP; write_json output.json" /content/code.v 