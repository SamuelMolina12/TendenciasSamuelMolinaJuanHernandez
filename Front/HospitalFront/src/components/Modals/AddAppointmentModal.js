import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createAppointment } from '../Datas';
import moment from 'moment';

function AddAppointmentModal({ onClose, isOpen, appointment}) {
  const [formData, setFormData] = useState({

    appointmentDate: '',
    appointmentTime: '',
    doctor: '',
    appointmentType: '',
    patientId: '',
  });

  useEffect(() => {
    if (appointment) {
      setFormData({

        appointmentDate: appointment.appointmentDate || '',
        appointmentTime: appointment.appointmentTime || '',
        doctor: appointment.doctor || '',
        appointmentType: appointment.appointmentType || '',
        patientId: appointment.patientId || '',
      });
    }
  }, [appointment]);

  const handleInputChange = (e) => {

    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async () => {
    try { 
      const formattedDate = moment(formData.appointmentDate, 'YYYY-MM-DD').format('DD/MM/YYYY');
      const formattedData = {
        date: formattedDate,
        hour: formData.appointmentTime,
        doctor: formData.doctor,
        appointmentType: formData.appointmentType,
        patientId: formData.patientId,
      };

      await createAppointment(formattedData);
      toast.success('Cita creada con éxito');
      onClose();
    } catch (error) {
      toast.error('Error al guardar la cita. Por favor, inténtalo de nuevo.');

    }
  };

  return (
    <Modal
      closeModal={onClose}
      isOpen={isOpen}
      title={"Crear Cita"}
      width="max-w-3xl"
    >
      <Input
        label="Fecha de la Cita"
        name="appointmentDate"
        type="date"
        value={formData.appointmentDate}
        onChange={handleInputChange}
        color={true}
      />
      <Input
        label="Hora de la Cita"
        name="appointmentTime"
        type="time"
        value={formData.appointmentTime}
        onChange={handleInputChange}
        color={true}
      />
      <Input
        label="Cedula del doctor"
        name="doctor"
        value={formData.doctor}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del doctor"
        color={true}
      />
      <Input
        label="Tipo de Cita"
        name="appointmentType"
        value={formData.appointmentType}
        onChange={handleInputChange}
        placeholder="Ingrese el tipo de cita"
        color={true}
      />
      <Input
        label="Cedula del paciente"
        name="patientId"
        value={formData.patientId}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del paciente"
        color={true}
      />
      <div className="grid sm:grid-cols-2 gap-4 w-full">
        <button
          onClick={onClose}
          className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light border border-red-600"
        >
          Cancelar
        </button>
        <Button
          label="Guardar"
          Icon={HiOutlineCheckCircle}
          onClick={handleSubmit}
          color="bg-subMain"
          textColor="text-white"
        />
      </div>
    </Modal>
  );
}

export default AddAppointmentModal;
