#!/bin/bash

function getOperatorKeystorePath {
    network=${1}
    path="./config/${network}/keystores"
    mkdir -p ${path}
    echo "${path}/operator.icx"
}

function generateOperatorKeystore {
    network=${1}
    echo -e "\n===[${network}]===================================="
    keystore=$(getOperatorKeystorePath ${network})
    password=$(< /dev/urandom tr -dc A-Z-a-z-0-9_.+*/= | head -c32)
    echo -ne "${password}" > ./config/${network}/keystores/operator.password.txt
    # Check if file exists
    if [ -f "$keystore" ]; then
        echo "Operator wallet is already generated for ${network}."
    else
        echo "Generating operator keystore for ${network} ..."
        tbears keystore -p $(cat ./config/${network}/keystores/operator.password.txt) ${keystore}
        echo "New address generated :"
        tbears keyinfo -p $(cat ./config/${network}/keystores/operator.password.txt) ${keystore}
    fi
    echo -e "===[/${network}]====================================\n"
}

# Generate keystores
# localhost should be pre-generated

# generateOperatorKeystore "localhost"
generateOperatorKeystore "yeouido"
# Euljiro shouldn't be needed
#generateOperatorKeystore "euljiro"
generateOperatorKeystore "mainnet"