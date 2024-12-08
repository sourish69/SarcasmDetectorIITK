import numpy as np
class matrix_op:

    def add(ar1,ar2):
        print(ar1+ar2)

    def matMul(ar1,ar2):
        print(np.dot(ar1,ar2))
        

    def determinant(ar1,ar2):
        ar1_rows,ar1_cols=ar1.shape
        ar2_rows,ar2_cols=ar2.shape

        if(ar1_rows!=ar1_cols):
            print("The matrix is not square")
        else:
            print("Determinant of first array:",np.linalg.det(ar1))
        

        if(ar2_rows!=ar2_cols):
            print("The matrix is not square")
        else:
            print("Determinant: of second array",np.linalg.det(ar2))



def matrix_operation(ar1,ar2,choice):
    if(choice=="ADD"):
        matrix_op.add(ar1,ar2)
    elif(choice=="MULTIPLY"):
        matrix_op.matMul(ar1,ar2)
    elif(choice=="DETERMINANT"):
        matrix_op.determinant(ar1,ar2)
    else:
        print("Invalid choice entered")




l1=eval(input("Enter first 2D array "))
l2=eval(input("Enter second 2D array "))
ar1=np.array(l1)
ar2=np.array(l2)
choice=input("Enter the required operation: ADD for addition, MULTIPLY for multiplication and DETERMINANT for determinant ")
matrix_operation(ar1,ar2,choice)


        



        
