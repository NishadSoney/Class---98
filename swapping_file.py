#class pro2:
#    def swapfilestext():
#        
#        #flnm = input("Enter your file name(either file1 or file2)...")
#
#        data_a = open("file1.txt")
#        data_b = open("file2.txt")
#
#        fl1 = data_a.read()
#        fl2 = data_b.read()
#
#        data_a.write(fl2)
#        data_b.write(fl1)
#
#    swapfilestext()

class pro2wr:
    def swapfilestext1():
        flnm = input("Enter your file name(either file1 or file2)...")
        
        data_a = open("file1.txt",'w')
        data_b = open("file2.txt",'w')

        if(flnm == "file1"):
            print("this is file 2")

        if(flnm == "file2"):
            print("this is file 1")

    swapfilestext1()