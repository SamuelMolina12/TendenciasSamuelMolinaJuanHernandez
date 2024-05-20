import React, { useState, useEffect } from 'react';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';


import AddDiagnosticHelpModal from '../../components/Modals/AddDiagnosticHelpModal';


import DeleteDiagnosticHelpModal from '../../components/Modals/DelDiagnosticHelpModal';

import { DiagnosticHelpTable } from '../../components/Tables';

import { DiagnosticHelpData } from '../../components/Datas';

function DiagnosticHelp() {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [diagnosticHelpData, setDiagnosticHelpData] = useState([]);

    const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
    const [selectedDiagnosticHelp, setSelectedDiagnosticHelp] = useState(null);

    const onCloseModal = async () => {
        setIsModalOpen(false);
        setSelectedDiagnosticHelp(null);
        await getData();
    };

    const onCloseDeleteModal = () => {
        setIsDeleteModalOpen(false);
        setSelectedDiagnosticHelp(null);
    };

    const preview = (id) => {
        const diagnosticHelp = diagnosticHelpData.find(emp => emp.id === id);
        setSelectedDiagnosticHelp(diagnosticHelp);
        setIsModalOpen(true);
    };

    const handleDelete = async (id) => {
        setSelectedDiagnosticHelp(id);
        setIsDeleteModalOpen(true);
    }

    const getData = async () => {
        const data = await DiagnosticHelpData();
        setDiagnosticHelpData(data);
    };

    useEffect(() => {
        getData();
    }, []);

    return (
        <Layout>
            {isModalOpen && (
                <AddDiagnosticHelpModal
                    onClose={onCloseModal}
                    selectedDiagnosticHelp={selectedDiagnosticHelp}
                />
            )}
            {isDeleteModalOpen && (
                <DeleteDiagnosticHelpModal
                    onClose={onCloseDeleteModal}
                    selectedDiagnosticHelp={selectedDiagnosticHelp}
                />
            )}

            <button
                onClick={() => setIsModalOpen(true)}
                className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
            >
                <BiPlus className="text-2xl" />
            </button>
            <h1 className="text-xl font-semibold">Ayudas Diagnosticas</h1>
            <div
                data-aos="fade-up"
                data-aos-duration="1000"
                data-aos-delay="100"
                data-aos-offset="200"
                className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
            >
                <div className="mt-8 w-full overflow-x-scroll">
                    <DiagnosticHelpTable
                        data={diagnosticHelpData}
                        function={{
                            preview: preview,
                            handleDelete: handleDelete
                        }}
                    />
                </div>
            </div>
        </Layout>
    );
}

export default DiagnosticHelp;


