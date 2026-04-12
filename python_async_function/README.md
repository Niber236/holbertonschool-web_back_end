# Python - Asynchronous Programming

## Description
This project covers the basics and advanced concepts of asynchronous programming in Python using the `asyncio` library. The goal is to understand how to write concurrent code that can handle multiple tasks efficiently without blocking the execution flow.

## Learning Objectives
By the end of this project, I am able to explain:
* The syntax for `async` and `await`.
* How to execute an async program with `asyncio`.
* How to run multiple coroutines concurrently.
* How to create and manage `asyncio` tasks.
* How to measure the runtime of asynchronous functions.

## Requirements
* **OS**: Ubuntu 20.04 LTS.
* **Language**: Python 3.9.
* **Style**: All code follows the `pycodestyle` (version 2.5.x) standard.
* **Type Annotations**: All functions and coroutines are strictly type-annotated.
* **Documentation**: Every module and function includes comprehensive docstrings.

## Files and Tasks

| File | Description |
| --- | --- |
| `0-basic_async_syntax.py` | An asynchronous coroutine that waits for a random delay. |
| `1-concurrent_coroutines.py` | Executing multiple coroutines concurrently using `as_completed`. |
| `2-measure_runtime.py` | Function to measure the average execution time of concurrent tasks. |
| `3-tasks.py` | Converting coroutines into `asyncio.Task` objects. |
| `4-tasks.py` | Altering the concurrent routine to use task-based execution. |

## Author
* **Stamina** (ou ton nom complet pour Holberton)