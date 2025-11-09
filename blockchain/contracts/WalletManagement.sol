// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract WalletSim {
mapping(address => uint) public balance;
event Deposited(address indexed who, uint amount);
event Withdrawn(address indexed who, uint amount);
event Transferred(address indexed from, address indexed to, uint amount);
/// @notice Simulates depositing a specific amount to your wallet.
/// @param amount Amount to deposit (example: 100)
function deposit(uint amount) public {
require(amount > 0, "amount>0");
balance[msg.sender] += amount;
emit Deposited(msg.sender, amount);
}
/// @notice Withdraw a certain amount if your simulated balance allows it.
/// @param amount Amount to withdraw.
function withdraw(uint amount) public {
require(balance[msg.sender] >= amount, "insufficient");
balance[msg.sender] -= amount;
emit Withdrawn(msg.sender, amount);
}
/// @notice Transfer simulated funds to another user.
/// @param to Recipient address.
/// @param amount Amount to transfer.
function transferTo(address to, uint amount) public {
require(balance[msg.sender] >= amount, "insufficient");
balance[msg.sender] -= amount;
balance[to] += amount;
emit Transferred(msg.sender, to, amount);
}
/// @notice Get your simulated balance.
/// @return Current balance of the caller.
function myBalance() public view returns (uint) {
return balance[msg.sender];
}
}