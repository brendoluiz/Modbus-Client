import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from pymodbus.client import ModbusTcpClient

class MyNode(Node):
    
    def __init__(self):
        
        super().__init__("CLP")
        self.publisher1_ = self.create_publisher(Int16, "signal_feedback_driver1", 10)
        self.timer_= self.create_timer(0.5,self.Modbus_msg)
        self.modbus_client_ = ModbusTcpClient('192.168.0.10', 502)
        self.get_logger().info ('Conexão com CLP estabelicida')
        
        
    def Modbus_msg (self):
    
        addr1 = 1
        resultHold = self.modbus_client_.read_holding_registers(0,6)
        signal_feedback1 = (resultHold.registers[0])
        
        valor1 = signal_feedback1
        msg = Int16()
        
        self.modbus_client_.write_register(addr1, valor1)
        msg.data = signal_feedback1
        self.publisher1_.publish(msg)
        

def main():
    
    rclpy.init()
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()
