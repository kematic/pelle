# 1 SOF
# 11 ID
# 1 RTR
# 1 IDE
# 1 r0
# 4 DLC (number of bytes)
# 0-64 DATA
# 15 CRC
# 1 delimiter
# 1 ACK
# 1 delimiter
# 7 EOF
from datetime import *
from collections import defaultdict

module = defaultdict(lambda: defaultdict())


def map_can(node_id, data):
    hex_id = hex(node_id)
    #
    # Checks for Module 0 related canbus information
    #
    # Telegrams from module to panel
    if hex_id[4] == '0' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN02'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN03'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN04'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN06'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN07'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN08'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN10'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN11'] = 'TBD'
            module['{}'.format(hex_id[4])]['IN12'] = 'TBD'
    # Telegrams from panel to module.
    elif hex_id[4] == '0' and hex_id[3] == '4':
        # Telegram #1
        if hex_id[2] == '2':
            module['576']['01'] = 'TBD'
            module['576']['23'] = 'TBD'
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['832']['45'] = 'TBD'
            module['832']['67'] = 'TBD'
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1088']['45'] = 'TBD'
            module['1088']['67'] = 'TBD'
        elif hex_id[2] == '5':
            module['1344']['01'] = 'TBD'
            module['1344']['23'] = 'TBD'
            module['1344']['45'] = 'TBD'
            module['1344']['67'] = 'TBD'
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module 1 related information
    #
    # Telegrams from module to panel.
    if hex_id[4] == '1' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '1' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['577']['01'] = 'TBD'
            module['577']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['833']['45'] = 'TBD'
            module['833']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1089']['45'] = 'TBD'
            module['1089']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1345']['01'] = 'TBD'
            module['1345']['23'] = 'TBD'
            module['1345']['45'] = 'TBD'
            module['1345']['67'] = 'TBD'
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    # Checks for Module 2 related information
    if hex_id[4] == '2' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '2' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['578']['01'] = 'TBD'
            module['578']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['834']['45'] = 'TBD'
            module['834']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1090']['45'] = 'TBD'
            module['1090']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1346']['01'] = 'TBD'
            module['1346']['23'] = 'TBD'
            module['1346']['45'] = 'TBD'
            module['1346']['67'] = 'TBD'
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module 3 related information
    #
    # Telegrams from module to panel.
    if hex_id[4] == '3' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '3' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['579']['01'] = 'TBD'
            module['579']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['835']['45'] = 'TBD'
            module['835']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1091']['45'] = 'TBD'
            module['1091']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1347']['01'] = 'TBD'
            module['1347']['23'] = 'TBD'
            module['1347']['45'] = 'TBD'
            module['1347']['67'] = 'TBD'
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module 4 related information
    #
    # Telegrams from module to panel.
    if hex_id[4] == '4' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '4' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['580']['01'] = 'TBD'
            module['580']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['836']['45'] = 'TBD'
            module['836']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1092']['45'] = 'TBD'
            module['1092']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1348']['01'] = 'TBD'
            module['1348']['23'] = 'TBD'
            module['1348']['45'] = 'TBD'
            module['1348']['67'] = 'TBD'
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module 5 related information
    #
    # Telegrams from module to panel.
    if hex_id[4] == '5' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '5' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['581']['01'] = 'TBD'
            module['581']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['837']['45'] = 'TBD'
            module['837']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1093']['45'] = 'TBD'
            module['1093']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1349']['01'] = 'TBD'
            module['1349']['23'] = 'TBD'
            module['1349']['45'] = 'TBD'
            module['1349']['67'] = 'TBD'
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module 6 related information
    #
    # Telegrams from module to panel.
    if hex_id[4] == '6' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
            # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '6' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['582']['01'] = 'TBD'
            module['582']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['838']['45'] = 'TBD'
            module['838']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1094']['45'] = 'TBD'
            module['1094']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1350']['01'] = 'TBD'
            module['1350']['23'] = 'TBD'
            module['1350']['45'] = 'TBD'
            module['1350']['67'] = 'TBD'
        # Telegram #7
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module 7 related information
    #
    # Telegrams from module to panel.
    if hex_id[4] == '7' and hex_id[3] == 'c':
        # Telegram #1
        if hex_id[2] == '1':
            module['{}'.format(hex_id[4])]['01'] = 'TBD'
            module['{}'.format(hex_id[4])]['23'] = 'TBD'
            module['{}'.format(hex_id[4])]['45'] = 'TBD'
            module['{}'.format(hex_id[4])]['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['{}'.format(hex_id[4])]['IN01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN03'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN04'] = '{}'.format(__bytes2int(data[7], data[6]))
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['IN05'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN06'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN07'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN08'] = '{}'.format(__bytes2int(data[7], data[6]))
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['IN09'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['IN10'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['{}'.format(hex_id[4])]['IN11'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['{}'.format(hex_id[4])]['IN12'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '7' and hex_id[3] == '4':
        # Telegram #2
        if hex_id[2] == '2':
            module['583']['01'] = 'TBD'
            module['583']['23'] = 'TBD'
        # Telegram #3
        elif hex_id[2] == '3':
            module['{}'.format(hex_id[4])]['AO01'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO02'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['839']['45'] = 'TBD'
            module['839']['67'] = 'TBD'
        # Telegram #4
        elif hex_id[2] == '4':
            module['{}'.format(hex_id[4])]['AO03'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['{}'.format(hex_id[4])]['AO04'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['1095']['45'] = 'TBD'
            module['1095']['67'] = 'TBD'
        # Telegram #5
        elif hex_id[2] == '5':
            module['1351']['01'] = 'TBD'
            module['1351']['23'] = 'TBD'
            module['1351']['45'] = 'TBD'
            module['1351']['67'] = 'TBD'
        # Telegram #7
        elif hex_id[2] == '7':
            module['{}'.format(hex_id[4])]['comm'] = datetime.now() + timedelta(seconds=2)
    #
    # Checks for Module Lambda related information
    #
    # Telegrams from module to panel
    if hex_id[4] == '0' and hex_id[3] == 'd':
        # Telegram #1
        if hex_id[2] == '1':
            module['lambda']['01'] = 'TBD'
            module['lambda']['23'] = 'TBD'
            module['lambda']['45'] = 'TBD'
            module['lambda']['67'] = 'TBD'
        # Telegram #2
        elif hex_id[2] == '2':
            module['lambda']['amps'] = '{}'.format(__bytes2int(data[1], data[0]))
            module['lambda']['probe'] = '{}'.format(__bytes2int(data[3], data[2]))
            module['lambda']['vgnd'] = '{}'.format(__bytes2int(data[5], data[4]))
            module['lambda']['oxygen'] = '{}'.format(__bytes2int(data[7], data[6]))
    # Telegrams from panel to module.
    elif hex_id[4] == '0' and hex_id[3] == '5':
        # Telegram #2
        if hex_id[2] == '2':
            module['592']['01'] = 'TBD'
            module['592']['23'] = 'TBD'
            module['592']['45'] = 'TBD'
            module['592']['67'] = 'TBD'
        # Telegram #7
        elif hex_id[2] == '7':
            module['lambda']['comm'] = datetime.now() + timedelta(seconds=2)

    if node_id == 0x201:  # How does this one fit in?!?
        module['513']['01'] = 'TBD'
        module['513']['blowerspeed'] = '{:0.1f}'.format(__bytes2int(data[3], data[2]) / 25)
        module['513']['45'] = 'TBD'
        module['513']['67'] = 'TBD'

    return module


def __bytes2int(x, y):
    return (x * 256) + y
