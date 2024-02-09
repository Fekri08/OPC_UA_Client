import tkinter as tk
from tkinter import ttk

import opclabs_quickopc

#import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *

class MyGUI:
    def __init__(self):
        # Creating the window
        self.root = tk.Tk()

        # setting the geometry of the window
        self.root.geometry("800x600")

        # set the window title
        self.root.title("OPC UA Client")

        #frame for entering the endpoint url of the opc server
        self.endpointframe= tk.Frame(self.root)

        self.endpointframe.columnconfigure(0, weight=1)
        self.endpointframe.columnconfigure(1, weight=1)

        self.endpointLabel = tk.Label(self.endpointframe, text='EndPoint:', font=('Arial', 14))
        self.endpointLabel.grid(row=0, column=0)

        self.endpointEntry = tk.Entry(self.endpointframe, width=60)
        self.endpointEntry.grid(row=0, column=1, sticky='w')

        self.endpointframe.pack(fill='x', pady=20)


        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.separator.pack(fill='x')

        #frame for entering the nodeID to be read
        self.nodeFrame = tk.Frame(self.root)

        self.nodeFrame.columnconfigure(0, weight=1)
        self.nodeFrame.columnconfigure(1, weight=1)
        self.nodeFrame.columnconfigure(2, weight=1)

        self.nodeLabel = tk.Label(self.nodeFrame, text='NodeID:', font=('Arial', 14))
        self.nodeLabel.grid(row=0, column=0)

        self.nodeSpacetxt = tk.Label(self.nodeFrame, text='Namespace:', font=('Arial', 12))
        self.nodeSpacetxt.grid(row=0, column=1)

        self.nodeSpaceEntry = tk.Entry(self.nodeFrame, width=20)
        self.nodeSpaceEntry.grid(row=0, column=2, sticky='w')

        self.nodeNametxt = tk.Label(self.nodeFrame, text='Name:', font=('Arial', 12))
        self.nodeNametxt.grid(row=1, column=1, pady=10)

        self.nodeNameEntry = tk.Entry(self.nodeFrame, width=20)
        self.nodeNameEntry.grid(row=1, column=2, pady=10, sticky='w')

        self.nodeTypetxt = tk.Label(self.nodeFrame, text='Type:', font=('Arial', 12))
        self.nodeTypetxt.grid(row=2, column=1, pady=10)

        self.nodeTypeEntry = tk.Entry(self.nodeFrame, width=20)
        self.nodeTypeEntry.grid(row=2, column=2, pady=10, sticky='w')

        self.nodeFrame.pack(fill='x', pady=20)


        self.separator2 = ttk.Separator(self.root, orient='horizontal')
        self.separator2.pack(fill='x')



        #frame for entering the indexrange to be read
        self.indexFrame = tk.Frame(self.root)

        self.indexFrame.columnconfigure(0, weight=1)
        self.indexFrame.columnconfigure(1, weight=1)
        self.indexFrame.columnconfigure(2, weight=1)

        self.indexLabel = tk.Label(self.indexFrame, text='Index Range:', font=('Arial', 14))
        self.indexLabel.grid(row=0, column=0)

        self.indexFirstTxt = tk.Label(self.indexFrame, text='First index:', font=('Arial', 12))
        self.indexFirstTxt.grid(row=0, column=1)

        self.indexFirstEntry = tk.Entry(self.indexFrame, width=20)
        self.indexFirstEntry.grid(row=0, column=2, sticky='w')

        self.indexLastTxt = tk.Label(self.indexFrame, text='Last index:', font=('Arial', 12))
        self.indexLastTxt.grid(row=1, column=1, pady=10)

        self.indexLastEntry = tk.Entry(self.indexFrame, width=20)
        self.indexLastEntry.grid(row=1, column=2, pady=10, sticky='w')

        self.indexFrame.pack(fill='x', pady=20)


        self.separator3 = ttk.Separator(self.root, orient='horizontal')
        self.separator3.pack(fill='x')

        # output frame

        self.outputFrame = tk.Frame(self.root)

        self.outputLabel = tk.Label(self.outputFrame, text='Results:', font=('Arial',14))
        self.outputLabel.grid(row=0, sticky='w', padx=80)

        self.outputButton = tk.Button(self.outputFrame, text='Get Results', font=('Arial', 12), width=20, command=self.opcfunc)
        self.outputButton.grid(row=0, padx=10)

        self.outputText = tk.Text(self.outputFrame, font=('Arial', 12))
        self.outputText.grid(row=1, padx=20, pady=10)

        self.outputFrame.pack(fill='x', pady=20)

        self.root.mainloop()

    def opcfunc (self):
        firstindex = int(self.indexFirstEntry.get())
        lastindex = int(self.indexLastEntry.get())
        if self.endpointEntry.get()=='':
            endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
        # or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
        # or 'https://opcua.demo-this.com:51211/UA/SampleServer/'
        else:
            endpointDescriptor = UAEndpointDescriptor(self.endpointEntry.get())

        # Instantiate the client object.
        client = EasyUAClient()

        # Obtain the value, indicating that just the elements 2 to 4 should be returned
        try:
            arrayValue = IEasyUAClientExtension.ReadValue(client,
                                                          endpointDescriptor,
                                                          UANodeDescriptor(
                                                              'nsu='+ self.nodeNameEntry.get() +' ;ns='+ self.nodeSpaceEntry.get() + ';i=' + self.nodeTypeEntry.get()),
                                                          # Data.Static.Array.Int32Value
                                                          UAIndexRangeList.OneDimension(firstindex, lastindex))
        except UAException as uaException:
            print('*** Failure: ' + uaException.GetBaseException().Message)
            exit()

        # Dispaly results.
        self.outputText.delete("1.0", tk.END)
        for i, elementValue in enumerate(arrayValue):
            print('arrayValue[', i, ']: ', elementValue, sep='')
            self.outputText.insert(tk.END, ('arrayValue[' + str(i) + ']: '+ str(elementValue) +'\n'))
        print()
        print('Finished.')
        self.outputText.insert(tk.END, "Finished.")

MyGUI()