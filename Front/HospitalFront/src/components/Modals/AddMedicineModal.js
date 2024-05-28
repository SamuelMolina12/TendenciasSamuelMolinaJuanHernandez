import React, { useEffect, useState } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createMedicine, updateMedicine } from '../Datas';

function AddMedicineModal({ closeModal, isOpen, medicine }) {
  const [medicineData, setMedicineData] = useState({
    medicineName: '',
    medicineCost: '',
    medicineQuantity: '',
  });
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    if (medicine) {
      setMedicineData({
        medicineName: medicine.medicineName || '',
        medicineCost: medicine.medicineCost || '',
        medicineQuantity: medicine.medicineQuantity || '',
      });
    } else {
      setMedicineData({
        medicineName: '',
        medicineCost: '',
        medicineQuantity: '',
      });
    }
  }, [medicine]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setMedicineData({ ...medicineData, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      if (medicine) {
        await updateMedicine(medicine.id, medicineData);
        toast.success('Medicina actualizada con éxito');
      } else {
        await createMedicine(medicineData);
        toast.success('Medicina creada con éxito');
      }
      closeModal();
    } catch (error) {
      console.error('Error al guardar la medicina:', error);
      setErrorMessage(error.response?.data?.message || 'Error al guardar la medicina. Por favor, inténtalo de nuevo.');
    }
  };

  return (
    <Modal closeModal={closeModal} isOpen={isOpen} title={medicine ? 'Actualizar Medicina' : 'Crear Medicina'} width="max-w-3xl">
      <Input
        label="Nombre de la medicina"
        name="medicineName"
        value={medicineData.medicineName}
        onChange={handleInputChange}
        placeholder="Ingrese el nombre de la medicina"
        color={true}
      />
      <Input
        label="Costo de la medicina"
        name="medicineCost"
        value={medicineData.medicineCost}
        onChange={handleInputChange}
        placeholder="Ingrese el costo de la medicina"
        color={true}
      />
      <Input
        label="Cantidad"
        name="medicineQuantity"
        value={medicineData.medicineQuantity}
        onChange={handleInputChange}
        placeholder="Ingrese la cantidad de la medicina (mg, ml, etc)"
        color={true}
      />
      {errorMessage && <p className="text-red-600">{errorMessage}</p>}
      <div className="grid sm:grid-cols-2 gap-4 w-full">
        <button onClick={closeModal} className="bg-red-600 bg-opacity-5 text-red-600 text-sm p-4 rounded-lg font-light border border-red-600">
          Cancelar
        </button>
        <Button label="Guardar" Icon={HiOutlineCheckCircle} onClick={handleSubmit} color="bg-subMain" textColor="text-white" />
      </div>
    </Modal>
  );
}

export default AddMedicineModal;
