class Components:
    def Server(self):
        d = {}
        print("###Server###")
        d['Rack Space'] = input("Rack Space: ")
        d['LAN Ports'] = input("LAN Connections: ")
        stor = input("Storage (local, iscsi, dac): ")
        if (stor == "iscsi"):
            d['iSCSI Ports'] = input("iSCSI Ports: ")
            conn = input("Connection Method (SFP, Cat6): ")
            if (conn == "SFP"):
                d['SFP Modules'] = d['iSCSI Ports']
            if (conn == "Cat6"):
                d['Cat6 Cables'] = d['iSCSI Ports']
        if (stor == "dac"):
            d['DAC Cables'] = input("DAC Connections: ")
        d['Labor'] = input("Labor Hrs: ")
        return d


    def SAN():
        print("SAN")

    def Switch():
        print("Switch")

    def WAP():
        print("WAP")

    def Application():
        print("Application")