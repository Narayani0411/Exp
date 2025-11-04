// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Splitter {
address[] public receivers;
mapping(address => uint) public owed;
constructor(address[] memory _receivers) {
require(_receivers.length > 0, "need receivers");
for (uint i = 0; i < _receivers.length; i++) {
receivers.push(_receivers[i]);
}
}
function split(uint total) public {
require(total > 0, "total>0");
uint share = total / receivers.length;
for (uint i = 0; i < receivers.length; i++) {
owed[receivers[i]] += share;
}
}
function myOwed() public view returns (uint) {
return owed[msg.sender];
}
function receiversCount() public view returns (uint) {
return receivers.length;
}
}