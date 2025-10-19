
from datetime import date

def get_grade(percentage):
    if percentage >=90:
        return "A+"
    elif percentage >=80:
        return "B+"
    elif percentage >=70:
        return "C+"
    elif percentage >=60:
        return "D+"
    elif percentage >=50:
        return "E"
    else:
        return "fail"

def generate_report():
    name = input("enter the name:")
    stud_class= input("class/sec:")
    subjects={}
    print("\nenter subjects and marks(type 'done' to finish)")
    while True:
        subject=input("subject name :").strip()
        if subject.lower()=="done":
            break
        marks=float(input(f"marks obtained in {subject}:"))
        subjects[subject]=marks
    total_marks=sum(subjects.values())
    max_marks=len(subjects)*100
    percentage=(total_marks/max_marks)*100
    grade=get_grade(percentage)
    
    print("\n==========Report Card==========")
    print(f"name:{name}")
    print(f"class:{stud_class}")
    print(f"date:{date.today()}")
    print("---------------------------------")
    print(f"{'subject':20}{'marks':>10}")
    for sub,mark in subjects.items():
        print(f"{sub:20}{mark:>10}")
    print("______________________________")
    print(f"total:{total_marks}")
    print(f"percent:{percentage}")
    print(f"grade:{grade}")
    print("-----------------------------------")

def main():
    while True:
        print("generate new repo card")
        choice=input("choice")
        if choice=="1":
            report=generate_report()
        elif choice=="2":
            print("have a gr8 day")
            break
        else:
            print("invalid")

if __name__== "__main__":
    main()