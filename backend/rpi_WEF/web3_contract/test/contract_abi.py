abi = """[ {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "string",
          "name": "userName",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "confirmationCode",
          "type": "uint256"
        }
      ],
      "name": "newUserRegistered",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "batterystateofcharge",
          "type": "uint256"
        }
      ],
      "name": "no1s1update",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "bool",
          "name": "userActionConfirmed",
          "type": "bool"
        }
      ],
      "name": "userAction",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "theuuid",
          "type": "uint256"
        }
      ],
      "name": "whatuuid",
      "type": "event"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "logs",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "batteryoperatingtemp",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "batterycurrent",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "batteryvoltage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "batterystateofcharge",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "batterychargecycle",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "batterycapacity",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "pvvoltage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "pvcurrent",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "pvchargestate",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "time",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "name": "partners",
      "outputs": [
        {
          "internalType": "string",
          "name": "companyname",
          "type": "string"
        },
        {
          "internalType": "address payable",
          "name": "companyaccount",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "partnertype",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "workload",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "workprice",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "name": "usersid",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "uuid",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "timereg",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "ccode",
          "type": "uint256"
        },
        {
          "internalType": "address payable",
          "name": "account",
          "type": "address"
        },
        {
          "internalType": "int256",
          "name": "expectedduration",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "payamount",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "haveaccount",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "isidentified",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "ispaid",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "name": "usersusage",
      "outputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "actualduration",
          "type": "uint256"
        },
        {
          "internalType": "int256",
          "name": "paychangeamount",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "timeex",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "grantedentrance",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "startedmeditation",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "serviceclosed",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "paychanged",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "actualpayment",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_Btemp",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_Bcurrent",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_Bvoltage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_BSOC",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_BCS",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_Bcapacity",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_Pvoltage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_Pcurrent",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_Pchargestate",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_time",
          "type": "uint256"
        }
      ],
      "name": "broadcastData",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "string",
          "name": "_username",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "_cCode",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_time",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_uuid",
          "type": "uint256"
        }
      ],
      "name": "initNewUser",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "checkStatus",
      "outputs": [
        {
          "internalType": "int256",
          "name": "c_allowtime",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "estimated_cost",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "update_time",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "address payable",
          "name": "_fundingAddress",
          "type": "address"
        },
        {
          "internalType": "address payable",
          "name": "_defaultAddress",
          "type": "address"
        }
      ],
      "name": "setUserAccounts",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "string",
          "name": "_partnername",
          "type": "string"
        },
        {
          "internalType": "address payable",
          "name": "_partnerAddress",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "_companyname",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_partnertype",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "_workload",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_workprice",
          "type": "uint256"
        }
      ],
      "name": "setPartner",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "whatismyacc",
      "outputs": [
        {
          "internalType": "address payable",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "address payable",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "whatismybalance",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "whatisuseruuid",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "whatisuseruuid2",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "int256",
          "name": "_selectedDuration",
          "type": "int256"
        },
        {
          "internalType": "string",
          "name": "_username",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "_selectedCost",
          "type": "uint256"
        }
      ],
      "name": "userPay",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "toContract",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "bool",
          "name": "_pressuredetected",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "_dooropened",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "_motiondetected",
          "type": "bool"
        },
        {
          "internalType": "string",
          "name": "_username",
          "type": "string"
        }
      ],
      "name": "userActive",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "bool",
          "name": "_motiondetected",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "_dooropened",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "_handletriggered",
          "type": "bool"
        },
        {
          "internalType": "string",
          "name": "_username",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "_actualduration",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_timeex",
          "type": "uint256"
        }
      ],
      "name": "serviceClose",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    } ]"""