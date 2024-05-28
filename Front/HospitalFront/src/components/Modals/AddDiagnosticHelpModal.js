import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createDiagnosticHelp, updateDiagnosticHelp } from '../Datas';

function AddDiagnosticHelpModal({ closeModal, isOpen, diagnosticHelpData }) {
    const [formData, setFormData] = useState({
        diagnosticName: '',
        diagnosticCost: '',
    });

    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        if (diagnosticHelpData) {
            setFormData({
                diagnosticName: diagnosticHelpData.diagnosticName || '',
                diagnosticCost: diagnosticHelpData.diagnosticCost || '',
            });
        }
    }, [diagnosticHelpData]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    }

    const handleSubmit = async () => {
        if (!formData.diagnosticName || !formData.diagnosticCost) {
          setErrorMessage('Por favor, completa todos los campos.');
          return;
        }
        
        try {
          const dataToSubmit = {
            diagnosticName: formData.diagnosticName,
            diagnosticCost: parseFloat(formData.diagnosticCost),
          };
          
          if (isNaN(dataToSubmit.diagnosticCost)) {
            setErrorMessage('El costo debe ser un número válido.');
            return;
          }
      
          if (diagnosticHelpData) {
            await updateDiagnosticHelp(diagnosticHelpData.id, dataToSubmit);
            toast.success('Ayuda diagnóstica actualizada con éxito');
          } else {
            await createDiagnosticHelp(dataToSubmit);
            toast.success('Ayuda diagnóstica creada con éxito');
          }
          closeModal();
        } catch (error) {
          toast.error('Error al guardar la ayuda diagnóstica. Por favor, inténtalo de nuevo.');
          setErrorMessage('Error al guardar la ayuda diagnóstica. Por favor, inténtalo de nuevo.');
        }
      };

    return (
        <Modal
            closeModal={closeModal}
            isOpen={isOpen}
            title={diagnosticHelpData ? 'Actualizar Ayuda diagnostica' : 'Crear Ayuda diagnostica'}
            width="max-w-3xl"
        >
            <Input
                label="Nombre de la ayuda diagnostica"
                name="diagnosticName"
                value={formData.diagnosticName}
                onChange={handleInputChange}
                placeholder={"Ingrese el nombre de la ayuda diagnostica"}
                color={true}
            />
            <Input
                label="Costo de la ayuda diagnostica"
                name="diagnosticCost"
                value={formData.diagnosticCost}
                onChange={handleInputChange}
                placeholder={"Ingrese el costo de la ayuda diagnostica"}
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

export default AddDiagnosticHelpModal;
