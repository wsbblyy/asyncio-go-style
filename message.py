import asyncio
import random
import threading
import time
from util.db import database
import janus



class MessageController:

    def __init__(self):
       
        self.main_loop = asyncio.get_event_loop()

        async def queue_init():
            queue = janus.Queue()
            self.queue = queue.async_q

        self.main_loop.create_task(queue_init())

        # self.main_loop.create_task(self.queue.async_q)
        self.main_loop.create_task(self.cumsuer())

        def run_main_loop():
            self.main_loop.run_forever()

        self.main_loop_thread = threading.Thread(target=run_main_loop)
        self.main_loop_thread.start()
        

    async def cumsuer(self):
        
        while True:
            item = await self.queue.get()

            if item == None:
                # self.stop_main_loop()
                break
            
            self.main_loop.create_task(self.worker(item))
        
        
    async def worker(self, item):
        print(item)

    def push(self, item):
        self.queue.put_nowait(item)

