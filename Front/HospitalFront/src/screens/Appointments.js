import React,{useState,useEffect} from 'react';
import Layout from '../Layout';
import { Calendar } from 'react-big-calendar';
import {BiPlus} from 'react-icons/bi';

import { AppointmentTable } from '../components/Tables';
import { AppointmentsData } from '../components/Datas';

import AddAppointmentModal from '../components/Modals/AddApointmentModal';

import DelAppointmentModal from '../components/Modals/DelAppointmentModal';

function Appointments() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [appointmentsData, setAppointmentsData] = useState([]);

  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedAppointment, setSelectedAppointment] = useState(null);

  const onCloseModal = async () => {
    setIsModalOpen(false);
    setSelectedAppointment(null);
    await getData();
  }

  const onCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setSelectedAppointment(null);
  }

  const handleUpdate = (id) => { 
    setSelectedAppointment(id);
    setIsDeleteModalOpen(true);
  };

  const getData = async () => {
    const data = await AppointmentsData();
    setAppointmentsData(data);
  };

  useEffect(() => {
    getData();
  }, []);
 
return (
    <Layout>
      {isModalOpen && (
        <AddAppointmentModal
          onClose={onCloseModal}
          appointment={selectedAppointment}
        />
      )}
      {isDeleteModalOpen && (
        <DelAppointmentModal
          onClose={onCloseDeleteModal}
          appointment={selectedAppointment}
        />
      )}
      <div className="flex justify-between items-center">
        <h1 className="text-3xl text-gray-700">Appointments</h1>
        <button
          onClick={() => setIsModalOpen(true)}
          className="flex items-center bg-green-500 text-white px-4 py-2 rounded-md"
        >
          <BiPlus className="mr-2" />
          Add Appointment
        </button>
      </div>
      <AppointmentTable
        data={appointmentsData}
        onUpdate={handleUpdate}
      />
    </Layout>
  );
}



    
