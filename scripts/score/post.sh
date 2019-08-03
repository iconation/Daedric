#!/bin/bash

. ./scripts/utils/utils.sh

function print_usage {
    usage_header ${0}
    usage_option " -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)"
    usage_option " -p <price value> : Price to be updated"
    usage_footer
    exit 1
}

function process {
    if [[ ("$network" == "") || ("$price" == "") ]]; then
        print_usage
    fi

    command="tbears sendtx <(python ./scripts/score/dynamic_call/post.py ${network} ${price}) 
            -c ./config/${network}/tbears_cli_config.json"

    txresult=$(./scripts/icon/txresult.sh -n "${network}" -c "${command}")
    echo -e "${txresult}"
}

# Parameters
while getopts "n:p:" option; do
    case "${option}" in
        n)
            network=${OPTARG}
            ;;
        p)
            price=${OPTARG}
            ;;
        *)
            print_usage 
            ;;
    esac 
done
shift $((OPTIND-1))

process