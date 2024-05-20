import React, { useState } from 'react';
import Modal from './Modal';
import { Button } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { deleteSpecialist } from '../Datas';

function DelSpecialistModal({ closeModal, isOpen, specialistId, onDeleteSuccess }) {
  const [errorMessage, setErrorMessage] = useState('');

  const handleDelete = async () => {
    try {
      await deleteSpecialist(specialistId);
      toast.success('Especialista eliminado con éxito');
      onDeleteSuccess();
      closeModal();
    } catch (error) {
      console.error('Error al eliminar el especialista:', error);
      setErrorMessage(error.response?.data?.message || 'Error al eliminar el especialista. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title="Eliminar Especialista"
      width="max-w-md"
    >
      <p>¿Seguro que quiere eliminar al especialista?</p>
      {errorMessage && <p className="text-red-600">{errorMessage}</p>}
      <div className="grid sm:grid-cols-2 gap-4 w-full mt-4">
        <button
          onClick={closeModal}
          className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light border border-red-600"
        >
          Cancelar
        </button>
        <Button
          label="Eliminar especialista"
          Icon={HiOutlineCheckCircle}
          onClick={handleDelete}
          color="bg-red-600"
          textColor="text-white"
        />
      </div>
    </Modal>
  );
}

export default DelSpecialistModal;
