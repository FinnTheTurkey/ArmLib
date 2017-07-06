import serial.tools.list_ports
import serial,time

class ArmError(Exception): pass


def findarm():
    
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "arduino" in p.description.lower():
            #print(p.device);
            ser = serial.Serial(p.device, 9600)
            #print("Start write")
            time.sleep(1)
            a = list('youarm:0;')
            for i in a:
                ser.write(i.encode());
                
            ser.flush();
            responce = "";
            #print("End write")
            time.sleep(1.2);
            responce = ser.readline();
            responce = ser.readline();
                    
            #print(responce);
            if responce == b'MeArm!\r\n':
                return Arm(p.device);
            #ser.close();
    raise ArmError("No Arms found!")
    
class Arm():
    
    def __init__(self,port):
        self.port = port
        
    def __repr__(self):
        return "<Arm on port '%s'>" % self.port
        
    def _send(self,command):
        try:
            ser = serial.Serial(self.port, 9600)
            err = False
        except:
            err = True
        if err:
            raise ArmError("Cannot find arm!");
        #print("Start write")
        #time.sleep(1)
        a = list(command)
        for i in a:
            ser.write(i.encode());
            
        ser.flush();
        responce = "";
        #print("End write")
        time.sleep(1.2);
        responce = ser.readline();
        responce = ser.readline();
        ser.close();
        return responce
    
        #print(responce);
    def setTurn(self,value):
        if value > 1000 or value < 0 or type(value) != int:
            raise ArmError("Value must be an int in between 0 and 1000");
        self._send("turn:%i;" % value)
        
    def setGripper(self,value):
        if value > 1000 or value < 0 or type(value) != int:
            raise ArmError("Value must be an int in between 0 and 1000");
        self._send("grip:%i;" % value)
        
    def setExtend(self,value):
        if value > 1000 or value < 0 or type(value) != int:
            raise ArmError("Value must be an int in between 0 and 1000");
        self._send("exte:%i;" % value)
        
    def setNod(self,value):
        if value > 1000 or value < 0 or type(value) != int:
            raise ArmError("Value must be an int in between 0 and 1000");
        self._send("nodd:%i;" % value)
        
    def reset(self):
        self._send("youarm:0;")
