import React, { useState } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createSpecialist } from '../Datas';

function AddSpecialistModal({ closeModal, isOpen }) {
  const [specialistData, setSpecialistData] = useState({
    nameSpecialist: '',
  });
  const [errorMessage, setErrorMessage] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSpecialistData({ ...specialistData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      const response = await createSpecialist(specialistData);
      console.log('Especialista creado:', response);
      toast.success('Especialista creado con éxito');
      closeModal();
    } catch (error) {
      console.error('Error al crear el especialista:', error);
      setErrorMessage(error.response?.data?.message || 'Error al crear el especialista. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title="Crear Especialista"
      width="max-w-3xl"
    >
      {/* Campos del formulario */}
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

export default AddSpecialistModal;
