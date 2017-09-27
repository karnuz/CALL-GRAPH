RTA

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


3. Classes.facts
 enlists all classes

4.  Immediate Subclass.facts
Enlists immediate inheritance relation
Format:
#Class 	#Subclass

5. Instantiated Classes
Enlists all instantiated classes
Format:
#Class Name

\************************************************************************************


Following are the important output from call graph algorithm

1. Reachable.csv
Enlists reachable methods as per the algorithm


2. staticLookup.csv
For each method call to e.m() checks for the applicable method that will be applied on the object e. As the 
desired method might not be defined agains the objectType(e) but one of its super class.
Format
#Static Class of object 		#Method Name		#Applicable Method Class	#Applicable Method Name(same as Method Name)


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

3. To enter new Classes (refer next for sub-classes)
	- Enter data in Classes.facts
	Format:
	#Class Name


4. To enter new SubClasses 
	- Enter data in SubClasses
	Format:
	#Class		#Subclass		#Subclass		#Subclass		...

5. To add instantiated classes
	-Enter data in InstantiatedClass.facts
	Format
	#Class Name
\********************************************************************************
Note: Dataflow facts have been entered manually.