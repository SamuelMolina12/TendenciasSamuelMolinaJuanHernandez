import React, { useState,useEffect } from 'react';
import Modal from './Modal';
import { Button, Input } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createBilling } from '../Datas';
import moment from 'moment';

function AddBillingModal({ onClose, isOpen, billing }) {
    const [formData, setFormData] = useState({
        patient_id: '',
        doctor_id: '',
        order_id: ''
    });

    useEffect(() => {
        if (billing) {
            setFormData({
                patient_id: billing.patient_id || '',
                doctor_id: billing.doctor_id || '',
                order_id: billing.order_id || ''
            });
        }
    }, [billing]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };


const handleSubmit = async () => {
    try {
        const formattedData = {
            patient_id: formData.patient_id,
            doctor_id: formData.doctor_id,
            order_id: formData.order_id
        };

        await createBilling(formattedData);
        toast.success('Factura creada con éxito');
        onClose();
    } catch (error) {
        toast.error('Error al guardar la factura. Por favor, inténtalo de nuevo.');
    }
};

return (
    <Modal
        closeModal={onClose}
        isOpen={isOpen}
        title={"Nueva Factura"}
        width="max-w-3xl"
    >
        <Input
            label="Cedula del paciente"
            name="patient_id"
            value={formData.patient_id}
            onChange={handleInputChange}
            placeholder="Cedula del paciente"
            color={true}
        />
        <Input
            label="Cedula del doctor"
            name="doctor_id"
            value={formData.doctor_id}
            onChange={handleInputChange}
            placeholder="Cedula del doctor"
            color={true}
        />
        <Input
            label="Id de la orden"
            name="order_id"
            value={formData.order_id}
            onChange={handleInputChange}
            placeholder="Id de la orden"
            color={true}
        />
        <div className="grid sm:grid-cols-2 gap-4 w-full">
            <button
                onClick={onClose}
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

export default AddBillingModal;






      
