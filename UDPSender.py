
"""
Created on Mon Dec 17  10:20:15 2018

@author: mshaik
"""
import socket
import time


destination_IP = "127.0.0.1"
#destination_IP = "192.168.1.51"
destination_PORT = 2809
trys_counter = 100
loop_counter = 0
hil_result  = 0
one_second = 1
five_seconds = 5
ten_seconds = 10
one_minute_delay  = 60
two_minute_delay  = 2*60
three_minute_delay  = 3*60
five_minute_delay  = 5*60
one_hour_delay  = 60*60

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create UDP socket'

def sendUDP(MESSAGE):
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(MESSAGE, (destination_IP, destination_PORT))

  # Reference Enum TestType { None_T = 0,
                 # TC_0007_Check_FR_Message_Period_Test = 1,
                 # TC_0008_SW_Version_Test = 2,
                 # TC_0010_SW_Latency_Test = 3,
                 # TC_0012_BlockId_Incremental_Test = 4,
                 # TC_0013_HC_Functionality_Test = 5, //Heating cleaning functionality test
                 # TC_0014_HC_Activ_Deactiv_Test = 6, //Heating cleaning Activation and de activation test
                 # TC_0015_HC_Sequence_Test = 7,     //Heating cleaning Activation and de activation test
                 # TC_0016_NVM_Read_Write_DID_Test = 8,
                 # TC_0017_Check_ShutDown_Behaviour_Test = 9,
                 # TC_0018_Check_Startup_Behaviour_Test = 10,
                 # TC_0019_Motor_Speed_Test = 11,
                 # TC_0020_Check_DTCs_Test = 12,
                 # TC_0021_Check_CPU_Load_Test = 13,
                 # TC_0023_Check_ECU_Behaviour_AfterOneHourRun_Test = 14,
                 # TC_xxxx_Enable_Development_Messages = 15,
                 # TC_xxxx_Disable_Error_Classes = 16,
                 # TC_xxxx_Clear_DTCs = 17 
                # };

if __name__ == "__main__":
    start_measurement 					  	= '43414e6f65464458010000010080000004000100'.decode('hex')
    stop_measurement 					  	= '43414e6f65464458010000010080000004000200'.decode('hex')
    status_request 						  	= '43414e6f65464458010000010080000004000A00'.decode('hex')
    get_version 						  	= '43414e6f6546445801000001008000000C0005001200040001000000'.decode('hex')
    TC_0007_Check_FR_Message_Period_Test  	= '43414e6f6546445801000001008000000C0005001200040001000000'.decode('hex')
    TC_0008_SW_Version_Test 			  	= '43414e6f6546445801000001008000000C0005001200040002000000'.decode('hex')
    TC_0010_SW_Latency_Test 			  	= '43414e6f6546445801000001008000000C0005001200040003000000'.decode('hex')
    TC_0012_BlockId_Incremental_Test 	  	= '43414e6f6546445801000001008000000C0005001200040004000000'.decode('hex')
    TC_0013_HC_Functionality_Test 		  	= '43414e6f6546445801000001008000000C0005001200040005000000'.decode('hex')
    TC_0014_HC_Activ_Deactiv_Test 		  	= '43414e6f6546445801000001008000000C0005001200040006000000'.decode('hex')
    TC_0015_HC_Sequence_Test 			  	= '43414e6f6546445801000001008000000C0005001200040007000000'.decode('hex')
    TC_0016_NVM_Read_Write_DID_Test 	  	= '43414e6f6546445801000001008000000C0005001200040008000000'.decode('hex')
    TC_0017_Check_ShutDown_Behaviour_Test 	= '43414e6f6546445801000001008000000C0005001200040009000000'.decode('hex')
    TC_0018_Check_Startup_Behaviour_Test  	= '43414e6f6546445801000001008000000C000500120004000A000000'.decode('hex')
    TC_0019_Motor_Speed_Test 				= '43414e6f6546445801000001008000000C000500120004000B000000'.decode('hex')
    TC_0020_Check_DTCs_Test 				= '43414e6f6546445801000001008000000C000500120004000C000000'.decode('hex')
    TC_0021_Check_CPU_Load_Test 			= '43414e6f6546445801000001008000000C000500120004000D000000'.decode('hex')
    TC_0023_Check_ECU_Behaviour_AfterOneHourRun_Test =   '43414e6f6546445801000001008000000C000500120004000E000000'.decode('hex')
    TC_xxxx_Enable_Development_Messages 			 =   '43414e6f6546445801000001008000000C000500120004000F000000'.decode('hex')
    TC_xxxx_Disable_Error_Classes 		=     '43414e6f6546445801000001008000000C0005001200040010000000'.decode('hex')
    TC_xxxx_Clear_DTCs 					=     '43414e6f6546445801000001008000000C0005001200040011000000'.decode('hex')
    Write_Expected_Sw_Version 			=     '43414e6f6546445801000001008000000C0005001300040041373135'.decode('hex')
    Write_Test_Status_Undefined			=     '43414e6f6546445801000001008000000C0005001400040002000000'.decode('hex')
    Read_Test_Status					=     '43414e6f654644580100000100800000060006001400'.decode('hex')	
	
    Klemme15Cycle ='43414e6f6546445801000001008000000C0005001200040009000000'.decode('hex')

    sendUDP(start_measurement)
  

    while(trys_counter>0):
        sendUDP(status_request)
        data, addr = s.recvfrom(1024)
        print 'data[20]:' , ord(data[20]), 'loop_counter: ', loop_counter
        trys_counter += 1
        if(ord(data[20])!= 3):
            trys_counter -= 1
            #hil_result = 1
        else:
            trys_counter = 0
            hil_result = 1
        loop_counter += 1
        time.sleep(1)
    print 'CANoe: Measurement is running script waiting for 2 minutes run before start test Please reset the power for better test performence . . . '
    time.sleep(1*10)
    if hil_result == 1:
	    ########## TC_0018_Check_Startup_Behaviour_Test ##################################################
        print 'TC_0018_Check_Startup_Behaviour_Test'
        sendUDP(TC_0018_Check_Startup_Behaviour_Test)
        time.sleep(three_minute_delay)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        #print (data)
        #print 'Check Check_Startup_Behaviour_Test Result:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_0018_Check_Startup_Behaviour_Test:Pass'
        else:
            print 'TC_0018_Check_Startup_Behaviour_Test:Fail'
		
		########## TC_xxxx_Disable_Error_Classes ##################################################
        print 'TC_xxxx_Disable_Error_Classes'
        sendUDP(TC_xxxx_Disable_Error_Classes)
        time.sleep(five_seconds)
        sendUDP(Read_Test_Status)
        data = s.recvfrom(1024)
        #print (data)
        #print 'Check Check_Startup_Behaviour_Test Result:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_xxxx_Disable_Error_Classes:Pass'
        else:
            print 'TC_xxxx_Disable_Error_Classes:Fail'
        ########## TC_xxxx_Clear_DTCs ##################################################
        print 'TC_xxxx_Clear_DTCs'
        sendUDP(TC_xxxx_Clear_DTCs)
        time.sleep(five_seconds)
        sendUDP(Read_Test_Status)
        data = s.recvfrom(1024)
        #print (data)
        #print 'Check Check_Startup_Behaviour_Test Result:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_xxxx_Clear_DTCs:Pass'
        else:
            print 'TC_xxxx_Clear_DTCs:Fail'
        ########## TC_xxxx_Enable_Development_Messages ##################################################
        print 'TC_xxxx_Enable_Development_Messages'
        sendUDP(TC_xxxx_Enable_Development_Messages)
        time.sleep(five_seconds)
        ########## TC_0020_Check_DTCs_Test ##################################################
        #print 'TC_0020_Check_DTCs_Test'
        sendUDP(TC_0020_Check_DTCs_Test)
        time.sleep(10)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        #print (data)
        #print 'Check DTCs Result:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_0020_Check_DTCs_Test:Pass'
        else:
            print 'TC_0020_Check_DTCs_Test:Fail'
		
        print 'TC_xxxx_Disable_Error_Classes'
        sendUDP(TC_xxxx_Disable_Error_Classes)
        time.sleep(five_seconds)
		
		########## TC_0008_SW_Version_Test ##################################################
        #print 'TC_0008_SW_Version_Test'
        sendUDP(Write_Expected_Sw_Version)
        time.sleep(one_second)
        sendUDP(TC_0008_SW_Version_Test)
        time.sleep(five_seconds)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        #print (data)
        #print 'SW Version Test Result:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
           print 'TC_0008_SW_Version_Test:Pass'
        else:
           print 'TC_0008_SW_Version_Test:Fail'
        
		########## TC_0019_Motor_Speed_Test ##################################################
        #print 'TC_0019_Motor_Speed_Test'
        sendUDP(TC_0019_Motor_Speed_Test)
        time.sleep(10)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        #print (data)
        #print 'Motor Speed Test Result:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_0019_Motor_Speed_Test:Pass'
        else:
            print 'TC_0019_Motor_Speed_Test:Fail'
		########## TC_0010_SW_Latency_Test ##################################################
        #print 'TC_0010_SW_Latency_Test'
        #sendUDP(TC_0010_SW_Latency_Test)
        time.sleep(one_second)
        print 'TC_0010_SW_Latency_Test:Not implemented'
		
		########## TC_0012_BlockId_Incremental_Test ##################################################
        #print 'TC_0012_BlockId_Incremental_Test'
        sendUDP(TC_0012_BlockId_Incremental_Test)
        time.sleep(two_minute_delay)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        #print (data)
        #print 'NVM Read write DID:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_0012_BlockId_Incremental_Test:Pass'
        else:
            print 'TC_0012_BlockId_Incremental_Test:Fail'
		
		########## TC_0013_HC_Functionality_Test ##################################################
        #print 'TC_0013_HC_Functionality_Test'
        #sendUDP(TC_0013_HC_Functionality_Test)
        time.sleep(one_second)
        print 'TC_0013_HC_Functionality_Test:Not implemented'
		########## TC_0014_HC_Activ_Deactiv_Test ##################################################
        #print 'TC_0014_HC_Activ_Deactiv_Test'
        #sendUDP(TC_0014_HC_Activ_Deactiv_Test)
        time.sleep(one_second)
        print 'TC_0014_HC_Activ_Deactiv_Test:Not implemented'
		########## TC_0015_HC_Sequence_Test ##################################################
        #print 'TC_0015_HC_Sequence_Test'
        #sendUDP(TC_0015_HC_Sequence_Test)
        time.sleep(one_second)
        print 'TC_0015_HC_Sequence_Test:Not implemented'
        ########## TC_0021_Check_CPU_Load_Test ##################################################
        #print 'TC_0021_Check_CPU_Load_Test'
        #sendUDP(TC_0021_Check_CPU_Load_Test)
        #time.sleep(three_minute_delay)
        #sendUDP(Read_Test_Status)
        #time.sleep(one_second)
        #data = s.recvfrom(1024)
        #if ord(data[0][40]) == 1:
            #print 'TC_0021_Check_CPU_Load_Test:Pass'
        #else:
            #print 'TC_0021_Check_CPU_Load_Test:Fail'
        ########## TC_0007_Check_FR_Message_Period_Test ##################################################
        sendUDP(TC_0007_Check_FR_Message_Period_Test)
        time.sleep(three_minute_delay)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        if ord(data[0][40]) == 1:
            print 'TC_0007_Check_FR_Message_Period_Test:Pass'
        else:
            print 'TC_0007_Check_FR_Message_Period_Test:Fail'
		########## TC_0016_NVM_Read_Write_DID_Test ##################################################
        print 'TC_0016_NVM_Read_Write_DID_Test'
        sendUDP(TC_0016_NVM_Read_Write_DID_Test)
        time.sleep(two_minute_delay)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        print (data)
        print 'NVM Read write DID:' , ord(data[0][40])
        if ord(data[0][40]) == 1:
            print 'TC_0016_NVM_Read_Write_DID_Test:Pass'
        else:
            print 'TC_0016_NVM_Read_Write_DID_Test:Fail'
		########## TC_0023_Check_ECU_Behaviour_AfterOneHourRun_Test ##################################################
        #sendUDP(TC_0023_Check_ECU_Behaviour_AfterOneHourRun_Test)
        #time.sleep(one_hour_delay)
        #sendUDP(Read_Test_Status)
        #time.sleep(one_second)
        #data = s.recvfrom(1024)
        #if ord(data[0][40]) == 1:
            #print 'TC_0023_Check_ECU_Behaviour_AfterOneHourRun_Test:Pass'
        #else:
            #print 'TC_0023_Check_ECU_Behaviour_AfterOneHourRun_Test:Fail'
		########## TC_0017_Check_ShutDown_Behaviour_Test ##################################################
        sendUDP(TC_0017_Check_ShutDown_Behaviour_Test)
        time.sleep(ten_seconds)
        sendUDP(Read_Test_Status)
        time.sleep(one_second)
        data = s.recvfrom(1024)
        if ord(data[0][40]) == 1:
            print 'TC_0017_Check_ShutDown_Behaviour_Test:Pass'
        else:
            print 'TC_0017_Check_ShutDown_Behaviour_Test:Fail'
		
		os.system('taskkill /IM CANoe64.exe /F')