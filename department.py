from persons import Patient, Doctor

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
