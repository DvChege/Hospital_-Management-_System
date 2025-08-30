from person import Person
class Patient(Person):
    """A specialized 'distribution' of Person - like Ubuntu is to Debian"""
    
    def __init__(self, name: str, age: int, patient_id: str, medical_history=None):
        super().__init__(name, age)
        self.patient_id = patient_id
        self._medical_history = medical_history or []
    
    def add_medical_record(self, record: str):
        """Polymorphic behavior - different from Doctor's implementation"""
        self._medical_history.append(record)
        print(f"Record added: {record} (Like adding a PPA to your sources.list!)")

class Doctor(Person):
    """Another specialized 'distro' with medical superpowers"""
    
    def __init__(self, name: str, age: int, doctor_id: str, specialty: str):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialty = specialty
    
    def diagnose(self, patient: Patient, diagnosis: str):
        """Polymorphism in action - Doctors diagnose, Admins don't!"""
        print(f"Dr. {self.name} diagnosed {patient.name}: {diagnosis}")
        patient.add_medical_record(f"Diagnosis: {diagnosis}")