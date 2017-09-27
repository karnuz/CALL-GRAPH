# Call Graph construction Algorithms

This project implements different call graph construction algorithms described in [Scalable Propagation-Based Call Graph Construction
Algorithms](http://web.cs.ucla.edu/~palsberg/paper/oopsla00.pdf)


#RTA

## Run

To run the analysis

```
python parser.py
souffle CallGraph.dl
```

### DataFlow Facts Files Description

**1. Classes.facts**: Enlists all classes

Format: *#Class*

**2. Methods.facts**: Enlists methods across each class. Inherited methods have not been repeated.

Format: *#Class      #Method1*

**Note**: same name can be used for different methods in different classes. Hence the complete identification of method is by method name listed across the class name in which it is defined. This format will be needed and followed in all representation of methods.


**3.  MethodCall.facts**: Includes Caller-Callee relation

Format: *#Caller Name        #Caller Class       #Callee Name        #Callee Class*

3. Classes.facts
 enlists all classes

**4. Immediate Subclass.facts**:  Enlists immediate inheritance relation
 
Format: *#Class #Subclass*

**5. Instantiated.facts**: Enlists instantiated classes across methods, ie. each occurance of "new()" in method M,C (method with name M defined in class C)

 Format: *#Method Name    #Method Class   #Instantiated Class *



### Output of XTA algorithm

**1. Reachable.csv**:  Enlists reachable methods as per the algorithm


**2. staticLookup.csv**:  For each method call to e.m() checks for the applicable method that will be applied on the object e. As the desired method might not be defined agains the objectType(e) but one of its super class.

Format: *#Static Class of object         #Method Name        #Applicable Method Class    #Applicable Method Name(same as Method Name)*



### To Enter Data Flow facts


1. To enter new Classes (refer next for sub-classes)
    
    \- Enter data in Classes.facts
    
    Format: *#Class Name*

2. To enter new SubClasses
 
    \- Enter data in SubClasses

	Format:*#Class      #Subclass       #Subclass       #Subclass       ...*


3.  To enter new Methods
    -Enter data in Methods
    Format
    #Class name     #Method1    #Method2    ...


4. To enter Method Calls
    
    -Enter data in MethodCall.facts
    
    Format:*#Caller Method name #Caller Method Class    #Called Method name #Static Class of object method is being called on*


5. To enter instantiated class information

    -Enter data in instantiated
    
    Format: *#Instantiating method name  #Instantiating method's class   #type of instance ( C of new C() )*



Note: Dataflow facts have been entered manually.