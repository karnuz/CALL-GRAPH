XTA Analysis



To run the script

python parser.py
souffle CallGraph.dl





\**********************************************************************************

Following are the file names with dataflow facts

A. Classes.facts
 enlists all classes

B.  Immediate Subclass.facts
1. enlists immediate inheritance relation
Format:
#Class 	#Subclass

C.  Methods.facts
1. Enlists methods across each class. Inherited methods have not been repeated
Format:
#Class		#Method1
Note: same name can be used for different methods in different classes. Hence the complete identification
of method is by method name listed across the class name in which it is defined. This format will be 
needed and followed in all representation of methods.


D.  MethodCall.facts
1. Includes Caller-Callee relation
Format:
#Caller Name		#Caller Class		#Callee Name		#Callee Class


E.  Instantiated.facts
1. Enlists instantiated classes across methods, ie. each occurance of "new()" in method M,C (method with name M defined in class C)
Format:
#Method Name	#Method Class	#Instantiated Class

F.  FieldstaticType.facts
1.Enlists the fields of each class and the declared type of field
Format:
#Class Name		#Field		#StaticType of Field


G.  ParamTypes.facts
1. For each method with parameters, the static type of parameter is listed
Format:
#Method Name		#Method Class		#Parameter Type


H.  ReadField.facts
1. All read field operations are listed
#Reading method name		#Reading method Class		#Field Class	#Field Name

I.  ReturnType.facts
1. For all methods with return, enlists the declared return type
Format:
#Method Name	#Method Class	#declared return type

J.  WriteField.facts
1. Enlists all instances of writing of field
Formath:
#Writing method name		#Writing method class		#Field Class		#Field Name


\************************************************************************************




Following are the important output from call graph algorithm

1. Reachable.csv
Enlists reachable methods as per the algorithm

2. RelatedClasses.csv
Enlists Classes related to each method. This is used in the algorithm to check for possible reachable methods.
Format:
#Method		#Method Class		#Class related


3. staticLookup.csv
For each method call to e.m() checks for the applicable method that will be applied on the object e. As the 
desired method might not be defined agains the objectType(e) but one of its super class.
Format
#Static Class of object 		#Method Name		#Applicable Method Class	#Applicable Method Name(same as Method Name)

4. RelatedFieldClass.csv
Enlists what types can be associated with a field (c,x)


\*************************************************************************************************************

To Enter Data Flow facts
1. To enter new Classes (refer next for sub-classes)
	- Enter data in Classes.facts
	Format:
	#Class Name

2. To enter new SubClasses 
	- Enter data in SubClasses
	Format:
	#Class		#Subclass		#Subclass		#Subclass		...

3.  To enter new Methods
	-Enter data in Methods
	Format
	#Class name		#Method1	#Method2	...

4. To enter Method Calls
	-Enter data in MethodCall.facts
	Format:
	#Caller Method name	#Caller Method Class	#Called Method name	#Static Class of object method is being called on

5.   To enter instantiated class information
	-Enter data in instantiated
	Format
	#Instantiating method name	#Instantiating method's class	#type of instance (C of new C() )

6.  To enter Parameter Types
	-Enter data in ParamTypes
	Format:
	#Method Name		#Method Class		#Parameter type 1	#Parameter type 2	...

5.  To enter Static Field Types
	-Enter data in FieldstaticType.facts
	Format:
	#Class name		#Field Name		#static type of Field

6.  To enter Return Type
	-Enter dataa in ReturyType
	Format:
	#Method Name		#Method Class	#Return type 1		#Return type 2		...

7.  To enter Read Field instances
	-Enter data in ReadField.facts
	Format:
	#Name of Reading method	#Class of reading method	#Field class	#Field name

8.   To enter Write field instances
	-Enter data in WriteField.facts
	Format
	#Name of Writing method	#Class of writing method	#Field class	#Field name



\***********************************************************************************************

NOTE:  Dataflow facts are entered manually