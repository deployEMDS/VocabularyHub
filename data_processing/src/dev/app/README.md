# App folder

This folder contains files used to run the application server in a container or on a Unix-like host. The README documents the purpose of each file, the main environment variables (from `.env`), and notes about how the `run-server.sh` launcher works.

## Files
- `.env`
  - Environment variable declarations used by `run-server.sh` and by the deployment environment.
  - The project includes a sample `.env` in this folder that documents recommended defaults (network, logging, worker and timeout settings). Customize these values in a deployment-specific `.env` or via your container/orchestration environment.

- `.gitkeep`
  - Placeholder so the `app` folder is tracked by Git when empty. No runtime behavior.

- `run-server.sh`
  - Bash script that launches the application with Gunicorn.
  - The script computes a recommended number of workers based on available CPU cores and allows overriding with environment variables.
  - The script configures Gunicorn with many tunable options (bind address and port, log files and format, worker class, number of workers, connection/thread settings, timeouts, keepalive, request limits, temp directory, preload, etc.).
  - The script changes the working directory to `/usr/src` and expects a WSGI entrypoint named `wsgi:app` to be importable from that directory (the project provides a `wsgi.py` at the application root).
  - This launcher is intended for Unix-like environments (containers, Linux hosts, or WSL on Windows). It is not a Windows-native PowerShell script.

Key environment variables (defaults taken from the sample `.env` in this folder)
- Network
  - `BIND_ADDRESS` (`0.0.0.0`): IP address Gunicorn binds to.
  - `PORT` (`5000`): port to listen on.

- Logging
  - `ACCESS_LOG_FILE` (default: `-`): access log destination (`-` = stdout).
  - `ERROR_LOG_FILE` (default: `-`): error log destination (`-` = stderr/stdout depending on setup).
  - `LOG_LEVEL` (default: `info`): Gunicorn log level.
  - `ACCESS_LOG_FORMAT` (default shown in `.env`): format string for access logs.

- Workers and concurrency
  - `WORKERS` (default in sample: `4`, recommended formula: `(2 * CPU_CORES) + 1`): number of Gunicorn worker processes.
  - `WORKER_CLASS` (default: `gthread`): Gunicorn worker type (e.g. `sync`, `gthread`, `gevent`).
  - `WORKER_CONNECTIONS` (default: `1000`): relevant for async worker classes like `gevent`.
  - `THREADS` (default: `4`): number of threads per worker when using thread-capable worker classes.

- Timeouts and stability
  - `TIMEOUT` (default: `300`): worker timeout in seconds.
  - `GRACEFUL_TIMEOUT` (default: `60`): graceful shutdown timeout.
  - `KEEP_ALIVE` (default: `5`): keep-alive seconds for client connections.
  - `MAX_REQUESTS` (default: `1000`): number of requests a worker will process before restarting.
  - `MAX_REQUESTS_JITTER` (default: `100`): jitter added to `MAX_REQUESTS` to avoid coordinated restarts.
  - `LIMIT_REQUEST_LINE` and `LIMIT_REQUEST_FIELD_SIZE` (defaults: `0`): request size limits (0 = disabled).
  - `FORWARDED_ALLOW_IPS` (default: `*`): forwarded proxy IPs allowed by Gunicorn.

- Optimizations
  - `PRELOAD_APP` (default: `true` in sample): whether to preload the application before forking workers.
  - `WORKER_TMP_DIR` (default: `/dev/shm`): temporary directory for worker processes.


