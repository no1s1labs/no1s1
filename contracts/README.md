# no1s1 Smart Contracts

This repository contains the smart contracts for the no1s1 prototype. The different contracts are described below. The newest contract version currently used for the prototype is V2.

<!-- Describe where live contracts are deployed. -->

## no1s1 Contracts V1

The [no1s1App_V1.sol](./contracts/no1s1App_V1.sol) and [no1s1Data_V1.sol](./contracts/no1s1Data_V1.sol) contracts together provided the functionality of the initial protoype. 

They also make use of the OpenZeppelin [SafeMath.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol) contract to protect against overflow.

<!-- Describe functionality -->

## no1s1 Contract WEF

For exhibition at the World Economic Forum 2022, we used a reduced version of the above contracts for simplified demonstration of the protoype: [no1s1WEF.sol](.//contracts/no1s1WEF.sol).

<!-- Describe functionality -->

## no1s1 Contracts V2

<!-- Describe newest contracts -->

## Getting started

### Develop and Test with Local Network (Ganache)

Install [Truffle Suite](https://truffleframework.com/), [node.js](https://nodejs.org/en/) and [Metamask](https://metamask.io/).

Clone this repository and change to the project directory. Install all prerequisites, e.g. the [Openzeppelin Contracts](https://www.openzeppelin.com/contracts) with:

```sh
npm install
```

Launch Ganache-Cli with the following seed to get the correct test accounts:

```sh
ganache-cli -m "spirit supply whale amount human item harsh scare congress discover talent hamster"
```

Alternatively, you can use the Ganache-GUI by changing the develpment port (7545 instead of 8545) in [truffle-config.js](./truffle-config.js).

Make sure the [2_no1s1_migration.js](./migrations/2_no1s1_migration.js) file contains the correct smart contracts you want to deploy. Then compile and migrate the smart contracts:

```sh
truffle compile
truffle migrate --reset --network development
```

To run the unit tests of the smart contracts:

```sh
truffle test
```

Point Metamask to your localhost network and import the needed private keys. You are ready to go!

### Develop and Test with Remix

Instead of using Truffle and Ganache, [Remix IDE](https://remix.ethereum.org/) is a nice way for fast contract testing and development. It automatically provides a GUI to interact with the smart contract functions. Just import the .sol files and compile and deploy to your preffered network.
