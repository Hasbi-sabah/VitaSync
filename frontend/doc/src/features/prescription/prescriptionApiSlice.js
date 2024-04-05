import { apiSlice } from "../../app/api/apiSlice";

/**
 * prescriptionApiSclice provides API endpoints for managing prescription data.
 */
export const prescriptionApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to fetch patient prescriptions by patient ID.
         * @param id - ID of the patient.
         * @returns A promise containing the patient's prescriptions data.
         */
        getPatientPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/prescription`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to add a prescription for a patient by ID.
         * @param id - ID of the patient.
         * @returns A promise containing the result of the mutation.
         */
        addPatientPrescriptionById: builder.mutation({
            query: (id) => ({
                url: `/api/patient/${id}/prescription`,
                method: "POST"
            }),
        }),
        
        /**
         * Query to fetch a prescription by ID.
         * @param id - ID of the prescription.
         * @returns A promise containing the prescription data.
         */
        getPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to fill a prescription by ID.
         * @param id - ID of the prescription.
         * @returns A promise containing the result of the mutation.
         */
        getPrescriptionFilledById: builder.mutation({
            query: (id) => ({
                url: `/api/prescription/${id}/fill`,
                method: "POST",
            }),
        }),

         /**
         * Mutation to update a prescription by ID.
         * @param id - ID of the prescription.
         * @param data - Prescription data to be updated.
         * @returns A promise containing the result of the mutation.
         */
        updatePrescriptionById: builder.mutation({
            query: (id, data) => ({
                url: `/api/prescription/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        /**
         * Mutation to delete a prescription by ID.
         * @param id - ID of the prescription.
         * @returns A promise containing the result of the mutation.
         */
        deletePrescriptionById: builder.mutation({
            query: (id) => ({
                url: `/api/prescription/${id}`,
                method: "DELETE",
            }),
        }),
        
        /**
         * Query to fetch drugs prescribed in a prescription by ID.
         * @param id - ID of the prescription.
         * @returns A promise containing the drugs prescribed in the prescription data.
         */
        getDrugPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}/drug`,
                method: "GET",
            }),
        }),
        
        /**
         * Query to fetch extended drug information prescribed in a prescription by ID.
         * @param id - ID of the prescription.
         * @returns A promise containing the extended drug information prescribed in the prescription data.
         */
        getDrugPrescriptionExtendedById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}/drug_extended`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to add a drug prescription to a prescription by ID.
         * @param id - ID of the prescription.
         * @param data - Drug prescription data to be added.
         * @returns A promise containing the result of the mutation.
         */
        addDrugPrescriptionById: builder.mutation({
            query: (id, data) => ({
                url: `/api/prescription/${id}/drug`,
                method: "POST",
                body: { ...data }
            }),
        }),
        
        /**
         * Query to fetch a prescription drug by ID.
         * @param id - ID of the prescription drug.
         * @returns A promise containing the prescription drug data.
         */
        getPrescriptionDrugById: builder.query({
            query: (id) => ({
                url: `/api/prescription_drug/${id}`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to update a prescription drug by ID.
         * @param id - ID of the prescription drug.
         * @param data - Prescription drug data to be updated.
         * @returns A promise containing the result of the mutation.
         */
        updatePrescriptionDrugById: builder.mutation({
            query: (id, data) => ({
                url: `/api/prescription_drug/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),
        
        /**
         * Mutation to delete a prescription drug by ID.
         * @param id - ID of the prescription drug.
         * @returns A promise containing the result of the mutation.
         */
        deletePrescriptionDrugById: builder.mutation({
            query: (id) => ({
                url: `/api/prescription_drug/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetPatientPrescriptionByIdQuery,
    useAddPatientPrescriptionByIdMutation,
    useGetPrescriptionFilledByIdMutation,
    useGetPrescriptionByIdQuery,
    useGetDrugPrescriptionExtendedByIdQuery,
    useUpdatePrescriptionByIdMutation,
    useDeletePrescriptionByIdMutation,
    useGetDrugPrescriptionByIdQuery,
    useAddDrugPrescriptionByIdMutation,
    useGetPrescriptionDrugByIdQuery,
    useUpdatePrescriptionDrugByIdMutation,
    useDeletePrescriptionDrugByIdMutation,
} = prescriptionApiSclice;
