def calculate_total(sub1,sub2,sub3):
    return sub1+sub2+sub3


def calculate_avg(total):
    return total//3

def class_obtained(avg):
    if avg>=60:
        return "1st Class"
    elif avg>=50:
        return "2nd Class"
    elif avg>=35:
        return "Pass Class"
    else:
        return "Fail"
    
name = input("Enter the Student Name:")
sub1 = int(input("Enter Subject1 marks:"))
sub2 = int(input("Enter the Subject2 marks:"))
sub3 = int(input("Enter the Subject3 marks:"))
total=calculate_total(sub1,sub2,sub3)
avg=calculate_avg(total)
classObtained=class_obtained(avg)

if 100<sub1 or sub1<0 or 100<sub2 or sub2<0 or 100<sub3 or sub3<0:
    print("Invalid Marks")
else:

    print("Student Report Card")
    print("Nane: ",name)
    print("Total Marks: ",total)
    print("Average Marks: ",avg)
    print("Class Obtained: ",classObtained)