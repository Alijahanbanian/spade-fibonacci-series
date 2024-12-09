import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import asyncio

class ParentAgent(Agent):
    class BehParent(CyclicBehaviour):
        async def on_start(self):
            self.number = 1
            print(f"ParentAgent: {self.number}")
        async def run(self):
            if self.number > 1000:
                self.kill(exit_code=0)
                return
            msg = Message(to = "Child@localhost")
            msg.body = str(self.number)
            await self.send(msg)
            reply = await self.receive(timeout=10)
            if reply:
                received_number = int(reply.body)
                self.number = received_number + self.number
                print(f"ParentAgent: {reply.body}")
            else:
                print("ParentAgent not recive ...")
    async def setup(self):
        print("Starting ParentAgent...")
        child_agent = ChildAgent("Child@localhost", "password")
        await child_agent.start(auto_register = True)
        self.add_behaviour(self.BehParent())

class ChildAgent(Agent):
    class BehChild(CyclicBehaviour):
        async def on_start(self):
            self.number = 1 
        async def run(self):
            if self.number >1000:
                self.kill(exit_code=0)
                return
            msg = await self.receive(timeout=10)
            if msg:
                received_number = int(msg.body)
                self.number += received_number  
                print(f"ChildAgent: {msg.body}")
                reply = msg.make_reply()
                reply.body = str(self.number)
                await self.send(reply)
            else:
                print("ChildAgent: No message received.")
    async def setup(self):
        print("Starting ChildAgent...")
        self.add_behaviour(self.BehChild())

async def main():
    parent_agent = ParentAgent("Parent@localhost", "password")
    await parent_agent.start(auto_register = True)
    await spade.wait_until_finished(parent_agent)

asyncio.run(main())
