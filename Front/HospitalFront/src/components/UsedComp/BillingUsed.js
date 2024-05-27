import { useEffect ,useState } from 'react';
import { BillingDataPatient } from '../../components/Datas';
import { BillingTable } from '../../components/Tables';

function BillingUsed({patientId}) {

  const [billing, setBilling] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (patientId) {
        try {
          const billingData = await BillingDataPatient(patientId);
          setBilling(billingData);
        } catch (error) {
          console.error('Error:', error);
        }
      }
    };
    fetchData();
  }, [patientId]);

return (
    <div className="w-full">
      <h1 className="text-sm font-medium mb-6">Facturas del paciente</h1>
      <div className="w-full overflow-x-scroll">
        <BillingTable data={billing} />
      </div>
    </div>
  );
}

export default BillingUsed;
