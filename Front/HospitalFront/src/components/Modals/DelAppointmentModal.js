import React from 'react';
import Modal from './Modal';
import { Button } from '../Form';
import { HiOutlineTrash } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { deleteAppointment } from '../Datas';

function DelAppointmentModal({ onClose, isOpen, appointment, onDeleteSuccess }) {
  const handleDelete = async () => {
    try {
      await deleteAppointment(appointment.id);
      toast.success('Cita eliminada con éxito');
      onDeleteSuccess();
      onClose();
    } catch (error) {
      toast.error('Error al eliminar la cita. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={onClose}
      isOpen={isOpen}
      title="Eliminar Cita"
      width="max-w-lg"
    >
      <p>¿Está seguro de que desea eliminar esta cita?</p>
      <div className="grid sm:grid-cols-2 gap-4 w-full mt-4">
        <button
          onClick={onClose}
          className="bg-gray-600 bg-opacity-5 text-gray-600 text-sm p-4 rounded-lg font-light border border-gray-600"
        >
          Cancelar
        </button>
        <Button
          label="Eliminar"
          Icon={HiOutlineTrash}
          onClick={handleDelete}
          color="bg-red-600"
          textColor="text-white"
        />
      </div>
    </Modal>
  );
}

export default DelAppointmentModal;