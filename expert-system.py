# define a rule-based expert system
class ExpertSystem:
    def __init__(self):
        self.rules = {} 

    def add_rule(self, symptom, diagnosis):
        self.rules[symptom] = diagnosis

    def infer(self, symptoms):
        for symptom in symptoms:
            if symptom in self.rules:
                return self.rules[symptom]
        return "Unknown"

expert_system = ExpertSystem()

expert_system.add_rule("cough", "Common cold")
expert_system.add_rule("fever", "Influenza")
expert_system.add_rule("headache", "Migraine")

user_input = input("Enter your symptoms: ")
symptoms = user_input.split()

diagnosis = expert_system.infer(symptoms)

print("Diagnosis:", diagnosis)