#Use this to automatically set up a work directory for a new lab
#arg 1: the module number
#arg 2: the number of assignments in the lab

if [ "$#" -lt 2 ]; then
    echo "Error: This script requires at least 2 arguments."
    echo "Usage: $0 <module_number> <number_of_assignments>"
    exit 1
fi

header="# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 5 Assignment 1"

mod_num=$1
num_assignments=$2

mkdir m$1
cd m$1

for ((i=1; i <= num_assignments; i++)); do
    header=$(echo "$header" | sed -E "s/(Module )[0-9]+/\1$mod_num/; s/(Assignment )[0-9]+$/\1$i/")
    echo "$header" >> M$1A$i.py
done