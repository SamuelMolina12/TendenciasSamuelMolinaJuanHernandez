import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createEmployer, updateEmployer } from '../Datas';

function AddDoctorModal({ closeModal, isOpen, employerData }) {
  const [formData, setFormData] = useState({
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
      setFormData({
        id: employerData.id || '',
        name: employerData.name || '',
        genre: employerData.genre || '',
        mail: employerData.mail || '',
        telephone: employerData.telephone || '',
        birth: employerData.birth || '',
        address: employerData.address || '',
        role: employerData.role || '',
        userName: employerData.userName || '',
        password: employerData.password ||''
      });
    }
  }, [employerData]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      const dataToSubmit = { ...formData };
      dataToSubmit.telephone = String(dataToSubmit.telephone); // Convertir teléfono a string

      if (employerData) {
        await updateEmployer(employerData.id, dataToSubmit);
        toast.success('Empleado actualizado con éxito');
      } else {
        await createEmployer(dataToSubmit);
        toast.success('Empleado creado con éxito');
      }
      closeModal();
    } catch (error) {
      console.error('Error al guardar el empleado:', error);
      toast.error('Error al guardar el empleado. Por favor, inténtalo de nuevo.');
      setErrorMessage(error.response?.data?.message || 'Error al guardar el empleado. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title={employerData ? 'Actualizar Empleado' : 'Crear Empleado'}
      width="max-w-3xl"
    >
      {/* Campos del formulario */}
      <Input
        label="Cédula"
        name="id"
        value={formData.id}
        onChange={handleInputChange}
        placeholder="Ingrese la cédula"
        color={true}
      />
      <Input
        label="Nombre Completo"
        name="name"
        value={formData.name}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre completo"
        color={true}
      />
      <Input
        label="Género"
        name="genre"
        value={formData.genre}
        onChange={handleInputChange}
        placeholder="Ingrese el género"
        color={true}
      />
      <Input
        label="Correo Electrónico"
        name="mail"
        value={formData.mail}
        onChange={handleInputChange}
        placeholder="Ingrese el correo electrónico"
        color={true}
      />
      <Input
        label="Teléfono"
        name="telephone"
        value={formData.telephone}
        onChange={handleInputChange}
        placeholder="Ingrese el número de teléfono"
        color={true}
      />
      <Input
        label="Fecha de Nacimiento"
        name="birth"
        value={formData.birth}
        onChange={handleInputChange}
        placeholder="Ingrese la fecha de nacimiento"
        color={true}
      />
      <Input
        label="Dirección"
        name="address"
        value={formData.address}
        onChange={handleInputChange}
        placeholder="Ingrese la dirección"
        color={true}
      />
      <Input
        label="Rol"
        name="role"
        value={formData.role}
        onChange={handleInputChange}
        placeholder="Ingrese el rol"
        color={true}
      />
      <Input
        label="Nombre de Usuario"
        name="userName"
        value={formData.userName}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre de usuario"
        color={true}
      />
      {/* Mostrar el campo de contraseña tanto en crear como en actualizar */}
      <Input
        label="Contraseña"
        name="password"
        value={formData.password}
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
