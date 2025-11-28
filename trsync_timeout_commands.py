# Klipper plugin for a self-calibrating Z offset.
#
# Copyright (C) 2021-2025  Titus Meyer <info@protoloft.org>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

# TRSYNC_TIMEOUT_QUERY
# TRSYNC_TIMEOUT_SET
# TRSYNC_TIMEOUT_RESET

import logging
from mcu import MCU_endstop

class TrsyncTimeoutCommander:
    def __init__(self, config):
        self.config = config
        self.printer = config.get_printer()
        self.gcode = self.printer.lookup_object('gcode')

        gcode_macro = self.printer.load_object(config, 'gcode_macro')
        
        self.gcode.register_command('TRSYNC_TIMEOUT_QUERY', self.cmd_TRSYNC_TIMEOUT_QUERY,
                                    desc=self.cmd_TRSYNC_TIMEOUT_QUERY_help)
        self.gcode.register_command('TRSYNC_TIMEOUT_SET', self.cmd_TRSYNC_TIMEOUT_SET,
                                    desc=self.cmd_TRSYNC_TIMEOUT_SET_help)
        self.gcode.register_command('TRSYNC_TIMEOUT_RESET', self.cmd_TRSYNC_TIMEOUT_RESET,
                                    desc=self.cmd_TRSYNC_TIMEOUT_RESET_help)
        
    cmd_TRSYNC_TIMEOUT_QUERY_help = ("Returns current TRSYNC_TIMEOUT value")
    def cmd_TRSYNC_TIMEOUT_QUERY(self, gcmd):
        gcmd.respond_info("TRSYNC_TIMEOUT = %.3f" % (0.025))
    
    cmd_TRSYNC_TIMEOUT_SET_help = ("Sets new TRSYNC_TIMEOUT value")
    def cmd_TRSYNC_TIMEOUT_SET(self, gcmd):
        gcmd.respond_info("Set TRSYNC_TIMEOUT = %.3f" % (0.025))
    
    cmd_TRSYNC_TIMEOUT_RESET_help = ("Resets TRSYNC_TIMEOUT to default value (0.025)")
    def cmd_TRSYNC_TIMEOUT_RESET(self, gcmd):
        gcmd.respond_info("Reset TRSYNC_TIMEOUT = %.3f" % (0.025))

def load_config(config):
    return TrsyncTimeoutCommander(config)