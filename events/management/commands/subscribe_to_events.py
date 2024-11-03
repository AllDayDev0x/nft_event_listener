import asyncio
from django.core.management.base import BaseCommand
from web3 import AsyncWeb3, WebSocketProvider
from eth_abi import decode
from decimal import Decimal
from events.models import TransferEvent 
from django.conf import settings
from asgiref.sync import sync_to_async

class Command(BaseCommand):
    help = "Subscribe to NFT transfer events"

    def handle(self, *args, **kwargs):
        asyncio.run(self.subscribe_to_transfer_events())

    async def subscribe_to_transfer_events(self):
        async with AsyncWeb3(WebSocketProvider("wss://mainnet.infura.io/ws/v3/" + settings.INFURA_API_KEY)) as w3:
            transfer_event_topic = w3.keccak(text="Transfer(address,address,uint256)")
            filter_params = {
                "address": settings.NFT_ADDRESS,
                "topics": [transfer_event_topic],
            }

            subscription_id = await w3.eth.subscribe("logs", filter_params)
            self.stdout.write(f"Subscribed to transfer events with ID: {subscription_id}")

            async for payload in w3.socket.process_subscriptions():
                result = payload["result"]
                print(result)
                
                from_addr = decode(["address"], result["topics"][1])[0]
                to_addr = decode(["address"], result["topics"][2])[0]
                token_id = decode(["uint256"], result["topics"][3])[0]

                await self.save_transfer_event(
                    from_addr=from_addr,
                    to_addr=to_addr,
                    token_id=token_id,
                    transaction_hash=result["transactionHash"].hex(),
                    block_number=result["blockNumber"]
                )
                self.stdout.write(f"{token_id} NFT transferred from {from_addr} to {to_addr}")

    @sync_to_async
    def save_transfer_event(self, from_addr, to_addr, token_id, transaction_hash, block_number):
        TransferEvent.objects.create(
            from_address=from_addr,
            to_address=to_addr,
            token_id=token_id,
            transaction_hash=transaction_hash,
            block_number=block_number
        )