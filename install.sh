#!/bin/bash

function getOperatorKeystorePath {
    network=${1}
    echo "./config/${network}/keystores/operator.icx"
}

function generateOperatorKeystore {
    network=${1}
    echo -e "\n===[${network}]===================================="
    keystore=$(getOperatorKeystorePath ${network})
    # Check if file exists
    if [ -f "$keystore" ]; then
        echo "Operator wallet is already generated for ${network}."
    else
        echo "Generating operator keystore for ${network} ..."
        tbears keystore ${keystore}
    fi
    echo -e "===[/${network}]====================================\n"
}

# Generate keystores
# localhost should be pre-generated

# generateOperatorKeystore "localhost"
generateOperatorKeystore "yeouido"
generateOperatorKeystore "euljiro"
generateOperatorKeystore "mainnet"
