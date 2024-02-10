#!/bin/bash

# Usage:
# ./run_tests.sh functional pour exécuter les tests fonctionnels
# ./run_tests.sh load pour exécuter les tests de charge

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [functional|load]"
    exit 1
fi

mode=$1

if [ "$mode" = "functional" ]; then
    echo "Exécution des tests fonctionnels..."
    python -m unittest discover -s ./FonctionnalTest -p 'test_*.py'

elif [ "$mode" = "load" ]; then
    echo "Exécution des tests de charge..."
    python LoadTesting/main.py

else
    echo "Mode non reconnu: $mode"
    echo "Usage: $0 [functional|load]"
    exit 2
fi
