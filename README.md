# azure-durable-function-python-concurrency
azure-durable-function-python-concurrency

Improve throughput performance of Python apps in Azure Functions.

## Async

Because Python is a single-threaded runtime, a host instance for Python can process only one function invocation at a time by default. For applications that process a large number of I/O events and/or is I/O bound, you can improve performance significantly by running functions asynchronously.
