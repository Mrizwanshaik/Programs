"""@Package: powersupplyCtrl
This module contains control functions for powersupply EA-PS 2342-06 B
@author: mshaik
"""


import Serial_Control
import time

def turn_on_to_v(volt, node=0):
    """Switsch on the powersupply to voltage value
        :param volt: voltage value to be setted
        :param node: 0 is for powersupply output 1; 1 is for powersupply output 2
        :return:nothing
    """
    turnon = Serial_Control.power_supply_control()
    turnon.init_pwr_supply_com()
    x = turnon.check_status(node)
    turnon.parse_response(x)
    print "power is : " + turnon.answer_telegram.data_field[2:4]
    turnon.activate_remote_node(node, True)
    turnon.set_volt(node, volt)
    turnon.set_output_on_off(node, True)
    turnon.activate_remote_node(0, False)
    turnon.activate_remote_node(1, False)
    turnon.close_pwr_supply_com()

def turn_off(node=0):
    """Switsch off the powersupply to voltage value
        :param node: 0 is for powersupply output 1; 1 is for powersupply output 2
        :return:nothing
    """
    turnoff = Serial_Control.power_supply_control()
    turnoff.init_pwr_supply_com()
    x = turnoff.check_status(node)
    turnoff.parse_response(x)
    print "power is : " + turnoff.answer_telegram.data_field[2:4]
    turnoff.activate_remote_node(node, True)
    turnoff.set_volt(node, 0)
    turnoff.set_output_on_off(node, True)
    turnoff.activate_remote_node(0, False)
    turnoff.activate_remote_node(1, False)
    turnoff.close_pwr_supply_com()

def query_actual_current(node=0):
    """Read the actual current on the output of the powersupply
        :param node: 0 is for powersupply output 1; 1 is for powersupply output 2
        :return:actual current
    """
    mypwrcmd = Serial_Control.power_supply_control()
    mypwrcmd.init_pwr_supply_com()
    x = mypwrcmd.check_status(node)
    actCur = mypwrcmd.get_actual_current(x)
    mypwrcmd.close_pwr_supply_com()
    return actCur

def query_actual_voltage(node=0):
    """Read the actual voltage on the output of the powersupply
        :param node: 0 is for powersupply output 1; 1 is for powersupply output 2
        :return:actual voltage
    """
    mypwrcmd = Serial_Control.power_supply_control()
    mypwrcmd.init_pwr_supply_com()
    x = mypwrcmd.check_status(node)
    actVolt = mypwrcmd.get_actual_voltage(x)
    mypwrcmd.close_pwr_supply_com()
    return actVolt

def ScaLa_restart(t, volt, node=0):
    """Make a hard reset on the output of the powersupply
        :param node: 0 is for powersupply output 1; 1 is for powersupply output 2
        :return:nothing
    """
    turn_off(node)
    time.sleep(t)
    turn_on_to_v(volt, node)

if __name__ == "__main__":
    turn_on_to_v(12,1)
    time.sleep(5)
    turn_on_to_v(12,0)
    #turn_off(0)
    #turn_off(1)
