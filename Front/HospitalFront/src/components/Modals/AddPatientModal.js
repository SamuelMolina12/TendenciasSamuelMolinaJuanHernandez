import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { Button, Input, Select } from '../Form';
import { HiOutlineCheckCircle } from 'react-icons/hi';
import { toast } from 'react-hot-toast';
import { createPatient } from '../Datas';

function AddPatientModal({ closeModal, isOpen, patientData }) {
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

    const genreOptions = [
        { title: 'Masculino', onClick: () => handleGenreChange('Masculino') },
        { title: 'Femenino', onClick: () => handleGenreChange('Femenino') },
    ];

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
                emergencyContact: {
                    nameC: patientData.emergencyContact?.nameC || '',
                    relationship: patientData.emergencyContact?.relationship || '',
                    telephoneC: patientData.emergencyContact?.telephoneC || '',
                },
                Policy: {
                    insuranceCompany: patientData.Policy?.insuranceCompany || '',
                    policyNumber: patientData.Policy?.policyNumber || '',
                    statePolicy: patientData.Policy?.statePolicy || '',
                    termPolicy: patientData.Policy?.termPolicy || '',
                }
            });
        }
    }, [patientData]);

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

            await createPatient(dataToSubmit);
            toast.success('Paciente creado con éxito');
            closeModal();
        } catch (error) {
            toast.error('Error al crear el paciente. Por favor, inténtalo de nuevo.');
            setErrorMessage(error.response?.data?.message || 'Error al guardar el Paciente. Por favor, inténtalo de nuevo.');
        }
    };

    return (
        <Modal
            closeModal={closeModal}
            isOpen={isOpen}
            title={patientData ? 'Editar Paciente' : 'Agregar Paciente'}
            width="max-w-3xl"
        >
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

            {/* Dropdown de género */}
            <div className="mb-4">
                <label className="block text-sm font-medium text-gray-700">Género</label>
                <Select datas={genreOptions} item={formData.genre}>
                    <button className="w-full bg-transparent text-sm px-4 py-2 border border-gray-300 rounded-lg focus:border focus:border-subMain flex justify-between items-center">
                        {formData.genre || 'Seleccione un género'}
                    </button>
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

            {!patientData && (
                <>
                    <Input
                        label="Contacto de Emergencia"
                        name="emergencyContact.nameC"
                        value={formData.emergencyContact.nameC}
                        onChange={handleInputChange}
                        placeholder="Ingrese el nombre del contacto de emergencia"
                        color={true}
                    />
                    <Input
                        label="Parentesco"
                        name="emergencyContact.relationship"
                        value={formData.emergencyContact.relationship}
                        onChange={handleInputChange}
                        placeholder="Ingrese el parentesco"
                        color={true}
                    />
                    <Input
                        label="Teléfono de Emergencia"
                        name="emergencyContact.telephoneC"
                        value={formData.emergencyContact.telephoneC}
                        onChange={handleInputChange}
                        placeholder="Ingrese el teléfono de emergencia"
                        color={true}
                    />

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
                </>
            )}

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

export default AddPatientModal;