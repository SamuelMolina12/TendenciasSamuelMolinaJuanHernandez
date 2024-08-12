import React, { useState, useEffect } from 'react';
import Layout from '../Layout';
import { BiPlus } from 'react-icons/bi';
import { AppointmentTable } from '../components/Tables';
import { AppointmentsData } from '../components/Datas';
import AddAppointmentModal from '../components/Modals/AddAppointmentModal';
import DelAppointmentModal from '../components/Modals/DelAppointmentModal';
import moment from 'moment'; 

function Appointments() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [appointmentsData, setAppointmentsData] = useState([]);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedAppointment, setSelectedAppointment] = useState(null);
  const [filterDate, setFilterDate] = useState('');


  const onCloseModal = async () => {
    setIsModalOpen(false);
    setSelectedAppointment(null);
    await getData();
  };


  const onCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setSelectedAppointment(null);
  };




  const handleDelete = (id) => {
    const appointment = appointmentsData.find(appt => appt.id === id);
    setSelectedAppointment(appointment);
    setIsDeleteModalOpen(true);
  };


  const getData = async () => {
 
    const data = await AppointmentsData();
 


    const normalizedData = data.map(appointment => ({
      ...appointment,
      date: moment(appointment.date, 'DD/MM/YYYY').format('YYYY-MM-DD')
    }));


    const filteredData = filterDate
      ? normalizedData.filter(appointment => appointment.date === filterDate)
      : normalizedData;

    setAppointmentsData(filteredData);
  };


  useEffect(() => {
    getData();
  }, [filterDate]);

  return (
    <Layout>
      {isModalOpen && (
        <AddAppointmentModal
          isOpen={isModalOpen}
          onClose={onCloseModal}
          appointment={selectedAppointment}
        />
      )}
      {isDeleteModalOpen && (
        <DelAppointmentModal
          isOpen={isDeleteModalOpen}
          onClose={onCloseDeleteModal}
          appointment={selectedAppointment}
          onDeleteSuccess={getData}
        />
      )}
      <div className="flex justify-between items-center">
        <h1 className="text-3xl text-gray-700">Citas Médicas</h1>
        <div className="flex items-center">

          <input
            type="date"
            value={filterDate}
            onChange={(e) => {
              const selectedDate = e.target.value; 
              setFilterDate(selectedDate);
            }}
            className="mr-4 px-4 py-2 border rounded-md"
          />
        <button
        onClick={() => {
          setSelectedAppointment(null); 
          setIsModalOpen(true);
          }}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
        >
        <BiPlus className="text-2xl" />
        </button>
        </div>
      </div>
      <AppointmentTable
        data={appointmentsData}
        functions={{
          handleDelete: handleDelete,
        }}
        showPatientId={true}
        showActions={true}
      />
    </Layout>
  );
}

export default Appointments;
