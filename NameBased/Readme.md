To run the script

python parser.py
souffle CallGraph.dl


\**********************************************************************************

Following are the file names with dataflow facts


1.  Methods.facts
 Enlists methods across each class. Inherited methods have not been repeated
Format:
#Class		#Method1
Note: same name can be used for different methods in different classes. Hence the complete identification
of method is by method name listed across the class name in which it is defined. This format will be 
needed and followed in all representation of methods.


2.  MethodCall.facts
 Includes Caller-Callee relation
Format:
#Caller Name		#Caller Class		#Callee Name		#Callee Class



\************************************************************************************


Following are the important output from call graph algorithm

1. Reachable.csv
Enlists reachable methods as per the algorithm


\*************************************************************************************************************

To Enter Data Flow facts

1.  To enter new Methods
	-Enter data in Methods
	Format
	#Class name		#Method1	#Method2	...

2. To enter Method Calls
	-Enter data in MethodCall.facts
	Format:
	#Caller Method name	#Caller Method Class	#Called Method name	#Static Class of object method is being called on


Note: Dataflow facts have been entered manually.