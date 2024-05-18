import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { updateEmployer } from '../Datas'; // Corregido el nombre de importación

function Updatedemployer({ closeModal, isOpen, employerData }) {
  const [updatedEmployerData, setUpdatedEmployerData] = useState({
    id: '',
    name: '',
    genre: '',
    mail: '',
    telephone: '',
    birth: '',
    address: '',
    role: '',
    userName: '',
    password: '' 
  });

  useEffect(() => {
    if (employerData) {
      setUpdatedEmployerData(employerData); 
    }
  }, [employerData]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUpdatedEmployerData({ ...updatedEmployerData, [name]: value }); 
  };

  const handleSubmit = async () => {
    try {
      const updatedData = await updateEmployer(updatedEmployerData); 
      console.log('Empleado actualizado:', updatedData);
      toast.success('Empleado actualizado con éxito.');
      closeModal();
    } catch (error) {
      console.error('Error al actualizar el empleado:', error);
      toast.error('Error al actualizar el empleado. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title="Actualizar Empleado"
      width="max-w-3xl"
    >
      <div className="p-4">
        <Input
          label="Nombre Completo"
          name="name"
          value={updatedEmployerData.name}
          onChange={handleInputChange}
        />
        <Input
          label="Género"
          name="genre"
          value={updatedEmployerData.genre}
          onChange={handleInputChange}
        />

        <div className="mt-4 flex justify-end">
          <Button
            label="Guardar"
            Icon={HiOutlineCheckCircle}
            onClick={handleSubmit}
          />
        </div>
      </div>
    </Modal>
  );
}

export default Updatedemployer;
