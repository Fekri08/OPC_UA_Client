import tkinter as tk
from tkinter import ttk


#import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *

def opcfunc():
    endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
    # or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
    # or 'https://opcua.demo-this.com:51211/UA/SampleServer/'

    # Instantiate the client object.
    client = EasyUAClient()

    # Obtain the value, indicating that just the elements 2 to 4 should be returned
    try:
        arrayValue = IEasyUAClientExtension.ReadValue(client,
                                                      endpointDescriptor,
                                                      UANodeDescriptor('nsu=http://test.org/UA/Data/ ;ns=2;i=10305'),
                                                      # Data.Static.Array.Int32Value
                                                      UAIndexRangeList.OneDimension(0, 0))
    except UAException as uaException:
        print('*** Failure: ' + uaException.GetBaseException().Message)
        exit()

    # Dispaly results.
    for i, elementValue in enumerate(arrayValue):
        print('arrayValue[', i, ']: ', elementValue, sep='')

    print()
    print('Finished.')


# Creating the window
root = tk.Tk()

# setting the geometry of the window
root.geometry("800x600")

# set the window title
root.title("OPC UA Client")

#frame for entering the endpoint url of the opc server
endpointframe= tk.Frame(root)

endpointframe.columnconfigure(0, weight=1)
endpointframe.columnconfigure(1, weight=1)

endpointLabel = tk.Label(endpointframe, text='EndPoint:', font=('Arial', 14))
endpointLabel.grid(row=0, column=0)

endpointEntry = tk.Entry(endpointframe, width=60)
endpointEntry.grid(row=0, column=1, sticky='w')

endpointframe.pack(fill='x', pady=20)


separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')

#frame for entering the nodeID to be read
nodeFrame = tk.Frame(root)

nodeFrame.columnconfigure(0, weight=1)
nodeFrame.columnconfigure(1, weight=1)
nodeFrame.columnconfigure(2, weight=1)

nodeLabel = tk.Label(nodeFrame, text='NodeID:', font=('Arial', 14))
nodeLabel.grid(row=0, column=0)

nodeSpacetxt = tk.Label(nodeFrame, text='Namespace:', font=('Arial', 12))
nodeSpacetxt.grid(row=0, column=1)

nodeSpaceEntry = tk.Entry(nodeFrame, width=20)
nodeSpaceEntry.grid(row=0, column=2, sticky='w')

nodeNametxt = tk.Label(nodeFrame, text='Name:', font=('Arial', 12))
nodeNametxt.grid(row=1, column=1, pady=10)

nodeNameEntry = tk.Entry(nodeFrame, width=20)
nodeNameEntry.grid(row=1, column=2, pady=10, sticky='w')

nodeTypetxt = tk.Label(nodeFrame, text='Type:', font=('Arial', 12))
nodeTypetxt.grid(row=2, column=1, pady=10)

nodeTypeEntry = tk.Entry(nodeFrame, width=20)
nodeTypeEntry.grid(row=2, column=2, pady=10, sticky='w')

nodeFrame.pack(fill='x', pady=20)


separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x')



#frame for entering the indexrange to be read
indexFrame = tk.Frame(root)

indexFrame.columnconfigure(0, weight=1)
indexFrame.columnconfigure(1, weight=1)
indexFrame.columnconfigure(2, weight=1)

indexLabel = tk.Label(indexFrame, text='Index Range:', font=('Arial', 14))
indexLabel.grid(row=0, column=0)

indexFirstTxt = tk.Label(indexFrame, text='First index:', font=('Arial', 12))
indexFirstTxt.grid(row=0, column=1)

indexFirstEntry = tk.Entry(indexFrame, width=20)
indexFirstEntry.grid(row=0, column=2, sticky='w')

indexLastTxt = tk.Label(indexFrame, text='Last index:', font=('Arial', 12))
indexLastTxt.grid(row=1, column=1, pady=10)

indexLastEntry = tk.Entry(indexFrame, width=20)
indexLastEntry.grid(row=1, column=2, pady=10, sticky='w')

indexFrame.pack(fill='x', pady=20)


separator3 = ttk.Separator(root, orient='horizontal')
separator3.pack(fill='x')

# output frame

outputFrame = tk.Frame(root)

outputLabel = tk.Label(outputFrame, text='Results:', font=('Arial',14))
outputLabel.grid(row=0, sticky='w', padx=80)

outputButton = tk.Button(outputFrame, text='Get Results', font=('Arial', 12), width=20)
outputButton.grid(row=0, padx=10)

outputText = tk.Text(outputFrame, font=('Arial', 12))
outputText.grid(row=1, padx=20, pady=10)

outputFrame.pack(fill='x', pady=20)

root.mainloop()