"""

Student Record and Academic Management System

Data Organization using Python



B.Tech - AI & ML | First Year | Division B

Sanjivani University

"""



students = []





def clean_text(value):

    if isinstance(value, tuple):

        return value[0].strip() if value else ""

    return str(value).strip() if value is not None else ""





def add_student(roll_number, registration_number, name, department,

                subjects, marks, attendance, dob, email, address, clubs):

    """Add a new student record after checking for duplicate roll numbers."""

    roll_number = (clean_text(roll_number).upper(),)         # Tuple

    registration_number = (clean_text(registration_number).upper(),) # Tuple

    name = clean_text(name).title()                           # String

    department = clean_text(department).upper()               # String

    email = clean_text(email).lower()                         # String

    address = clean_text(address)                             # String

    dob = tuple(clean_text(dob).split("-"))                   # Tuple



    for student in students:

        if student["roll_number"] == roll_number:

            print("Student already exists.")

            return False



    student = {

        "roll_number": roll_number,

        "registration_number": registration_number,

        "name": name,

        "department": department,

        "subjects": list(subjects),                 # List

        "marks": list(marks),                       # List

        "attendance": list(attendance),             # List

        "dob": dob,

        "contact": {"email": email, "address": address},

        "clubs": set(clubs)                         # Set

    }



    students.append(student)                        # List of dictionaries

    print("Student added successfully.")

    return True





def search_student(roll_number):

    """Search for a student by roll number."""

    roll_number = (clean_text(roll_number).upper(),)

    for student in students:

        if student["roll_number"] == roll_number:

            return student

    return None





def update_student(roll_number, field, new_value):

    """Update an allowed student field."""

    student = search_student(roll_number)

    if student is None:

        print("Student not found.")

        return False



    field = clean_text(field).lower()



    if field == "roll_number":

        new_roll = (clean_text(new_value).upper(),)

        for s in students:

            if s is not student and s["roll_number"] == new_roll:

                print("Error: Roll number already exists for another student.")

                return False

        student["roll_number"] = new_roll

    elif field == "registration_number":

        student["registration_number"] = (clean_text(new_value).upper(),)

    elif field == "name":

        student["name"] = clean_text(new_value).title()

    elif field == "department":

        student["department"] = clean_text(new_value).upper()

    elif field == "email":

        student["contact"]["email"] = clean_text(new_value).lower()

    elif field == "address":

        student["contact"]["address"] = clean_text(new_value)

    elif field == "dob":

        student["dob"] = tuple(clean_text(new_value).split("-"))

    elif field == "subjects":

        student["subjects"] = list(new_value)

    elif field == "attendance":

        student["attendance"] = list(new_value)

    elif field == "marks":

        student["marks"] = list(new_value)

    elif field == "clubs":

        student["clubs"] = set(new_value)

    else:

        print("Invalid field.")

        return False



    print("Student record updated successfully.")

    return True





def delete_student(roll_number):

    """Delete a student record by roll number."""

    student = search_student(roll_number)

    if student is None:

        print("Student not found.")

        return False

    students.remove(student)

    print("Student record deleted successfully.")

    return True





def calculate_average(student):

    """Calculate the average of a student's marks."""

    if not student:

        return 0.0

    marks = student.get("marks", [])

    if not marks:

        return 0.0

    return sum(marks) / len(marks)





def find_highest_scorer():

    """Return the student with the highest average marks."""

    if not students:

        return None

    return max(students, key=calculate_average)





def list_by_department(department):

    """Return all students belonging to a department."""

    department = clean_text(department).upper()

    return [student for student in students

            if student["department"] == department]





def count_students():

    return len(students)





def display_records(records=None):

    """Display all records or a supplied collection."""

    records = students if records is None else records

    if not records:

        print("No student records available.")

        return



    print("\n" + "=" * 72)

    print("STUDENT RECORDS")

    print("=" * 72)



    for student in records:

        print(f"Roll Number : {student['roll_number'][0]}")

        print(f"Registration: {student['registration_number'][0]}")

        print(f"Name        : {student['name']}")

        print(f"Department  : {student['department']}")

        print(f"Subjects    : {', '.join(student['subjects'])}")

        print(f"Marks       : {student['marks']}")

        print(f"Average     : {calculate_average(student):.2f}")

        print(f"Attendance  : {student['attendance']}")

        print(f"DOB         : {'-'.join(student['dob'])}")

        print(f"Email       : {student['contact']['email']}")

        print(f"Address     : {student['contact']['address']}")

        print(f"Clubs       : {', '.join(sorted(student['clubs']))}")

        print("-" * 72)





def generate_report():

    """Generate a summary report using sets."""

    if not students:

        print("No records available for report.")

        return



    departments = {student["department"] for student in students}

    subjects = {subject for student in students for subject in student["subjects"]}

    clubs = {club for student in students for club in student["clubs"]}



    print("\n" + "=" * 72)

    print("ACADEMIC REPORT")

    print("=" * 72)

    print(f"Total students      : {count_students()}")

    print(f"Departments         : {', '.join(sorted(departments))}")

    print(f"Unique subjects     : {', '.join(sorted(subjects))}")

    print(f"Student clubs       : {', '.join(sorted(clubs))}")



    top = find_highest_scorer()

    if top:

        print(f"Highest scorer      : {top['name']} ({calculate_average(top):.2f})")



    print("\nStudents by department:")

    for department in sorted(departments):

        print(f"  {department}: {len(list_by_department(department))}")





def seed_demo_data():

    add_student("S001", "REG001", "Aarav Kumar", "CSE",

                ["Python", "Mathematics", "Physics"], [86, 91, 84], [92, 95, 90],

                "2006-04-19", "aarav@example.com", "Guntur, Andhra Pradesh",

                ["Coding Club", "AI Club"])

    add_student("S002", "REG002", "Meera Sharma", "AIML",

                ["Python", "Mathematics", "AI"], [94, 89, 96], [97, 91, 95],

                "2006-08-12", "meera@example.com", "Vijayawada, Andhra Pradesh",

                ["AI Club"])





def main():

    seed_demo_data()



    while True:

        print("\n" + "=" * 72)

        print("STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM")

        print("=" * 72)

        print("1. Add Student")

        print("2. Search Student")

        print("3. Update Student")

        print("4. Delete Student")

        print("5. Display Records")

        print("6. Calculate Average")

        print("7. Generate Reports")

        print("8. Find Highest Scorer")

        print("9. List Students by Department")

        print("10. Count Students")

        print("0. Exit")



        choice = input("Enter your choice: ").strip()



        if choice == "1":

            roll = input("Roll number: ")

            reg = input("Registration number: ")

            name = input("Name: ")

            dept = input("Department: ")

            subjects = [s.strip() for s in input("Subjects (comma-separated): ").split(",") if s.strip()]

            marks_input = input("Marks (comma-separated): ")

            attendance_input = input("Attendance (comma-separated): ")

            try:

                marks = [float(x.strip()) for x in marks_input.split(",") if x.strip()]

                attendance = [float(x.strip()) for x in attendance_input.split(",") if x.strip()]

            except ValueError:

                print("Error: Marks and attendance must be numbers.")

                continue

            dob = input("Date of birth (YYYY-MM-DD): ")

            email = input("Email: ")

            address = input("Address: ")

            clubs = [c.strip() for c in input("Clubs (comma-separated): ").split(",") if c.strip()]

            add_student(roll, reg, name, dept, subjects, marks, attendance, dob, email, address, clubs)



        elif choice == "2":

            result = search_student(input("Enter roll number: "))

            if result:

                display_records([result])

            else:

                print("Student not found.")



        elif choice == "3":

            roll = input("Enter roll number: ")

            field = input("Field (roll_number/registration_number/name/department/email/address/dob/subjects/marks/attendance/clubs): ").strip().lower()

            if field in {"marks", "attendance"}:

                try:

                    values = [float(v.strip()) for v in input("Enter comma-separated values: ").split(",") if v.strip()]

                    update_student(roll, field, values)

                except ValueError:

                    print("Error: Marks and attendance must be numbers.")

            elif field in {"subjects", "clubs"}:

                values = [v.strip() for v in input("Enter comma-separated values: ").split(",") if v.strip()]

                update_student(roll, field, values)

            else:

                update_student(roll, field, input("New value: "))



        elif choice == "4":

            delete_student(input("Enter roll number: "))



        elif choice == "5":

            display_records()



        elif choice == "6":

            result = search_student(input("Enter roll number: "))

            if result:

                print(f"Average marks: {calculate_average(result):.2f}")

            else:

                print("Student not found.")



        elif choice == "7":

            generate_report()



        elif choice == "8":

            top = find_highest_scorer()

            if top:

                print(f"Highest scorer: {top['name']} - {calculate_average(top):.2f}")

            else:

                print("No student records available.")



        elif choice == "9":

            dept = input("Enter department: ")

            records = list_by_department(dept)

            if records:

                display_records(records)

            else:

                print(f"No students found in department '{dept.strip().upper()}'.")



        elif choice == "10":

            print(f"Total students: {count_students()}")



        elif choice == "0":

            print("Thank you. Program ended.")

            break



        else:

            print("Invalid choice. Please try again.")





if __name__ == "__main__":

    main()
