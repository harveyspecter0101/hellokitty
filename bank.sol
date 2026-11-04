pragma solidity ^0.8.0;

contract Bank{

    string public name;
    uint public acc_no;
    uint public balance;

    function setDetails(string memory n,uint acc) public {
        name = n;
        acc_no = acc;
    }

    function getDetails() public view returns(string memory,uint,uint) {
        return (name,acc_no,balance);
    }

    function deposit(uint amount) public {
        balance =  balance + amount;
    }

    function withdraw(uint amount) public {
        require(amount <= balance,"Insufficient Balance");
        balance = balance - amount;
    }

    function showBalance() public view returns(uint) {
        return balance;
    }
}