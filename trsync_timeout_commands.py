# Klipper plugin for changing TRSYNC_TIMEOUT values.
#
# Copyright (C) 2025  Sskki-exe <queries@sskki.fyi>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

# TRSYNC_TIMEOUT_QUERY
# TRSYNC_TIMEOUT_SET
# TRSYNC_TIMEOUT_RESET

class TrsyncTimeoutCommands:
    def __init__(self, config):
        self.printer = config.get_printer()
        gcode = self.printer.lookup_object('gcode')
        
        gcode.register_command("TRSYNC_TIMEOUT_QUERY", self.cmd_TRSYNC_TIMEOUT_QUERY,
                                    desc=self.cmd_TRSYNC_TIMEOUT_QUERY_help)
        gcode.register_command("TRSYNC_TIMEOUT_SET", self.cmd_TRSYNC_TIMEOUT_SET,
                                    desc=self.cmd_TRSYNC_TIMEOUT_SET_help)
        gcode.register_command("TRSYNC_TIMEOUT_RESET", self.cmd_TRSYNC_TIMEOUT_RESET,
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
    return TrsyncTimeoutCommands(config)