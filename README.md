# CoreDotCloud

CoreDotCloud is a lightweight system monitoring tool that collects CPU, memory, disk, and network usage data and sends it to a predefined RESTful API.

## Features

-   Collects system resource usage every 30 seconds
-   Sends data as a compact JSON payload to reduce network overhead
-   Simple setup with a single configuration file
-   Easily installable via PyPI

## Installation

Install CoreDotCloud via pip:

```sh
pip install coredotcloud
```

## Configuration

Before running the tool, create a configuration file in your home directory:

```sh
nano ~/.coredotcloud.json
```

Insert the following content:

```json
{
    "API_URL": "https://mon.core.today/sentinel",
    "API_KEY": "your-api-key"
}
```

Replace `your-api-key` with your actual API key.

## Usage

Once configured, simply run the following command:

```sh
coredotcloud
```

The program will start collecting and sending system resource usage data every 30 seconds.

## Data Format

The data is sent in the following JSON format:

```json
{
    "apikey": "DKWs8wl",
    "data": [14.8, 128.0, 57.78, 46.0, 3721.87, 10.39, 1.5, 277.0, 8.0]
}
```

### Data Order

The list under `data` follows this structure:

1. **CPU Usage (%)**
2. **Total Memory (GB)**
3. **Used Memory (GB)**
4. **Memory Usage (%)**
5. **Total Disk Space (GB)**
6. **Used Disk Space (GB)**
7. **Disk Usage (%)**
8. **Network Receive Speed (KB/s)**
9. **Network Transmit Speed (KB/s)**

## Development & Contribution

### Setting Up for Development

Clone the repository:

```sh
git clone https://github.com/yourusername/coredotcloud.git
cd coredotcloud
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Run the program:

```sh
python -m coredotcloud.main
```

### Running Tests

```sh
pytest tests/
```

## License

CoreDotCloud is released under the MIT License.
