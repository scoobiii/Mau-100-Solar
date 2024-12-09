// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MauathonContract {
    address public prefeitura;
    address public mexEnergia;
    uint public totalPayments;
    uint public totalReceived;

    constructor(address _prefeitura, address _mexEnergia, uint _totalPayments) {
        prefeitura = _prefeitura;
        mexEnergia = _mexEnergia;
        totalPayments = _totalPayments;
        totalReceived = 0;
    }

    function makePayment() public payable {
        require(msg.sender == prefeitura, "Only Prefeitura can make payments");
        require(totalReceived < totalPayments, "All payments have been made");
        totalReceived += msg.value;
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function withdraw() public {
        require(msg.sender == mexEnergia, "Only MEx Energia can withdraw");
        payable(mexEnergia).transfer(address(this).balance);
    }
}