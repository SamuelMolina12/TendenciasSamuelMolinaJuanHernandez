
import { useEffect, useState } from 'react';
import { AppointmentsDataPatient } from '../Datas';
import { AppointmentTable } from '../Tables';

function ClinicalAppointmentUsed({ patientId }) {

  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (patientId) {
        try {
          const appointmentsData = await AppointmentsDataPatient(patientId);
          setAppointments(appointmentsData);
        } catch (error) {
          console.error('Error:', error);
        }
      }
    };
    fetchData();
  }, [patientId]);



  return (
    <div className="w-full">
      <h1 className="text-sm font-medium mb-6">Citas Médicas del paciente</h1>
      <div className="w-full overflow-x-scroll">
        <AppointmentTable data={appointments} />
      </div>
    </div>
  );
}

export default ClinicalAppointmentUsed;
