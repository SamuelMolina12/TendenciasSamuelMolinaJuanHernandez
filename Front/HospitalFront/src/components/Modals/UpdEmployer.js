import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { updateEmployer } from '../Datas';

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

  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    if (employerData) {
      setUpdatedEmployerData(employerData); 
    }
  }, [employerData]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    // Si el nombre es "telephone", convierte el valor a string
    const updatedValue = name === 'telephone' ? String(value) : value;
    setUpdatedEmployerData({ ...updatedEmployerData, [name]: updatedValue }); 
  };

  const handleSubmit = async () => {
    try {
      const { id, ...dataToUpdate } = updatedEmployerData; // Excluir el id

      dataToUpdate.telephone = String(dataToUpdate.telephone);
      console.log('Datos que se van a enviar:', dataToUpdate); // Log de los datos que se envían
      const updatedData = await updateEmployer(id, dataToUpdate); // Pasar el id por separado
      console.log('Empleado actualizado:', updatedData);
      toast.success('Empleado actualizado con éxito.');
      closeModal();
    } catch (error) {
      console.error('Error al actualizar el empleado:', error);
      setErrorMessage(error.response?.data?.message || 'Error al actualizar el empleado. Por favor, inténtalo de nuevo.');
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
          label="ID"
          name="id"
          value={updatedEmployerData.id}
          onChange={handleInputChange}
          color={true}
          disabled={true} 
        />
        <Input
          label="Nombre Completo"
          name="name"
          value={updatedEmployerData.name}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Género"
          name="genre"
          value={updatedEmployerData.genre}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Correo Electrónico"
          name="mail"
          value={updatedEmployerData.mail}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Teléfono"
          name="telephone"
          value={updatedEmployerData.telephone}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Fecha de Nacimiento"
          name="birth"
          value={updatedEmployerData.birth}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Dirección"
          name="address"
          value={updatedEmployerData.address}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Rol"
          name="role"
          value={updatedEmployerData.role}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Nombre de Usuario"
          name="userName"
          value={updatedEmployerData.userName}
          onChange={handleInputChange}
          color={true}
        />
        <Input
          label="Contraseña"
          name="password"
          value={updatedEmployerData.password}
          onChange={handleInputChange}
          type="password"
          color={true}
        />
        {errorMessage && <p className="text-red-600 mt-2">{errorMessage}</p>}
        <div className="mt-4 flex justify-end">
          <Button
            label="Actualizar"
            Icon={HiOutlineCheckCircle}
            onClick={handleSubmit}
          />
        </div>
      </div>
    </Modal>
  );
}

export default Updatedemployer;
