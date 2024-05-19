import React, { useState } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createEmployer } from '../Datas';

function AddDoctorModal({ closeModal, isOpen }) {
  const [employeeData, setEmployeeData] = useState({
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

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEmployeeData({ ...employeeData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      const response = await createEmployer(employeeData);
      console.log('Empleado creado:', response);
      toast.success('Empleado creado con éxito');
      closeModal();
    } catch (error) {
      console.error('Error al crear el empleado:', error);
      setErrorMessage(error.response?.data?.message || 'Error al crear el empleado. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title="Crear Empleado"
      width="max-w-3xl"
    >
      {/* Campos del formulario */}
      <Input
        label="Cédula"
        name="id"
        value={employeeData.id}
        onChange={handleInputChange}
        placeholder="Ingrese la cédula"
        color={true}
      />
      <Input
        label="Nombre Completo"
        name="name"
        value={employeeData.name}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre completo"
        color={true}
      />
      <Input
        label="Género"
        name="genre"
        value={employeeData.genre}
        onChange={handleInputChange}
        placeholder="Ingrese el género"
        color={true}
      />

      <Input
        label="Correo Electrónico"
        name="mail"
        value={employeeData.mail}
        onChange={handleInputChange}
        placeholder="Ingrese el correo electrónico"
        color={true}
      />
      <Input
        label="Teléfono"
        name="telephone"
        value={employeeData.telephone}
        onChange={handleInputChange}
        placeholder="Ingrese el número de teléfono"
        color={true}
      />
      <Input
        label="Fecha de Nacimiento"
        name="birth"
        value={employeeData.birth}
        onChange={handleInputChange}
        placeholder="Ingrese la fecha de nacimiento"
        color={true}
      />
      <Input
        label="Dirección"
        name="address"
        value={employeeData.address}
        onChange={handleInputChange}
        placeholder="Ingrese la dirección"
        color={true}
      />
      <Input
        label="Rol"
        name="role"
        value={employeeData.role}
        onChange={handleInputChange}
        placeholder="Ingrese el rol"
        color={true}
      />
      <Input
        label="Nombre de Usuario"
        name="userName"
        value={employeeData.userName}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre de usuario"
        color={true}
      />
      <Input
        label="Contraseña"
        name="password"
        value={employeeData.password}
        onChange={handleInputChange}
        placeholder="Ingrese la contraseña"
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

export default AddDoctorModal;
