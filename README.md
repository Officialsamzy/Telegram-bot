
# Telegram Message Forwarding Script

This Python script uses the [Telethon](https://docs.telethon.dev/en/stable/) library to automate the forwarding of messages from one Telegram group to another. It is ideal for community management, information sharing, and tracking discussions across groups.

## Features

- **Message Cloning**: Automatically fetches and forwards the last 100 messages from a specified source group to a target group.
- **Asynchronous Execution**: Utilizes Python's asynchronous capabilities for efficient message handling.
- **Easy Configuration**: Users can quickly set their API credentials and group identifiers in the script.
- **Command-Line Interface**: Run the script from the command line with ease.

## Requirements

- Python 3.x
- Telethon library (install using `pip`)
- A verified Telegram account with access to the specified groups

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
   cd REPO-NAME
