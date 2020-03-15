#!/bin/bash

function getOperatorKeystorePath {
    network=${1}
    path="./config/${network}/keystores"
    mkdir -p ${path}
    echo "${path}/operator.icx"
}

function getOperatorKeystorePassword {
    network=${1}
    echo $(cat ./config/${network}/keystores/operator.password.txt)
}

./install.sh

echo "If you haven't already done, send 20 ICX to this address for covering the SCORE deploy fees :"
tbears keyinfo -p $(getOperatorKeystorePassword ${network}) ${keystore}

read -p "Press enter to continue"

./scripts/score/deploy_score.sh -n mainnet -t ICXUSD