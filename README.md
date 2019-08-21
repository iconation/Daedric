<p align="center">
  <img 
    src="https://iconation.team/images/very_small.png" 
    width="120px"
    alt="ICONation logo">
</p>

<h1 align="center">Daedric : Price Feed SCORE</h1>

 [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

**Daedric** is a price feed designed to be a component required for a price oracle running on ICON to work. The Daedric SCORE operator can update and share a price associated with a ticker symbol at any time. Once deployed, the Daedric SCORE operator may subscribe its SCORE to a price oracle (such as [Hylian](https://github.com/iconation/Hylian)) in order to take part of the price consensus needed for the oracle to work in a decentralized manner.

## Table of Contents

  * [Quick start](https://github.com/iconation/Daedric#quick-start)
  * [Deploy Daedric SCORE to localhost, testnet or mainnet](https://github.com/iconation/Daedric#deploy-daedric-score-to-localhost-testnet-or-mainnet)
  * [Update an already deployed Daedric to localhost, testnet or mainnet](https://github.com/iconation/Daedric#update-an-already-deployed-daedric-to-localhost-testnet-or-mainnet)
  * [Post a new price to the feed](https://github.com/iconation/Daedric#post-a-new-price-to-the-feed)
  * [Read the values from a Daedric SCORE](https://github.com/iconation/Daedric#read-the-values-from-a-daedric-score)
  * [Update the price feed using a built-in price bot](https://github.com/iconation/Daedric#update-the-price-feed-using-a-built-in-price-bot)

## Quick Start

Here is a checklist you will need to follow in order to deploy your first Daedric SCORE to the Yeouido testnet:

  * Install prerequisites:
    * `python3 -m venv ./venv && source ./venv/bin/activate`
    * `pip install tbears`
    * `sudo apt install jq`
  * Clone the Daedric repository:
    * `git clone https://github.com/iconation/Daedric.git && cd Daedric`
  * Start tbears using the `start_tbears.sh` script located at the root folder of the Daedric repository
    * `./start_tbears.sh`
  * Install the operator wallets:
    * `./install.sh`
    * It will generate 3 operator wallets : 
      * A first one on the Yeouido network in `./config/yeouido/keystores/operator.icx`
      * A second one on the Euljiro network in `./config/euljiro/keystores/operator.icx`
      * A last one on the Mainnet network in `./config/mainnet/keystores/operator.icx`
    * Input a password for each network
  * Send few ICX (20 ICX should be enough) to the Yeouido wallet (the newly generated address is displayed after executing the `install.sh` script)
    * If you don't have some testnet ICX, use the [faucet](http://icon-faucet.ibriz.ai/) or contact [@Spl3en](https://t.me/Spl3en)
  * Deploy your SCORE to the testnet:
    * `./scripts/score/deploy_score.sh -n yeouido -t ICXUSD`
  * Test your Daedric SCORE by manually calling the following script:
    * `./scripts/bots/equalizer/icxusd/post.sh -n yeouido`
  * Check the value of your feed using the ICON Yeouido tracker : 
    * https://bicon.tracker.solidwallet.io/contract/<your_contract_address>
  * Install your price bot (Marvin):
    * Follow the instructions in the [Marvin repository](https://github.com/rhizomeicx/marvin/blob/master/README.md)
  * If everything is working as intended, please share your SCORE address with [@Spl3en](https://t.me/Spl3en), so your SCORE can be added to [Hylian](https://github.com/iconation/Hylian) (price oracle).

## Deploy Daedric SCORE to localhost, testnet or mainnet

- In the root folder of the project, run the following command:
<pre>./scripts/score/deploy_score.sh</pre>

- It should display the following usage:
```
> Usage:
 `-> ./scripts/score/deploy_score.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
 -t <ticker name> : Standardized name for the ticker (such as ICXUSD)
```

- Fill the `-n` option corresponding to the network you want to deploy to: `localhost`, `yeouido`, `euljiro` or `mainnet`.
- Fill the `-t` option with the name of the ticker, such as `ICXUSD`. Note that ticker name needs to be the same than the deployed [Medianizer SCORE](https://github.com/iconation/Medianizer).
- **Example** : 
<pre>$ ./scripts/score/deploy_score.sh -n localhost -t ICXUSD</pre>

## Update an already deployed Daedric to localhost, testnet or mainnet

- If you modified the Daedric SCORE source code, you may need to update it.

- In the root folder of the project, run the following command:
<pre>$ ./scripts/score/update_score.sh</pre>

- It should display the following usage:
```
> Usage:
 `-> ./scripts/score/update_score.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
```

- Fill the `-n` option corresponding to the network where your SCORE is deployed to: `localhost`, `yeouido`, `euljiro` or `mainnet`.

- **Example** :
<pre>$ ./scripts/score/update_score.sh -n localhost</pre>


## Post a new price to the feed

- In the root folder of the project, run the following command:

<pre>$ ./scripts/score/post.sh</pre>

- It should display the following usage:
```
> Usage:
 `-> ./scripts/score/post.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
 -p <price value> : Price to be updated
```

- Fill the `-n` option corresponding to the network where your SCORE is deployed to: `localhost`, `yeouido`, `euljiro` or `mainnet`.
- Fill the `-p` option with the price (in loops). Please make sure of the format of the price with the Medianizer SCORE operator. For instance for the `ICXUSD`, the price value needs to be the amount of **loops** for 1 USD.
- **Example** : Given a ICX price of $0.10, 10000000000000000000 loops (10 ICX) are required to have 1 USD. So the request to the price feed should be the following :
<pre>$ ./scripts/score/post.sh -n localhost -p 10000000000000000000</pre>

## Read the values from a Daedric SCORE

- In the root folder of the project, run the following command:

<pre>$ ./scripts/score/peek.sh</pre>

- It should display the following usage:
```
> Usage:
 `-> ./scripts/score/peek.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
```

- Fill the `-n` option corresponding to the network where your SCORE is deployed to: `localhost`, `yeouido`, `euljiro` or `mainnet`.

- **Example** :
<pre>$ ./scripts/score/peek.sh -n localhost</pre>

This command shall return the following result:
```
> Command:
$ tbears call <(python ./scripts/score/dynamic_call/peek.py localhost) -c ./config/localhost/tbears_cli_config.json

> Result:
$ response : {
    "jsonrpc": "2.0",
    "result": "{\"value\": 10000000000000000000, \"timestamp\": 1565044831817071, \"ticker_name\": \"ICXUSD\"}",
    "id": 1
}
```

## Update the price feed using a built-in price bot

Daedric is released with multiple built-in ways to retrieve prices.
The Daedric operator is encouraged to build its own price bot in order to avoid a situation where all price feed operators fail to retrieve a price from the same source.
In the meantime, using a built-in one is fine too.

The price bots are located in [./scripts/bots](./scripts/bots).
They all work the same way, for example the Binance one:

<pre>
./scripts/bots/binance/icxusd/post.sh
</pre>

```
> Usage:
 `-> ./scripts/bots/binance/icxusd/post.sh [options]

> Options:
 -n <network> : Network to use (localhost, yeouido, euljiro or mainnet)
 [-s <keystore password>] : The keystore password (optional)
```

You may call this script regularly (using a cron job for exemple) with the `-n` and the `-s` switches filled accordingly.
Make sure the cron job is launched from the root directory of Daedric, otherwise the bot won't work.

**Example** using a cron job that launches the script every hour:

```
0 * * * * cd ~/Daedric/ && ./scripts/bots/binance/icxusd/post.sh -n mainnet -s mysecretpassword
```

Alternatively, you can fill the keystore password in the configuration file (`config/mainnet/tbears_cli_config.json`).
