// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract MiniToken {
string public name = "MiniToken";
string public symbol = "MINI";
mapping(address => uint) public balance;
event Minted(address to, uint amount);
event Transferred(address from, address to, uint amount);
function mint(uint amount) public {
require(amount > 0, "amount>0");
balance[msg.sender] += amount;
emit Minted(msg.sender, amount);
}
function transfer(address to, uint amount) public {
require(balance[msg.sender] >= amount, "insufficient");
balance[msg.sender] -= amount;
balance[to] += amount;
emit Transferred(msg.sender, to, amount);
}
function balanceOf(address a) public view returns (uint) {
return balance[a];
}
}