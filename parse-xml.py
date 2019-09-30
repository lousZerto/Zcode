#!/usr/bin/python3
#
#  SCRIPT NAME: parse-xml.py
#
#  PURPOSE: To extact data from a Zerto VPG export XML file into a legible CSV file
#
#  PARAMETER FILE: N/A
#
#  INPUT FILE: N/A
#
#  CALLED SCRIPTS: N/A
#
#  IMPORTED MODULES: xml_elements_long.py
#
#  SCRIPT USAGE: parse-xml.py ExportedSettings_date_time.xml
#
#  UPDATE HISTORY:
#        DATE               AUTHOR              UPDATE DESCRIPTION
#     05.09.2019       Lou Sassani            Initial script creation
#     30.09.2019       Lou Sassani            Hit an issue with a different XML export file which was causing
#                                             the ProcessXMLfile sub-routine to prematurely close the temp file.
#                                             I've removed the file close function in the sub-routine ProcessXMLfile
#
#
#                                              Written By: LOU SASSANI,
#                                                      Systems Engineer
#                                                      AsiaPacific,
#                                                      Copyright Zerto Corporation
#                                              Email:  lou.sassani@zerto.com
#     Legal Disclaimer:
#
#     ----------------------
#     This script is an example script and is not supported under any Zerto support program or service.
#
#     The author and Zerto further disclaim all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for
#     a particular purpose.
#
#     In no event shall Zerto, its authors or anyone else involved in the creation, production or delivery of the scripts be liable for any damages whatsoever
#     (including, withoutlimitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) 
#     arising out of the use of or the inability to use the sample scripts or documentation, even if the author or Zerto has been advised of the possibility
#     of such damages.  The entire risk arising out of the use or performance of the sample scripts and documentation remains with you.
#
## -- Set Global Veriables
#
import sys, os, re
Script_Version = "0.0.002"
#Script_Name = sys.argv[0]
Script_Name = os.path.basename(__file__)
global returncode
returncode = 0
#
## - Process filename passed
#
def ProcessPARAMETERS():
    global infile
    parmlen = len(sys.argv)
    if parmlen == 2:
       infile = sys.argv[1]
    else:
       print ("Script requires an XML Filename to process")
       print ("Exmaple:")
       print (Script_Name, "(Filename to process)")
       exit(4)
#
## - This sub-routine will generate the XML data in a raw CSV appened format
#
def ProcessXMLfileCSVRaw():
    #
    ## - Import known schemas
    #
    import xml_elements_long as EL
    #
    ## - import XML Element tree structure
    #
    import xml.etree.ElementTree as ET
    #
    ## - Zerto VPG export XML file
    #
    tree = ET.parse(infile)
    root = tree.getroot()
    #
    ## - Root element
    #
    for S in root.iter(EL.S006):
        for C0 in S.getchildren():
            cc=str(C0)
            s0,s1 = cc.split("}")
            s0,S1 = s1.split("'")
            print ("\n","Root->", s0,",",C0.text,",", end="")
            #
            ## - First Child Element
            #
            for C1 in C0.getchildren():
                cc=str(C1)
                s0,s1 = cc.split("}")
                s0,S1 = s1.split("'")
                print (s0,",",C1.text,",", end="")
                #
                ## - First Child Element
                #
                for C2 in C1.getchildren():
                    cc=str(C2)
                    s0,s1 = cc.split("}")
                    s0,S1 = s1.split("'")
                    print (s0,",",C2.text,",", end="")
                    #
                    ## - Second Child Element
                    #
                    for C3 in C2.getchildren():
                        cc=str(C3)
                        s0,s1 = cc.split("}")
                        s0,S1 = s1.split("'")
                        print (s0,",",C3.text,",", end="")
                        #
                        ## - Third Child Element
                        #
                        for C4 in C3.getchildren():
                            cc=str(C4)
                            s0,s1 = cc.split("}")
                            s0,S1 = s1.split("'")
                            print (s0,",",C4.text,",", end="")
                            #
                            ## - Forth Child Element
                            #
                            for C5 in C4.getchildren():
                                cc=str(C5)
                                s0,s1 = cc.split("}")
                                s0,S1 = s1.split("'")
                                print (s0,",",C5.text,",", end="")
                                #
                                ## - Fifth Child Element
                                #
                                for C6 in C5.getchildren():
                                    cc=str(C6)
                                    s0,s1 = cc.split("}")
                                    s0,S1 = s1.split("'")
                                    print (s0,",",C6.text,",", end="")
                                    #
                                    ## - Sixth Child Element
                                    #
                                    for C7 in C6.getchildren():
                                        cc=str(C7)
                                        s0,s1 = cc.split("}")
                                        s0,S1 = s1.split("'")
                                        print (s0,",",C7.text,",", end="")
                                        #
                                        ## - Seventh Child Element
                                        #
                                        for C8 in C7.getchildren():
                                            cc=str(C8)
                                            s0,s1 = cc.split("}")
                                            s0,S1 = s1.split("'")
                                            print (s0,",",C8.text,",", end="")
                                            #
                                            ## - Eighth Child Element
                                            #
                                            for C9 in C8.getchildren():
                                                cc=str(C9)
                                                s0,s1 = cc.split("}")
                                                s0,S1 = s1.split("'")
                                                print (s0,",",C9.text,",", end="")
                                                #
                                                ## - Ninth Child Element
                                                #
                                                for C10 in C9.getchildren():
                                                    cc=str(C10)
                                                    s0,s1 = cc.split("}")
                                                    s0,S1 = s1.split("'")
                                                    print (s0,",",C10.text,",", end="")
#
## - This sub-routine will generate the XML data in formatted CSV format 
#
def ProcessXMLfile():
    #
    ## - Generate a temp file name
    #
    import tempfile
    global VMFtemp
    VMFtemp = tempfile.NamedTemporaryFile(prefix="vpg")
    #
    ## - Import known schemas
    #
    import xml_elements_long as EL
    #
    ## - import XML Element tree structure
    #
    import xml.etree.ElementTree as ET
    #
    ## - Zerto VPG export XML file
    #
    tree = ET.parse(infile)
    root = tree.getroot()
    #
    ## - Root element
    #
    global VPGdata
    VWF = open(VMFtemp.name,"w+")
    VPGcount=0
    VPGdata=[]
    for S in root.iter(EL.S006):
        for C0 in S.getchildren():
            cc=str(C0)
            s0,s1 = cc.split("}")
            s0,S1 = s1.split("'")
            VPGcount+=1
            VPGdata=("VPGN"+str(VPGcount),str(s0),str(C0.text))
            VWF.write(str(VPGdata))
            VWF.write("\n")
            #
            ## - First Child Element
            #
            for C1 in C0.getchildren():
                cc=str(C1)
                s0,s1 = cc.split("}")
                s0,S1 = s1.split("'")
                VPGdata=("VPGN"+str(VPGcount),str(s0),str(C1.text))
                VWF.write(str(VPGdata))
                VWF.write("\n")
                #
                ## - First Child Element
                #
                for C2 in C1.getchildren():
                    cc=str(C2)
                    s0,s1 = cc.split("}")
                    s0,S1 = s1.split("'")
                    VPGdata=("VPGN"+str(VPGcount),str(s0),str(C2.text))
                    VWF.write(str(VPGdata))
                    VWF.write("\n")
                    #
                    ## - Second Child Element
                    #
                    for C3 in C2.getchildren():
                        cc=str(C3)
                        s0,s1 = cc.split("}")
                        s0,S1 = s1.split("'")
                        VPGdata=("VPGN"+str(VPGcount),str(s0),str(C3.text))
                        VWF.write(str(VPGdata))
                        VWF.write("\n")
                        if s0 == "Name":
                            VPGdata = ("VPGN"+str(VPGcount),"VPG-Name=", str(C3.text))
                            VWF.write(str(VPGdata))
                            VWF.write("\n")
                        #
                        ## - Third Child Element
                        #
                        for C4 in C3.getchildren():
                            cc=str(C4)
                            s0,s1 = cc.split("}")
                            s0,S1 = s1.split("'")
                            VPGdata=("VPGN"+str(VPGcount),str(s0),str(C4.text))
                            VWF.write(str(VPGdata))
                            VWF.write("\n")
                            #
                            ## - Forth Child Element
                            #
                            for C5 in C4.getchildren():
                                cc=str(C5)
                                s0,s1 = cc.split("}")
                                s0,S1 = s1.split("'")
                                VPGdata=("VPGN"+str(VPGcount),str(s0),str(C5.text))
                                VWF.write(str(VPGdata))
                                VWF.write("\n")
                                #
                                ## - Fifth Child Element
                                #
                                for C6 in C5.getchildren():
                                    cc=str(C6)
                                    s0,s1 = cc.split("}")
                                    s0,S1 = s1.split("'")
                                    VPGdata=("VPGN"+str(VPGcount),str(s0),str(C6.text))
                                    VWF.write(str(VPGdata))
                                    VWF.write("\n")
                                    #
                                    ## - Sixth Child Element
                                    #
                                    for C7 in C6.getchildren():
                                        cc=str(C7)
                                        s0,s1 = cc.split("}")
                                        s0,S1 = s1.split("'")
                                        VPGdata=("VPGN"+str(VPGcount),str(s0),str(C7.text))
                                        VWF.write(str(VPGdata))
                                        VWF.write("\n")
                                        #
                                        ## - Seventh Child Element
                                        #
                                        for C8 in C7.getchildren():
                                            cc=str(C8)
                                            s0,s1 = cc.split("}")
                                            s0,S1 = s1.split("'")
                                            VPGdata=("VPGN"+str(VPGcount),str(s0),str(C8.text))
                                            VWF.write(str(VPGdata))
                                            VWF.write("\n")
                                            #
                                            ## - Eighth Child Element
                                            #
                                            for C9 in C8.getchildren():
                                                cc=str(C9)
                                                s0,s1 = cc.split("}")
                                                s0,S1 = s1.split("'")
                                                VPGdata=("VPGN"+str(VPGcount),str(s0),str(C9.text))
                                                VWF.write(str(VPGdata))
                                                VWF.write("\n")
                                                #
                                                ## - Ninth Child Element
                                                #
                                                for C10 in C9.getchildren():
                                                    cc=str(C10)
                                                    s0,s1 = cc.split("}")
                                                    s0,S1 = s1.split("'")
                                                    VPGdata=("VPGN"+str(VPGcount),str(s0),str(C10.text))
                                                    VWF.write(str(VPGdata))
                                                    VWF.write("\n")
        #
        ## - Close File 
        #
        #VWF.close()
#
## - This sub-routine will Process the XML data into a formatted CSV file
#
def ProcessXMLfileCSV():
    #
    ## - Create Array Name
    #
    VPGNameArray = []
    #
    ## - Generate CSV name
    #
    global CSVFileName
    CSVFileName = (str(infile)+".csv")
    CSV = open(CSVFileName,"w")
    #
    ## - Open XML data extra for reading
    #
    VWF = open(VMFtemp.name,"rt")
    VPGDetails = VWF.readlines()
    for VPGlines in VPGDetails:
        VPGnum, VPGfield, FieldDetails = VPGlines.split(",")
        if "VPG-Name" in VPGfield:
            VPGnum = VPGnum.replace("'","")
            VPGnum = VPGnum.replace("(","")
            FieldDetails = FieldDetails.replace("'","")
            VPGAddToArray = (VPGnum+":"+FieldDetails)
            VPGNameArray.append(VPGAddToArray)
    VPGnameToProcess = VPGNameArray
    CSVdata=("VPGname,"+"VPGfield,"+"FieldDetails")
    CSV.write(str(CSVdata))
    CSV.write("\n")
    for VPGnames in VPGnameToProcess:
        global VPGname
        VPGnumToFind, VPGname = VPGnames.split(":")
        VPGname, x = VPGname.split(")")
        VWF.seek(0,0)
        VPGDetails = VWF.readlines()
        for CSVBuild in VPGDetails:
            VPGnum, VPGfield, FieldDetails = CSVBuild.split(",")
            if VPGnumToFind in VPGnum:
                FieldDetails = FieldDetails.replace(")","")
                CSVdata=(VPGname+","+VPGfield+","+FieldDetails)
                if "VPG-Name" not in VPGfield:
                    CSV.write(str(CSVdata))
    #
    ## - Close File
    #
    VWF.close()
#
##
### -- Mainline Processing
##
#
ProcessPARAMETERS()
ProcessXMLfile()
ProcessXMLfileCSV()
#ProcessXMLfileCSVRaw()
print ("CSV filename", CSVFileName, "Created")
