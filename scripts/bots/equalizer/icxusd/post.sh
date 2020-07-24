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

    # Calculate the arithmetic mean value of all the available sources
    price=$(./scripts/bots/equalizer/icxusd/main.py           \
            $(./scripts/bots/binance/icxusd/main.py)          \
            $(./scripts/bots/velic/icxusd/main.py)            \
            $(./scripts/bots/coingecko/icxusd/main.py)        \
    )

    if [ $price -ne 0 ] ; then
        ./scripts/score/post.sh -n "${network}" -p "${price}" -s "${password}"
    fi
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