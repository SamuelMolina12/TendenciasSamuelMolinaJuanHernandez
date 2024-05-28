import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createAppointment, updateAppointment } from '../Datas';

function AddAppointmentModal({ onClose, isOpen, appointment }) {
  const [formData, setFormData] = useState({
    patientName: '',
    appointmentDate: '',
    appointmentTime: '',
    doctorName: '',
  });

  useEffect(() => {
    if (appointment) {
      setFormData({
        patientName: appointment.patientName || '',
        appointmentDate: appointment.appointmentDate || '',
        appointmentTime: appointment.appointmentTime || '',
        doctorName: appointment.doctorName || '',
      });
    }
  }, [appointment]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      if (appointment) {
        await updateAppointment(appointment.id, formData);
        toast.success('Cita actualizada con éxito');
      } else {
        await createAppointment(formData);
        toast.success('Cita creada con éxito');
      }
      onClose();
    } catch (error) {
      toast.error('Error al guardar la cita. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={onClose}
      isOpen={isOpen}
      title={appointment ? 'Actualizar Cita' : 'Crear Cita'}
      width="max-w-3xl"
    >
      <Input
        label="Nombre del Paciente"
        name="patientName"
        value={formData.patientName}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del paciente"
        color={true}
      />
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
        label="Nombre del Doctor"
        name="doctorName"
        value={formData.doctorName}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del doctor"
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