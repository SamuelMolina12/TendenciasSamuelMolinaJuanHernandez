import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createProcedure, updateProcedure } from '../Datas'; 

function AddProcedureModal({ closeModal, isOpen, procedure }) {
  const [procedureData, setProcedureData] = useState({
    procedureName: '',
    procedureCost: ''
  });

  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    if (procedure) {
      setProcedureData({
        procedureName: procedure.procedureName || '',
        procedureCost: procedure.procedureCost || ''
      });
    }
  }, [procedure]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProcedureData({ ...procedureData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      if (procedure) {
        await updateProcedure(procedure.id, procedureData);
        toast.success('Procedimiento actualizado con éxito');
      } else {
        await createProcedure(procedureData);
        toast.success('Procedimiento creado con éxito');
      }
      closeModal();
    } catch (error) {
      console.error('Error al guardar el procedimiento:', error);
      setErrorMessage(error.response?.data?.message || 'Error al guardar el procedimiento. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title={procedure ? 'Actualizar Procedimiento' : 'Crear Procedimiento'}
      width="max-w-3xl"
    >
      <Input
        label="Nombre del Procedimiento"
        name="procedureName"
        value={procedureData.procedureName}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre del procedimiento"
        color={true}
      />
      <Input
        label="Costo del Procedimiento"
        name="procedureCost"
        value={procedureData.procedureCost}
        onChange={handleInputChange}
        placeholder="Ingrese el costo del procedimiento"
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

export default AddProcedureModal;
