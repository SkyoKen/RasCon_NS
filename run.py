import argparse
import asyncio
import logging
import os
from contextlib import contextmanager

from joycontrol import logging_default as log,utils
from joycontrol.command_line_interface import ControllerCLI
from joycontrol.controller import Controller
from joycontrol.memory import FlashMemory
from joycontrol.protocol import controller_protocol_factory
from joycontrol.server import create_hid_server
import command
logger = logging.getLogger(__name__)


async def _main(args):

    # Create memory containing default controller stick calibration
    spi_flash = FlashMemory()
        
    # Get controller name to emulate from arguments
    controller = Controller.PRO_CONTROLLER
    
    with utils.get_output(path=args.log, default=None) as capture_file:
        factory = controller_protocol_factory(controller, spi_flash=spi_flash)
        transport, protocol = await create_hid_server(factory, 
                                                      ctl_psm=17,itr_psm=19, 
                                                      capture_file=capture_file)

        controller_state = protocol.get_controller_state()
        
        # Create command line interface and add some extra commands
        cli = command.CCLI(controller_state)
        
        try:
            await controller_state.connect()
            await cli.run()
        finally:
            logger.info('Stopping communication...')
            await transport.close()

if __name__ == '__main__':
    # check if root
    if not os.geteuid() == 0:
        raise PermissionError('Script must be run as root!')

    # setup logging
    log.configure()

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        _main(args)
    )
   

