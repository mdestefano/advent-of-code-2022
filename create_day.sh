#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

mkdir -p $SCRIPT_DIR/$1
touch $SCRIPT_DIR/$1/input.txt
touch $SCRIPT_DIR/$1/solution.py
touch $SCRIPT_DIR/$1/test.txt