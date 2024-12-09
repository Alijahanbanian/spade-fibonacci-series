
# SPADE Fibonacci Sequence Communication Demo

This project demonstrates agent-based communication using the **SPADE library** to generate the Fibonacci sequence. Two agents, `ParentAgent` and `ChildAgent`, interact to compute and acknowledge Fibonacci numbers.

---

## Features

- **ParentAgent**: Computes Fibonacci numbers and sends them to `ChildAgent`.
- **ChildAgent**: Receives Fibonacci numbers and acknowledges receipt.
- Implements **CyclicBehaviour** for continuous interaction.
- Demonstrates message passing using SPADE's `Message` class.

---

## Prerequisites

- **Linux OS**
- Python 3.8 or higher
- XMPP server, such as **Prosody**, running on `localhost`.

---

## Installation

### 1. Install Python and Dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
pip install spade
```

### 2. Set Up Prosody XMPP Server

1. **Install Prosody**  
   ```bash
   sudo apt install prosody
   ```

2. **Configure Prosody**  
   Edit `/etc/prosody/prosody.cfg.lua` to include:
   ```lua
   VirtualHost "localhost"
   ```

3. **Create Agent Accounts**  
   ```bash
   sudo prosodyctl adduser Parent@localhost
   Password: password
   sudo prosodyctl adduser Child@localhost
   Password: password
   ```

4. **Restart Prosody**  
   ```bash
   sudo systemctl restart prosody
   ```

---

## Usage

### Run the Script

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Alijahanbanian/spade-fibonacci-series.git
   cd spade-fibonacci-series
   ```

2. **Run the Script**  
   ```bash
   python3 main.py
   ```

3. **Expected Behavior**
   - `ParentAgent` computes and sends Fibonacci numbers.
   - `ChildAgent` receives numbers and acknowledges them.
   - Interaction continues until a number exceeds 1000.

---

## Code Overview

### Agents

- **ParentAgent**  
  - Computes the Fibonacci sequence.
  - Sends numbers to `ChildAgent` and waits for acknowledgment.

- **ChildAgent**  
  - Receives Fibonacci numbers.
  - Sends acknowledgments to `ParentAgent`.

### Key Methods

- `CyclicBehaviour.run()`: Defines recurring agent tasks.
- `Message`: Handles message exchange.

---

## Example Output

```plaintext
Starting ParentAgent...
Starting ChildAgent...
ParentAgent: 1
ChildAgent: 1
ParentAgent: 2
ChildAgent: 3
ParentAgent: 5
ChildAgent: 8
ParentAgent: 13
...
ParentAgent: 610
ChildAgent: 987
ParentAgent: 1597
```

---

## Troubleshooting

- **No response from ChildAgent**  
  - Ensure both agents are registered on the XMPP server.
  - Check network connectivity.

- **Script exits unexpectedly**  
  - Verify the Python environment and SPADE installation.



