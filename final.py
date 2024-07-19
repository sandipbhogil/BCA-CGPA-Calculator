each_sem_sgpa = []
def Cal_sgpa():

        print("Enter the subject and marks of semester")
        T_subject=int(input("enter the number of theory subject :"))
        print(f"I have {T_subject} Theory subject ")
        T_subj=[]
        T_mark=[]
        T_cred=[]
        T_grad=[]
        T_result=[]
        T_subj_grad_poin=[]

        def accept_T_sub():
            for i in range(1,T_subject+1):
                sub=(input("enter the Theory subject name:"))
                T_subj.append(sub)
            print("Subject Name :",T_subj)


        def accept_T_marks():
            for i in range(1,T_subject+1):
                marks=int(input("Please enter the theory subject marks between 1-100 :"))
                T_mark.append(marks)
            print("Given Marks :",T_mark)

        def T_grade():
            for i in T_mark:
                if i>90 and i<=100:
                    d="O"
                    T_grad.append(d)

                elif i>80 and i<=90:
                    e="A+"
                    T_grad.append(e)

                elif i>70 and i<=80:
                    f= "A"
                    T_grad.append(f)
                elif i>60 and i<=70:
                    g="B+"
                    T_grad.append(g)
                elif i>50 and i<=60:
                    h="B"
                    T_grad.append(h)
                elif i>40 and i<=50:
                    j="C"
                    T_grad.append(j)
                elif i<40:
                    k="F"
                    T_grad.append(k)
                else:
                    print("enter the valid statement")
            print("Theory Grade :",T_grad)



        def cal_T_credit_point():
            for i in T_mark:
                T_cred.append(4)
            print("TheoryCredit :",T_cred)

        def cal_T_grade_point():
            for i in T_grad:
                if i==("O"):
                    T_subj_grad_poin.append(10)
                elif i==("A+"):
                    T_subj_grad_poin.append(9)
                elif i==("A"):
                    T_subj_grad_poin.append(8)
                elif i==("B+"):
                    T_subj_grad_poin.append(7)
                elif i==("B"):
                    T_subj_grad_poin.append(6)
                elif i==("C"):
                    T_subj_grad_poin.append(5)
                elif i==("F"):
                    T_subj_grad_poin.append(0)
                else:
                    print("Invalid")

            print("Thoery Grade Point :",T_subj_grad_poin)


        def cal_T_total_grad_point():
            lenght1=len(T_cred)
            lenght2=len(T_subj_grad_poin)
            if lenght1!=lenght2:
                raise ValueError("Both lists must have the same length")
            for i in range(lenght1):
                # Multiply the corresponding elements and append to the result list
                T_result.append(T_cred[i] * T_subj_grad_poin[i])

        # Print the result
            print("Theory Point CG :",T_result)


        accept_T_sub()
        accept_T_marks()
        T_grade()
        cal_T_credit_point()
        cal_T_grade_point()
        cal_T_total_grad_point()

        P_subject=int(input("enter the number of Practical subject :"))
        print(f"I have {P_subject} practical subject ")
        P_subj=[]
        P_mark=[]
        P_cred=[]
        P_grad=[]
        P_result=[]
        P_subj_grad_poin=[]

        def accept_P_subject():
            for i in range(1,P_subject+1):
                P_sub=input("enter the practical subject name :")
                P_subj.append(P_sub)
            print(P_subj)


        def accept_P_marks():
            for i in range(1,P_subject+1):
                mark=int(input("enter the practcal marks beween 1-50:"))
                P_mark.append(mark)
            print(P_mark)


        def P_grade():
            for i in P_mark:
                if i>45 and i<=50:
                    P_grad.append("O")
                elif i>40 and i<=45:
                    P_grad.append("A+")
                elif i>35 and i<=40:
                    P_grad.append("A")
                elif i>30 and i<=35:
                    P_grad.append("B+")
                elif i>25 and i<=30:
                    P_grad.append("B")
                elif i>20 and i<=25:
                    P_grad.append("C")
                elif i<20:
                    P_grad.append("F")
                else:
                    print("Invalid")
            print("Practical Grade:",P_grad)
        def cal_p_grade_point():
            for i in P_grad:
                if i=="O":
                    P_subj_grad_poin.append(10)
                elif i=="A+":
                    P_subj_grad_poin.append(9)
                elif i== "A":
                    P_subj_grad_poin.append(8)
                elif i== "B+":
                    P_subj_grad_poin.append(7)
                elif i== "B":
                    P_subj_grad_poin.append(6)
                elif i== "C":
                    P_subj_grad_poin.append(5)
                elif i== "F":
                    P_subj_grad_poin.append(0)
                else:
                    print("Invalid")
            print("Practical Grade Point :",P_subj_grad_poin)
        def cal_p_credit_point():
                for i in P_mark:
                    if P_subject==4:
                        P_cred.append(1.5)
                    elif P_subject<4:
                        P_cred.append(2)
                    else:
                        print("Invalid")
                        break
                print("Practical Credit point :",P_cred)

        def cal_P_total_grad_point():
            lenght3=len(P_cred)
            lenght4=len(P_subj_grad_poin)
            if lenght3 != lenght4:
                raise ValueError("Both lists must have the same length")
            for i in range(lenght3):
                P_result.append(P_cred[i] * (P_subj_grad_poin[i]))

            print("Point CG :",P_result)


        accept_P_subject()
        accept_P_marks()
        P_grade()
        cal_p_grade_point()
        cal_p_credit_point()
        cal_P_total_grad_point()

        ex_subj = []
        ex_mark = []
        ex_cred = []
        ex_grad = []
        ex_result = []
        ex_subj_grad_poin = []
        print("You have external subject")

        a=input("enter yes or no :")
        if a=="no":
            print("No external subject for this semester :")

        elif a=="yes":
            Ex_subject=int(input("enter the number of external subject :"))
            print(f"I have {Ex_subject} external subject ")


            def accept_Ex_subject():
                for i in range(1, Ex_subject + 1):
                    Ex_sub = input("enter the practical subject name :")
                    ex_subj.append(Ex_sub)
                print(ex_subj)

            def accept_Ex_marks():
                for i in range(1, Ex_subject + 1):
                    mark = int(input("enter the practcal marks beween 1-50:"))
                    ex_mark.append(mark)
                print(ex_mark)

            def Ex_grade():
                for i in ex_mark:
                    if i > 45 and i <= 50:
                        ex_grad.append("O")
                    elif i > 40 and i <= 45:
                        ex_grad.append("A+")
                    elif i > 35 and i <= 40:
                        ex_grad.append("A")
                    elif i > 30 and i <= 35:
                        ex_grad.append("B+")
                    elif i > 25 and i <= 30:
                        ex_grad.append("B")
                    elif i > 20 and i <= 25:
                        ex_grad.append("C")
                    elif i < 20:
                        ex_grad.append("F")
                    else:
                        print("Invalid")
                print("Practical Grade:", ex_grad)

            def cal_Ex_grade_point():
                for i in ex_grad:
                    if i == "O":
                        ex_subj_grad_poin.append(10)
                    elif i == "A+":
                        ex_subj_grad_poin.append(9)
                    elif i == "A":
                        ex_subj_grad_poin.append(8)
                    elif i == "B+":
                        ex_subj_grad_poin.append(7)
                    elif i == "B":
                        ex_subj_grad_poin.append(6)
                    elif i == "C":
                        ex_subj_grad_poin.append(5)
                    elif i == "F":
                        ex_subj_grad_poin.append(0)
                    else:
                        print("Invalid")
                print("Practical Grade Point :", ex_subj_grad_poin)

            def cal_Ex_credit_point():
                for i in ex_mark:
                    ex_cred.append(2)
                print("Practical Credit point :", ex_cred)

            def cal_Ex_total_grad_point():
                lenght3 = len(ex_cred)
                lenght4 = len(ex_subj_grad_poin)
                if lenght3 != lenght4:
                    raise ValueError("Both lists must have the same length")
                for i in range(lenght3):
                    ex_result.append(ex_cred[i] * (ex_subj_grad_poin[i]))

                print("Point CG :", ex_result)


            accept_Ex_subject()
            accept_Ex_marks()
            Ex_grade()
            cal_Ex_grade_point()
            cal_Ex_credit_point()
            cal_Ex_total_grad_point()

        else:
            print("Invalid")



        def cal_sgpa():
            sum_of_total_T_grade_point = sum(T_result)
            sum_of_total_T_credit_point = sum(T_cred)
            sum_of_total_P_grade_point = sum(P_result)
            sum_of_total_P_credit_point = sum(P_cred)
            sum_of_total_Ex_grade_point =sum(ex_result)
            sum_of_total_Ex_credit_point=sum(ex_cred)
            total_credit_point = sum_of_total_T_credit_point + sum_of_total_P_credit_point+sum_of_total_Ex_credit_point
            total_grade_point = sum_of_total_T_grade_point + sum_of_total_P_grade_point+sum_of_total_Ex_grade_point
            sgpa = total_grade_point / total_credit_point
            each_sem_sgpa.append(sgpa)
            print(f"\n--- SGPA for a Semester ---")
            print("|------------------------------------------|")
            print("| Subject   | Grade | Credit | Grade Point |")
            print("|------------------------------------------|")
            for i in range(len(T_subj)):
                print(f"| {T_subj[i]:<9} | {T_grad[i]:<5} | {T_cred[i]:<6} | {T_result[i]:<11} |")
            for i in range(len(P_subj)):
                print(f"| {P_subj[i]:<9} | {P_grad[i]:<5} | {P_cred[i]:<6} | {P_result[i]:<11} |")
            if ex_subj:

                for i in range(len(ex_subj)):
                    print(f"| {ex_subj[i]:<9} | {ex_grad[i]:<5} | {ex_cred[i]:<6} | {ex_result[i]:<11} |")
            print("|------------------------------------------|")

            print(f"| SGPA: {sgpa:.2f}                               |")
            print(f"|Total : Creadit {total_credit_point}   Grade Points :{total_grade_point}    |")
            print("|------------------------------------------|")

        cal_sgpa()

def Cal_cgpa():
    semester=int(input("enter the number of semester :"))

    for sem in range(1,semester+1):
        Cal_sgpa()
    def cgpa():
        sum_of_all_sem_sgpa=sum(each_sem_sgpa)
        length_of_sgpa=len(each_sem_sgpa)
        cgpa=sum_of_all_sem_sgpa/length_of_sgpa
        print("|------------------------------------------|")
        print(f"| CGPA :  {cgpa:.2f}                            |")
        print("|------------------------------------------|")
    cgpa()


# def choice():
choice=int(input("enter the choice \n"
                 "1 : SGPA\n"
                 "2 : CGPA\n"
                 "3 : Exit\n"
                     "Enter Your Choice :"))
while choice!=3:
    if choice==1:
        Cal_sgpa()
        break
    elif choice==2:
         Cal_cgpa()
         break
    else:
         exit()
# choice()


