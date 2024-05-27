import React, { useState, useEffect } from 'react';
import { sortsDatas, updatePatient } from '../Datas';
import { Button, Input, Select } from '../Form';
import { toast } from 'react-hot-toast';
import { HiOutlineCheckCircle } from 'react-icons/hi';

function PersonalInfo({ patientData }) {
  const [title, setTitle] = useState(sortsDatas.title[0]);
  const [formData, setFormData] = useState({
    id: '',
    name: '',
    genre: '',
    mail: '',
    telephone: '',
    birth: '',
    address: '',
    emergencyContact: {
      nameC: '',
      relationship: '',
      telephoneC: '',
    },
    Policy: {
      insuranceCompany: '',
      policyNumber: '',
      statePolicy: '',
      termPolicy: '',
    }
  });

  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    if (patientData) {
      setFormData({
        id: patientData.id || '',
        name: patientData.name || '',
        genre: patientData.genre || '',
        mail: patientData.mail || '',
        telephone: patientData.telephone || '',
        birth: patientData.birth || '',
        address: patientData.address || '',
        emergencyContact: patientData.emergencyContact || {
          nameC: '',
          relationship: '',
          telephoneC: '',
        },
        Policy: patientData.Policy || {
          insuranceCompany: '',
          policyNumber: '',
          statePolicy: '',
          termPolicy: '',
        }
      });
    }
  }, [patientData]);

  const genreOptions = [
    { title: 'Masculino', onClick: () => handleGenreChange('Masculino') },
    { title: 'Femenino', onClick: () => handleGenreChange('Femenino') },
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    const keys = name.split('.');

    if (keys.length > 1) {
      setFormData(prevState => {
        const updatedData = { ...prevState };
        let nestedData = updatedData;
        for (let i = 0; i < keys.length - 1; i++) {
          nestedData = nestedData[keys[i]];
        }
        nestedData[keys[keys.length - 1]] = value;
        return updatedData;
      });
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleGenreChange = (genre) => {
    setFormData({ ...formData, genre });
  };

  const handleSubmit = async () => {
    try {
      const dataToSubmit = { ...formData };
      dataToSubmit.telephone = String(dataToSubmit.telephone);
      dataToSubmit.emergencyContact.telephoneC = String(dataToSubmit.emergencyContact.telephoneC);
  
      if (!dataToSubmit.id) {
        throw new Error('ID del paciente no proporcionado.');
      }
  
      await updatePatient(dataToSubmit.id, dataToSubmit);
      toast.success('Paciente actualizado con éxito');
    } catch (error) {
      toast.error('Error al actualizar el paciente. Por favor, inténtalo de nuevo.');
      setErrorMessage(error.response?.data?.message || error.message || 'Error al actualizar el paciente. Por favor, inténtalo de nuevo.');
      console.error(error);
    }
  };

  return (
    <div className="flex-colo gap-4">
      <Input
        label="Nombre Completo"
        name="name"
        value={formData.name}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre completo"
        color={true}
      />

      {/* Dropdown de género */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Género</label>
        <Select datas={genreOptions} item={formData.genre}>
          
            <span>{formData.genre || 'Seleccione Género'}</span>
  
        </Select>
      </div>

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
        placeholder="Ingrese el teléfono"
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

      <h3 className="text-lg font-medium text-gray-900">Contacto de Emergencia</h3>
      <Input
        label="Nombre del Contacto"
        name="emergencyContact.nameC"
        value={formData.emergencyContact.nameC}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del contacto"
        color={true}
      />
      <Input
        label="Relación"
        name="emergencyContact.relationship"
        value={formData.emergencyContact.relationship}
        onChange={handleInputChange}
        placeholder="Ingrese la relación"
        color={true}
      />
      <Input
        label="Teléfono del Contacto"
        name="emergencyContact.telephoneC"
        value={formData.emergencyContact.telephoneC}
        onChange={handleInputChange}
        placeholder="Ingrese el teléfono del contacto"
        color={true}
      />

      <h3 className="text-lg font-medium text-gray-900">Información de la Póliza</h3>
      <Input
        label="Compañía de Seguros"
        name="Policy.insuranceCompany"
        value={formData.Policy.insuranceCompany}
        onChange={handleInputChange}
        placeholder="Ingrese la compañía de seguros"
        color={true}
      />
      <Input
        label="Número de Póliza"
        name="Policy.policyNumber"
        value={formData.Policy.policyNumber}
        onChange={handleInputChange}
        placeholder="Ingrese el número de póliza"
        color={true}
      />
      <Input
        label="Estado de la Póliza"
        name="Policy.statePolicy"
        value={formData.Policy.statePolicy}
        onChange={handleInputChange}
        placeholder="Ingrese el estado de la póliza"
        color={true}
      />
      <Input
        label="Término de la Póliza"
        name="Policy.termPolicy"
        value={formData.Policy.termPolicy}
        onChange={handleInputChange}
        placeholder="Ingrese el término de la póliza"
        color={true}
      />

      {errorMessage && <div className="text-red-600">{errorMessage}</div>}
      <Button
        label={'Guardar Cambios'}
        onClick={handleSubmit}
        className="w-full flex justify-center items-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-main hover:bg-main focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-main"
      />
    </div>
  );
}

export default PersonalInfo;
