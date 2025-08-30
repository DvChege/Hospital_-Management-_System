# hospital_system.py

class Person:
    def __init__(self, name: str, age: int, id_number: str):
        self.name = name
        self.age = age
        self.id_number = id_number


class Patient(Person):
    def __init__(self, name: str, age: int, patient_id: str):
        super().__init__(name, age, patient_id)
        self.records = []

    def add_record(self, diagnosis: str):
        self.records.append(diagnosis)
        print(f"Record added for {self.name}: {diagnosis}")


class Doctor(Person):
    def __init__(self, name: str, age: int, doctor_id: str, specialty: str):
        super().__init__(name, age, doctor_id)
        self.specialty = specialty

    def diagnose(self, patient: Patient, diagnosis: str):
        print(f"Dr. {self.name} ({self.specialty}) diagnoses {patient.name}: {diagnosis}")
        patient.add_record(diagnosis)


class Department:
    """A department is COMPOSED of doctors - like a meta-package depends on components"""
    
    def __init__(self, name: str):
        self.name = name
        self.doctors = []
    
    def add_doctor(self, doctor: Doctor):
        """Composition: Department HAS-A Doctors (not IS-A relationship)"""
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added to {self.name} (Like installing a new service!)")
    
    def get_doctors_by_specialty(self, specialty: str):
        """Filtering doctors - similar to 'apt search' functionality!"""
        return [d for d in self.doctors if d.specialty == specialty]


class Hospital:
    """The main system that COMPOSES all departments - your systemd manager!"""
    
    def __init__(self, name: str):
        self.name = name
        self.departments = {}
    
    def add_department(self, department: Department):
        """Adding departments is like enabling a new repository!"""
        self.departments[department.name] = department
        print(f"Department added: {department.name} (sudo add-apt-repository completed)")
    
    def schedule_appointment(self, patient: Patient, department_name: str, doctor_specialty: str):
        """Polymorphic operation that varies by department"""
        if department_name not in self.departments:
            raise ValueError(f"Department {department_name} not found - check your /etc/hosts!")
        
        department = self.departments[department_name]
        doctors = department.get_doctors_by_specialty(doctor_specialty)
        
        if not doctors:
            print(f"No {doctor_specialty} doctors available - time for 'sudo apt install more-doctors'!")
            return None
        
        print(f"Appointment scheduled with Dr. {doctors[0].name} in {department_name}")
        return doctors[0]


# Let's boot up our hospital system! (Like 'sudo systemctl start hospital')
def main():
    print("=== WELCOME TO UBUNTU GENERAL HOSPITAL ===")
    print("Initializing system... (this might take a few dpkg prompts)")

    # Create hospital instance
    ubuntu_hospital = Hospital("Ubuntu General")
    
    # Add departments (repositories)
    cardiology = Department("Cardiology")
    pediatrics = Department("Pediatrics")
    
    ubuntu_hospital.add_department(cardiology)
    ubuntu_hospital.add_department(pediatrics)
    
    # Add doctors (install packages)
    dr_linus = Doctor("Linus Torvalds", 54, "DOC-001", "Cardiology")
    dr_mark = Doctor("Mark Shuttleworth", 49, "DOC-002", "Pediatrics")
    
    cardiology.add_doctor(dr_linus)
    pediatrics.add_doctor(dr_mark)   # ✅ fixed
    
    # Register patient (create user account)
    patient_ada = Patient("Ada Lovelace", 28, "PAT-1001")
    
    # Schedule appointment (run a service)
    print("\n$ hospital-cli schedule --department Cardiology --specialty Cardiology")
    doctor = ubuntu_hospital.schedule_appointment(patient_ada, "Cardiology", "Cardiology")
    
    # Diagnose (execute a command with sudo privileges)
    if doctor:
        doctor.diagnose(patient_ada, "Needs more open-source in her life")
    
    print("\nSystem running smoothly! (like a well-configured systemd)")


if __name__ == "__main__":
    main()
