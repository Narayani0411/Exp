// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract LotterySystem {
address public manager;
string[] private players;
string public winner;
bool public lotteryEnded;
constructor() {
manager = msg.sender;
lotteryEnded = false;
}
/// @notice Enter the lottery by providing your name.
/// @param _name The name of the participant.
function enterLottery(string memory _name) public {
    require(!lotteryEnded, "Lottery already ended");
players.push(_name);
}
/// @dev Generates a pseudo-random number for winner selection.
function random() private view returns (uint256) {
return uint256(
keccak256(abi.encodePacked(block.timestamp, players.length))
);
}
/// @notice Manager picks a random winner from participants.
function pickWinner() public {
require(msg.sender == manager, "Only manager can pick winner");
require(players.length > 0, "No participants yet");
require(!lotteryEnded, "Lottery already ended");
uint256 index = random() % players.length;
winner = players[index];
lotteryEnded = true;
}
/// @notice Returns the list of all participants.
function getPlayers() public view returns (string[] memory) {
return players;
}
/// @notice Resets the lottery for a new round.
function resetLottery() public {
require(msg.sender == manager, "Only manager can reset");
delete players;
lotteryEnded = false;
winner = "";
}
}