#!/bin/bash

INPUT=$1
OUTPUT=$2

dot -Tpng $INPUT -o $OUTPUT
