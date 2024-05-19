import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { updateSpecialist } from '../Datas';

function UpdSpecialistModal({ closeModal, isOpen, specialist, onUpdateSuccess }) {
  const [specialistData, setSpecialistData] = useState({
    nameSpecialist: '',
  });
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    if (specialist) {
      setSpecialistData(specialist);
    }
  }, [specialist]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSpecialistData({ ...specialistData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      const response = await updateSpecialist(specialist.id, specialistData);
      console.log('Especialista actualizado:', response);
      toast.success('Especialista actualizado con éxito');
      onUpdateSuccess();
      closeModal();
    } catch (error) {
      console.error('Error al actualizar el especialista:', error);
      setErrorMessage(error.response?.data?.message || 'Error al actualizar el especialista. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title="Actualizar Especialista"
      width="max-w-3xl"
    >
      <Input
        label="Nombre Especialista"
        name="nameSpecialist"
        value={specialistData.nameSpecialist}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del especialista"
        color={true}
      />

      {errorMessage && <p className="text-red-600">{errorMessage}</p>}

      <div className="grid sm:grid-cols-2 gap-4 w-full">
        <button
          onClick={closeModal}
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

export default UpdSpecialistModal;
