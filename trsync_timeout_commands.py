# Klipper plugin for changing TRSYNC_TIMEOUT values.
#
# Copyright (C) 2025  Sskki-exe <queries@sskki.fyi>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

# TRSYNC_TIMEOUT_QUERY
# TRSYNC_TIMEOUT_SET
# TRSYNC_TIMEOUT_RESET

class TrsyncTimeoutCommandsHelper:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.printer.register_event_handler("klippy:connect", self.handle_connect)

    def handle_connect(self):
       k = self.printer.lookup_object('toolhead').get_kinematics()

    def test_macro(self):
        toolhead = self.printer.lookup_object("toolhead")
        gcode = self.printer.lookup_object('gcode')
        curpos = toolhead.get_position()

        # this line outputs text in the terminal
        gcode.respond_info("Curpos is " + str(curpos))


class TrsyncTimeoutCommands:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.TrsyncTimeoutCommands_helper = TrsyncTimeoutCommandsHelper(config)
        gcode = self.printer.lookup_object('gcode')

        # make your gcode recognisable
        gcode.register_command("TEST_MACRO", self.cmd_TEST_MACRO, self.cmd_TEST_MACRO_help)


    cmd_TEST_MACRO_help = "Help hint at what this gcode macro does"
    def cmd_TEST_MACRO(self, gcmd):
        self.TrsyncTimeoutCommands_helper.test_macro()
    
def load_config(config):
    return TrsyncTimeoutCommands(config)