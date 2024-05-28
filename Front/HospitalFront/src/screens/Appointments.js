import React, { useState, useEffect } from 'react';
import Layout from '../Layout';
import { BiPlus } from 'react-icons/bi';
import { AppointmentTable } from '../components/Tables';
import { AppointmentsData } from '../components/Datas';
import AddAppointmentModal from '../components/Modals/AddAppointmentModal';
import DelAppointmentModal from '../components/Modals/DelAppointmentModal';

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

  const handleUpdate = (id) => {
    const appointment = appointmentsData.find(appt => appt.id === id);
    setSelectedAppointment(appointment);
    setIsModalOpen(true);
  };

  const handleDelete = (id) => {
    const appointment = appointmentsData.find(appt => appt.id === id);
    setSelectedAppointment(appointment);
    setIsDeleteModalOpen(true);
  };

  const getData = async () => {
    const data = await AppointmentsData(filterDate);
    setAppointmentsData(data);
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
            onChange={(e) => setFilterDate(e.target.value)}
            className="mr-4 px-4 py-2 border rounded-md"
          />
          <button
            onClick={() => setIsModalOpen(true)}
            className="flex items-center bg-green-500 text-white px-4 py-2 rounded-md"
          >
            <BiPlus className="mr-2" />
            Añadir Cita
          </button>
        </div>
      </div>
      <AppointmentTable
        data={appointmentsData}
        onUpdate={handleUpdate}
        onDelete={handleDelete}
      />
    </Layout>
  );
}

export default Appointments;