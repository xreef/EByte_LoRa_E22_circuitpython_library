# Author: Renzo Mischianti
# Website: www.mischianti.org
#
# Description:
# This script demonstrates how to use the E22 LoRa module with CircuitPython.
# It initializes the module, retrieves the current configuration,
# sets a new configuration, and restores the default configuration.
# It also includes examples of sending and receiving data using the module.
#
# Note: This code was written and tested using CircuitPython on a ESP32 board.
#       It works with other boards, but you may need to change the UART pins.

from lora_e22 import LoRaE22, print_configuration, Configuration
from lora_e22_constants import OperatingFrequency, FixedTransmission, TransmissionPower, \
    AirDataRate, UARTParity, UARTBaudRate, RssiAmbientNoiseEnable, SubPacketSetting, WorPeriod, \
    LbtEnableByte, RssiEnableByte, TransmissionPower22
from lora_e22_operation_constant import ResponseStatusCode
import busio
import board


# Create a UART object to communicate with the LoRa module with ESP32
uart2 = busio.UART(board.TX2, board.RX2, baudrate=9600)
# Create a LoRaE22 object, passing the UART object and pin configurations
lora = LoRaE22('400T22D', uart2, aux_pin=board.D15, m0_pin=board.D21, m1_pin=board.D19)

# Create a UART object to communicate with the LoRa module with Raspberry Pi Pico
# uart2 = busio.UART(board.TX1, board.RX1, baudrate=9600)
# Use the Serial1 pins of Arduino env on the Raspberry Pi Pico
# uart2 = busio.UART(board.D9, board.D8, baudrate=9600)
# lora = LoRaE22('433T20D', uart2, aux_pin=board.D2, m0_pin=board.D10, m1_pin=board.D11)
# STM32F411CEU6 Shield
# uart2 = busio.UART(board.TX2, board.RX2, baudrate=9600)
# lora = LoRaE22('400T22D', uart2, aux_pin=board.PA0, m0_pin=board.PB0, m1_pin=board.PB2)

# Initialize the LoRa module and print the initialization status code
code = lora.begin()
print("Initialization: {}", ResponseStatusCode.get_description(code))

##########################################################################################
# GET CONFIGURATION
##########################################################################################

# Retrieve the current configuration of the LoRa module and print it to the console
code, configuration = lora.get_configuration()
print("Retrieve configuration: {}", ResponseStatusCode.get_description(code))
print("------------- CONFIGURATION BEFORE CHANGE -------------")
print_configuration(configuration)

##########################################################################################
# SET CONFIGURATION
# To set the configuration, you must set the configuration with the new values
##########################################################################################

# Create a new Configuration object with the desired settings
configuration_to_set = Configuration('400T22D')
configuration_to_set.ADDL = 0x02
configuration_to_set.ADDH = 0x01
configuration_to_set.CHAN = 23

configuration_to_set.NETID = 0

configuration_to_set.SPED.airDataRate = AirDataRate.AIR_DATA_RATE_100_96
configuration_to_set.SPED.uartParity = UARTParity.MODE_00_8N1
configuration_to_set.SPED.uartBaudRate = UARTBaudRate.BPS_9600

configuration_to_set.OPTION.subPacketSetting = SubPacketSetting.SPS_064_10
configuration_to_set.OPTION.transmissionPower = TransmissionPower('400T22D').\
                                                    get_transmission_power().POWER_10
# or
# configuration_to_set.OPTION.transmissionPower = TransmissionPower22.POWER_10
configuration_to_set.OPTION.RSSIAmbientNoise = RssiAmbientNoiseEnable.RSSI_AMBIENT_NOISE_ENABLED

configuration_to_set.TRANSMISSION_MODE.WORTransceiverControl = WorTransceiverControl.WOR_TRANSMITTER
configuration_to_set.TRANSMISSION_MODE.enableLBT = LbtEnableByte.LBT_DISABLED
configuration_to_set.TRANSMISSION_MODE.enableRSSI = RssiEnableByte.RSSI_ENABLED
configuration_to_set.TRANSMISSION_MODE.enableRepeater = RepeaterModeEnableByte.REPEATER_DISABLED
configuration_to_set.TRANSMISSION_MODE.fixedTransmission = FixedTransmission.FIXED_TRANSMISSION
configuration_to_set.TRANSMISSION_MODE.WORPeriod = WorPeriod.WOR_1500_010

configuration_to_set.CRYPT.CRYPT_H = 1
configuration_to_set.CRYPT.CRYPT_L = 1


# Set the new configuration on the LoRa module and print the updated configuration to the console
code, confSetted = lora.set_configuration(configuration_to_set)
print("------------- CONFIGURATION AFTER CHANGE -------------")
print(ResponseStatusCode.get_description(code))
print_configuration(confSetted)

##########################################################################################
# RESTORE DEFAULT CONFIGURATION
# To restore the default configuration, you must set the configuration with the default values
##########################################################################################

# Set the configuration to default values and print the updated configuration to the console
print("------------- RESTORE ALL DEFAULT -------------")
configuration_to_set = Configuration('400T22D')
code, confSetted = lora.set_configuration(configuration_to_set)
print(ResponseStatusCode.get_description(code))
print_configuration(confSetted)


# Initialization: {} Success
# Retrieve configuration: {} Success
# ------------- CONFIGURATION BEFORE CHANGE -------------
# ----------------------------------------
# HEAD :  0xc1   0x0   0x9
#
# AddH :  0x0
# AddL :  0x0
#
# Chan :  23  ->  433
#
# SpeedParityBit :  0b0  ->  8N1 (Default)
# SpeedUARTDatte :  0b11  ->  9600bps (default)
# SpeedAirDataRate :  0b10  ->  2.4kbps (default)
#
# OptionSubPacketSett:  0b0  ->  240bytes (default)
# OptionTranPower :  0b0  ->  22dBm (Default)
# OptionRSSIAmbientNo:  0b0  ->  Disabled (default)
#
# TransModeWORPeriod :  0b11  ->  2000ms (default)
# TransModeTransContr:  0b0  ->  WOR Receiver (default)
# TransModeEnableLBT :  0b0  ->  Disabled (default)
# TransModeEnableRSSI:  0b0  ->  Disabled (default)
# TransModeEnabRepeat:  0b0  ->  Disabled (default)
# TransModeFixedTrans:  0b0  ->  Transparent transmission (default)
# ----------------------------------------
# ------------- CONFIGURATION AFTER CHANGE -------------
# Success
# ----------------------------------------
# HEAD :  0xc1   0x0   0x9
#
# AddH :  0x1
# AddL :  0x2
#
# Chan :  23  ->  433
#
# SpeedParityBit :  0b0  ->  8N1 (Default)
# SpeedUARTDatte :  0b11  ->  9600bps (default)
# SpeedAirDataRate :  0b100  ->  9.6kbps
#
# OptionSubPacketSett:  0b10  ->  64bytes
# OptionTranPower :  0b11  ->  10dBm
# OptionRSSIAmbientNo:  0b1  ->  Enabled
#
# TransModeWORPeriod :  0b10  ->  1500ms
# TransModeTransContr:  0b1  ->  WOR Transmitter
# TransModeEnableLBT :  0b0  ->  Disabled (default)
# TransModeEnableRSSI:  0b1  ->  Enabled
# TransModeEnabRepeat:  0b0  ->  Disabled (default)
# TransModeFixedTrans:  0b1  ->  Fixed transmission (first three bytes can be used
#  as high/low address and channel)
# ----------------------------------------
# ------------- RESTORE ALL DEFAULT -------------
# Success
# ----------------------------------------
# HEAD :  0xc1   0x0   0x9
#
# AddH :  0x0
# AddL :  0x0
#
# Chan :  23  ->  433
#
# SpeedParityBit :  0b0  ->  8N1 (Default)
# SpeedUARTDatte :  0b11  ->  9600bps (default)
# SpeedAirDataRate :  0b10  ->  2.4kbps (default)
#
# OptionSubPacketSett:  0b0  ->  240bytes (default)
# OptionTranPower :  0b0  ->  22dBm (Default)
# OptionRSSIAmbientNo:  0b0  ->  Disabled (default)
#
# TransModeWORPeriod :  0b11  ->  2000ms (default)
# TransModeTransContr:  0b0  ->  WOR Receiver (default)
# TransModeEnableLBT :  0b0  ->  Disabled (default)
# TransModeEnableRSSI:  0b0  ->  Disabled (default)
# TransModeEnabRepeat:  0b0  ->  Disabled (default)
# TransModeFixedTrans:  0b0  ->  Transparent transmission (default)
# ----------------------------------------
