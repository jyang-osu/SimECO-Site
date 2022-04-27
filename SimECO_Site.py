
########################################################################
##                                                                    ##
##             Simple Ecosystem Model for Education (SimEco)          ##
##                         single site Version, Developed at          ##
##                                 Oklahoma State University          ##
##                                               April, 2022          ##
##                                                                    ##
########################################################################

from datetime import datetime
import time
import sys
import IO_read_namelist

def main():
	
	print("#####################################################")
	print("#   Simple Ecosystem Model for Education (SimEco)   #")
	print("#               single site Version                 #")
	print("#####################################################")
	print("")
	
	time_simulation_start = datetime.now()
	print("SimEco simulation starts at "+ str(time_simulation_start))
	time.sleep(1)
	
	##############################################################
	IO_read_namelist.read_namelist()
	
	




	
	
	time_simulation_end = datetime.now()
	print("SimEco simulation ends at "+ str(time_simulation_end))
	time_simulation_last = time_simulation_end - time_simulation_start
	print("SimEco simulation last "+ str(time_simulation_last))
	
main()








