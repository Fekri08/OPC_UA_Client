# this example shows how to read a range of values from an array

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# The TKinter library for GUI interface
import tkinter as tk

#import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *

endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
#or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
#or 'https://opcua.demo-this.com:51211/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain the value, indicating that just the elements 2 to 4 should be returned
try:
    arrayValue = IEasyUAClientExtension.ReadValue(client,
                                                  endpointDescriptor,
                                                  UANodeDescriptor('nsu=http://test.org/UA/Data/ ;ns=2;i=10305'), # Data.Static.Array.Int32Value
                                                  UAIndexRangeList.OneDimension(0,0) )
except UAException as uaException:
    print ('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

#Dispaly results.
for i, elementValue in enumerate(arrayValue):
    print ('arrayValue[', i, ']: ', elementValue, sep='')

print()
print('Finished.')


# Creating the window
root = tk.Tk()

# setting the geometry of the window
root.geometry("800x600")

# set the window title
root.title("OPC UA Client")

root.mainloop()