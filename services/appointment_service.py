from nameko.rpc import rpc

class AppointmentService:
    name = "appointment_service"

    @rpc
    def book_appointment(self, patient_id, doctor, date, time, reason):
        # Implement appointment booking logic
        pass
