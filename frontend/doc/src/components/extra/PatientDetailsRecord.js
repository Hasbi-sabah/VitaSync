import React, { useState, useEffect } from 'react';
import { useGetProcedurePerformeddByIdMutation } from "../../features/procedure/procedureApiSlice";
import { useGetPrescriptionDrugsByIdQuery } from "../../features/prescDrug/prescDrugApiSlice"
import { useGetDrugQuery } from '../../features/drug/drugApiSlice'
import LoadingScreen from '../LoadingScreen';

const PatientDetailsRecord = ({ data }) => {
    const [sendProcedureRequest, { isLoading: isSendingRequest }] = useGetProcedurePerformeddByIdMutation();
    const [requestSent, setRequestSent] = useState(false);
    const sendRequest = () => {
        if (!data.status && !requestSent) {
          sendProcedureRequest(data.id)
            .unwrap()
            .then(() => {
              setRequestSent(true);
            })
            .catch((error) => {
              // Handle error
              alert('Failed to send request:', error);
            });
        }
     };
     const { data: prsc, isLoading: isPrscDataLoading } = useGetPrescriptionDrugsByIdQuery(data.prescriptionId);
     const { data: drugsData, isLoading: isDrugsDataLoading } = useGetDrugQuery();

     let mergedArray = []
     useEffect(() => {
        if (!isPrscDataLoading && !isDrugsDataLoading) {
            mergedArray = prsc.map(prescription => {
                const matchedDrug = drugsData.find(drug => drug.id === prescription.drugId);
                return { ...prescription, ...matchedDrug };
            });
        }
     }, [isDrugsDataLoading, isPrscDataLoading]);
        console.log(mergedArray)
        
        const [drugs, setDrugs] = useState([]);
        const [isLoading, setIsLoading] = useState(true);
       
        useEffect(() => {
           if (prsc && drugsData) {
            setDrugs(drugsData);
             setIsLoading(false);
           }
        }, [prsc, drugsData])
          
        if (isLoading) {
            return (
                <div className='h-128 h-128'>
                    <LoadingScreen />
                </div>
            );
        }
        if (prsc && drugsData) {
          const mergedArray = prsc.map(obj1 => {
            const matchedObj = drugsData.find(obj2 => obj1.drugId === obj2.id);
            return { ...obj1, ...matchedObj };
          });
          return (
            <div className="w-screen sm:w-128">
              <div className="grid sm:items-center lg:items-baseline">
                {mergedArray && mergedArray.length > 0 && <div className="bg-white rounded-lg mt-5 w-full">
                    <h2 className="text-center text-2xl font-meduim">Prescriptions</h2>
                    <hr />
                    <div className="table w-full">
                        <div className="table-header-group w-full">
                            <div className="table-row w-full bg-gray">
                                <div className="table-cell text-center">Drug</div>
                                <div className="table-cell text-center">Instructions</div>
                            </div>
                        </div>
                        <div className="table-row-group w-full">
                        {mergedArray && (mergedArray).map((item, idx) =>
                            <div className="table-row w-full" key={idx}>
                                <div className="table-cell text-center">{item.activeIngredient}</div>
                                <div className="table-cell text-left">{item.instructions}</div>
                            </div>
                        )}
                        </div>
                    </div>
                </div>}
                {data.diagnosis && <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
                    <h2 className="text-center text-2xl font-meduim">Diagnosis</h2>
                    <hr />
                    {data.diagnosis}
                </div>}
                {data.notes && <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
                    <h2 className="text-center text-2xl font-meduim">Notes</h2>
                    <hr />
                    {data.notes}
                </div>}
                {data.name && <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
                    <div className="flex justify">
                    <h2 className="text-center text-2xl font-meduim">Procedures</h2>
                    <button className="bg-blue hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={sendRequest} disabled={data.status || requestSent || isSendingRequest}>
                        {data.status || requestSent ? 'Performed' : 'Mark as performed'}
                    </button>
                    </div>
                    <hr />
                    {data.name}
                </div>}
                {data.vaccine && data.vaccine.length > 0 && <div className="bg-white rounded-sm mx-auto w-full mt-5 ">
                    <h2 className="text-center text-2xl font-meduim">Vaccine</h2>
                    <hr />
                    <div className="table w-full">
                        <div className="table-header-group w-full">
                            <div className="table-row w-full bg-gray">
                                <div className="table-cell text-center">Drug</div>
                                <div className="table-cell text-center">Dosage</div>
                            </div>
                        </div>
                        <div className="table-row-group w-full">
                        {data.vaccine && (data.vaccine).map((item, idx) =>
                            <div className="table-row w-full" key={idx}>
                                <div className="table-cell text-center">{item.drug}</div>
                                <div className="table-cell text-left">{item.dosage}</div>
                            </div>
                        )}
                        </div>
                    </div>
                </div>}
              </div>
            </div>
          );
        }

};

export default PatientDetailsRecord;
