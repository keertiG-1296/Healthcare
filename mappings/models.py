from django.db import models
from django.contrib.auth import get_user_model
from patients.models import Patient
from doctors.models import Doctor

User = get_user_model()

class PatientDoctorMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"