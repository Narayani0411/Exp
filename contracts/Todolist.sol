// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract ToDoList {
struct Task {
string description;
bool completed;
}
Task[] private tasks;
/// @notice Add a new task to the list.
/// @param _description The text description of the task.
function addTask(string memory _description) public {
tasks.push(Task(_description, false));
}
/// @notice Toggle completion status of a task.
/// @param _index Index of the task to toggle.
function toggleTask(uint256 _index) public {
require(_index < tasks.length, "Invalid task index");
tasks[_index].completed = !tasks[_index].completed;
}
/// @notice Delete a task by its index.
/// @param _index Index of the task to delete.
function deleteTask(uint256 _index) public {
require(_index < tasks.length, "Invalid task index");
tasks[_index] = tasks[tasks.length - 1];
tasks.pop();
}
/// @notice Get the full list of tasks.
/// @return Array of all tasks with their descriptions and status.
function getTasks() public view returns (Task[] memory) {
return tasks;
}
/// @notice Get the total number of tasks.
/// @return The count of tasks currently stored.
function getTaskCount() public view returns (uint256) {
return tasks.length;
}
}