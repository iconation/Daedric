#!/bin/bash

. ./scripts/utils/utils.sh

function print_usage {
    usage_header ${0}
    usage_option " -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)"
    usage_option " [-s <keystore password>] : The keystore password (optional)"
    usage_footer
    exit 1
}

function process {
    if [[ ("$network" == "") ]]; then
        print_usage
    fi

    price=$(./scripts/bots/coinmarketcap/main.py)
    ./scripts/score/post.sh -n "${network}" -p "${price}" -s "${password}"
}

# Parameters
while getopts "n:s:" option; do
    case "${option}" in
        n)
            network=${OPTARG}
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