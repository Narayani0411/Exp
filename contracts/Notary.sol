// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Notary {
struct Doc { address owner; uint ts; }
mapping(bytes32 => Doc) public docs;
event Notarized(bytes32 hash, address owner);
function generateHash(string memory text) public pure returns (bytes32) {
return keccak256(abi.encodePacked(text));
}
function notarizeDocument(string memory text) public returns (bytes32) {
bytes32 h = keccak256(abi.encodePacked(text));
docs[h] = Doc(msg.sender, block.timestamp);
emit Notarized(h, msg.sender);
return h;
}
function verifyDocument(string memory text) public view returns (bool,
address, uint) {
bytes32 h = keccak256(abi.encodePacked(text));
Doc storage d = docs[h];
if (d.owner != address(0)) {
    return (true, d.owner, d.ts);
} else {
return (false, address(0), 0);
}
}
}