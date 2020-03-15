import inspect
import logging
import asyncio

from aioconsole import ainput

from joycontrol.controller_state import button_push, ControllerState

logger = logging.getLogger(__name__)


class ControllerCLI:
    def __init__(self, controller_state: ControllerState):
        self.controller_state = controller_state
        self.available_buttons = self.controller_state.button_state.get_available_buttons()
        self.available_sticks = {'ls','rs'}
        self.script = False

    async def write(self,msg):
        with open('file/message.txt','a') as f:
            f.write(msg+'\n')

    async def get(self,file):
        with open('file/'+file,'r') as f:
            result = list()
            for line in f.readlines():                          #依次读取每行
                line = line.strip()                             #去掉每行头尾空白
                if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
                    continue                                    #是的话，跳过不处理
                result.append(line.lower())                     #保存小写文字
            return result
    async def clear(self,file):
        with open('file/'+file,'w+') as f:
            return f.truncate() 

    async def runCommand(self):
        user_input = await self.get('command.txt')
        if not user_input:
            return
        await self.clear('command.txt')

        for command in user_input:
            cmd, *args = command.split()
 
            if cmd == 'run':
                self.script = True
            elif cmd == 'stop':
                self.script = False
            elif cmd == 'off' or cmd =='on':
                print('开/关 未完成')
            else:
                await self.pressButton(command)
        return ' '
    async def pressButton(self,*commands):
         for command in commands:
             cmd,*args=command.split()
             if cmd in self.available_sticks:
                 print('side = ',cmd,'direction = ',args[0])
             elif cmd in self.available_buttons: #按钮
                 await button_push(self.controller_state,cmd)
             elif cmd.isdecimal(): #等待（ms）
                 await asyncio.sleep(float(cmd)/1000)
             elif cmd == 'print':
                 print(args[0])
             else: #错误代码
                 print('command',cmd,'not found')
    async def readCommand(self,file):
        user_input = await self.get(file)
        if not user_input:
            return
        await self.clear(file)
    def isCommand(self,cmd):
        return cmd in self.available_sticks or cmd in self.available_buttons or cmd.isdecimal() or cmd =='print'

    def forCheck(self,n,user_input):
        commands = []
        until = -1
        for i in range(len(user_input)):
            if i <= n or i<= until:
                continue

            cmd,*args = user_input[i].split()
            if cmd == 'for':
                for _ in range(int(args[0])):
                    until,forcmd = self.forCheck(i,user_input)
                    for get in forcmd:
                        commands.append(get)
            elif cmd == 'next':
                return i,commands
            elif self.isCommand(cmd):
                commands.append(user_input[i])
            else:
                print('command',cmd,'not found')

    async def runScript(self):
        user_input = await self.get('script.txt')
        if not user_input:
            return
        await self.clear('script.txt')

        commands=[]
        until=-1
        for i in range(len(user_input)):
            #检测按键
            await self.runCommand()
            #确认脚本是否要停止
            if self.script == False:
                return

            if i <= until:
                continue

            cmd, *args =user_input[i].split()
            if cmd == 'for':
                for _ in range(int(args[0])):
                    until,forcmd = self.forCheck(i,user_input)
                    for get in forcmd:
                        commands.append(get)
            elif self.isCommand(cmd):
                commands.append(user_input[i])
            else:
                print('commands',cmd,'not found')

        for command in commands:
            await self.runCommand()
            if self.script == False:
                return

            await self.pressButton(command)

        self.script = False

    async def run(self):

        while True:
            #等待输入
            cmd = await self.runCommand()
            if cmd == 'exit':
                return
            if self.script == True:
                await self.runScript()


