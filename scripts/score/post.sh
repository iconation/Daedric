#!/bin/bash

. ./scripts/utils/utils.sh

function print_usage {
    usage_header ${0}
    usage_option " -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)"
    usage_option " -p <price value> : Price to be updated"
    usage_option " [-s <keystore password>] : The keystore password (optional)"
    usage_footer
    exit 1
}

function process {
    if [[ ("$network" == "") || ("$price" == "") ]]; then
        print_usage
    fi

    command="tbears sendtx <(python ./scripts/score/dynamic_call/post.py ${network} ${price}) 
            -c ./config/${network}/tbears_cli_config.json"
    
    if [[ ("$password" != "") ]]; then
        command="$(echo ${command}) -p ${password}"
    fi

    txresult=$(./scripts/icon/txresult.sh -n "${network}" -c "${command}")
    echo -e "${txresult}"
}

# Parameters
while getopts "n:p:s:" option; do
    case "${option}" in
        n)
            network=${OPTARG}
            ;;
        p)
            price=${OPTARG}
            ;;
        s)
            password=${OPTARG}
            ;;
        *)
            print_usage 
            ;;
    esac 
done
shift $((OPTIND-1))

process