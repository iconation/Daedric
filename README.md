<p align="center">
  <img 
    src="https://iconation.team/images/very_small.png" 
    width="120px"
    alt="ICONation logo">
</p>

<h1 align="center">Daedric : Price Feed SCORE</h1>

 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

Daedric is a price feed designed to be a component required for a price oracle running on ICON to work. The Daedric SCORE operator can update and share a price associated with a ticker symbol at any time. Once deployed, the Daedric SCORE operator may subscribe its SCORE to a price oracle (such as [Hylian](https://github.com/iconation/Hylian)) in order to take part of the price consensus needed for the oracle to work in a decentralized manner.

## Prerequisites

- **[T-Bears](https://github.com/icon-project/t-bears/)** should be installed
- **T-Bears needs to be launched using the configuration file** provided in this repository :
<pre>
tbears start -c ./config/localhost/tbears_server_config.json
</pre>

- You also need `jq`. Install it with `sudo apt-get install jq`

## Installation

- Run the **`install.sh` script** located in the root folder of the repository;

- It will generate 3 operator wallets : 
  - A first one on the Yeouido network in `./config/yeouido/keystores/operator.icx`
  - A second one on the Euljiro network in `./config/euljiro/keystores/operator.icx`
  - A last one on the Mainnet network in `./config/mainnet/keystores/operator.icx`

- Make sure to send some funds to these wallets before deploying a SCORE (20 ICX should be good enough).

- A wallet for localhost development is already pre-generated.
- If you correctly loaded T-bears using the configuration as described in the prerequisites, `tbears balance hxba2e54b54b695085f31ff1a9b33868b5aea44e33` should return some balance.

## Deploy Daedric SCORE to localhost, testnet or mainnet

- In the root folder of the project, run the following command:
<pre>./scripts/score/deploy_score.sh</pre>

- It should display the following usage:
<pre>
> Usage:
 `-> ./scripts/score/deploy_score.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
 -t <ticker name> : Standardized name for the ticker (such as ICXUSD)
</pre>

- Fill the `-n` option corresponding to the network you want to deploy to: `localhost`, `yeouido`, `euljiro` or `mainnet`.
- Fill the `-t` option with the name of the ticker, such as `ICXUSD`. Note that ticker name needs to be the same than the deployed [Medianizer SCORE](https://github.com/iconation/Medianizer).
- **Example** : 
<pre>$ ./scripts/score/deploy_score.sh -n localhost -t ICXUSD</pre>

## Update an already deployed Daedric to localhost, testnet or mainnet

- In the root folder of the project, run the following command:
<pre>$ ./scripts/score/update_score.sh</pre>

- It should display the following usage:
<pre>
> Usage:
 `-> ./scripts/score/update_score.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
</pre>

- Fill the `-n` option corresponding to the network where your SCORE is deployed to: `localhost`, `yeouido`, `euljiro` or `mainnet`.

- **Example** :
<pre>$ ./scripts/score/update_score.sh -n localhost</pre>


## Post a new price to the feed

- In the root folder of the project, run the following command:

<pre>$ ./scripts/score/post.sh</pre>

- It should display the following usage:
<pre>
> Usage:
 `-> ./scripts/score/post.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
 -p <price value> : Price to be updated
</pre>

- Fill the `-n` option corresponding to the network where your SCORE is deployed to: `localhost`, `yeouido`, `euljiro` or `mainnet`.
- Fill the `-p` option with the price (in loops). Please make sure of the format of the price with the Medianizer SCORE operator. For instance for the `ICXUSD`, the price value needs to be the amount of **loops** for 1 USD.
- **Example** : Given a ICX price of $0.10, 10000000000000000000 loops (10 ICX) are required to have 1 USD. So the request to the price feed should be the following :
<pre>$ ./scripts/score/post.sh -n localhost -p 10000000000000000000</pre>

## Read the values from a Daedric SCORE

- In the root folder of the project, run the following command:

<pre>$ ./scripts/score/peek.sh</pre>

- It should display the following usage:
<pre>
> Usage:
 `-> ./scripts/score/peek.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
</pre>

- Fill the `-n` option corresponding to the network where your SCORE is deployed to: `localhost`, `yeouido`, `euljiro` or `mainnet`.

- **Example** :
<pre>$ ./scripts/score/peek.sh -n localhost</pre>

This command shall return the following result:
<pre>
> Command:
$ tbears call <(python ./scripts/score/dynamic_call/peek.py localhost) -c ./config/localhost/tbears_cli_config.json

> Result:
$ response : {
    "jsonrpc": "2.0",
    "result": "{\"value\": 10000000000000000000, \"timestamp\": 1565044831817071, \"ticker_name\": \"ICXUSD\"}",
    "id": 1
}</pre>
