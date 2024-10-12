from telethon import TelegramClient
import asyncio
import sys

# Replace these with your API_ID and API_HASH from my.telegram.org
api_id = 'your_api_id'  # Replace with your actual API ID
api_hash = 'your_api_hash'  # Replace with your actual API HASH
source_group = 'source_group_link_or_id'  # Replace with your source group link or ID
target_group = 'taxfarmingETH'  # Target group link or ID

async def main(phone_number):
    client = TelegramClient('session_name', api_id, api_hash)

    async with client:
        # Fetch the last 100 messages from the source group
        async for message in client.iter_messages(source_group, limit=100):
            await client.send_message(target_group, message.text)  # Send the message to the target group

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clone_messages.py '<phone_number>'")
        sys.exit(1)

    phone_number = sys.argv[1]
    asyncio.run(main(phone_number))
