import React from 'react';
import Modal from './Modal';
import { Button } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { deleteEmployer } from '../Datas'; // Debes cambiar esta línea

function DeleteEmployerModal({ closeModal, isOpen, employeeId, onDeleteSuccess }) {
  const handleDelete = async () => {
    try {
      await deleteEmployer(employeeId); // Debes cambiar esta línea
      toast.success('Empleado eliminado con éxito');
      onDeleteSuccess();
      closeModal();
    } catch (error) {
      console.error('Error al eliminar el empleado:', error);
      toast.error('Error al eliminar el empleado. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title="Eliminar Empleado"
      width="max-w-md"
    >
      <p>¿Seguro que desea eliminar al empleado?</p>
      <div className="grid sm:grid-cols-2 gap-4 w-full mt-4">
        <button
          onClick={closeModal}
          className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light border border-red-600"
        >
          Cancelar
        </button>
        <Button
          label="Eliminar empleado"
          Icon={HiOutlineCheckCircle}
          onClick={handleDelete}
          color="bg-red-600"
          textColor="text-white"
        />
      </div>
    </Modal>
  );
}

export default DeleteEmployerModal;
