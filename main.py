from telethon.sync import TelegramClient, events

# Get your api_id and api_hash here https://my.telegram.org/apps
api_id = 0000000
api_hash = ''

done = 0
count = sum(1 for line in open('card.txt'))

client = TelegramClient('session', api_id, api_hash)
client.start()

@client.on(events.NewMessage(from_users='SDBB_Bot'))
@client.on(events.MessageEdited(from_users='SDBB_Bot'))

async def MessageHandlers(event):
    global done
    if 'wait' in event.message.text or 'Waiting' in event.message.text:
        return
       
    done += 1
    print(event.message.text.replace("`", ""))
    print()
    
    if done == count:
        client.disconnect()

async def send_message_to_bot(cc):
    await client.send_message('SDBB_Bot', f'/auth {cc}')

async def main():
    with open('card.txt', 'r') as file:
        for line in file:
            cc = line.strip()
            await send_message_to_bot(cc)
            if done == count:
                break


with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()            
