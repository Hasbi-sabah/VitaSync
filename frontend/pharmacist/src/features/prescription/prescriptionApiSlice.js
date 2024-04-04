import { apiSlice } from "../../app/api/apiSlice";

export const prescriptionApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/prescription`,
                method: "GET",
            }),
        }),

        addPatientPrescriptionById: builder.mutation({
            query: (id) => ({
                url: `/api/patient/${id}/prescription`,
                method: "POST"
            }),
        }),
        
        getPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}`,
                method: "GET",
            }),
        }),

        getPrescriptionFilledById: builder.mutation({
            query: (id) => ({
                url: `/api/prescription/${id}/fill`,
                method: "POST",
            }),
        }),

        updatePrescriptionById: builder.mutation({
            query: (id, data) => ({
                url: `/api/prescription/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        deletePrescriptionById: builder.mutation({
            query: (id) => ({
                url: `/api/prescription/${id}`,
                method: "DELETE",
            }),
        }),
        
        getDrugPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}/drug`,
                method: "GET",
            }),
        }),
        
        getDrugPrescriptionExtendedById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}/drug_extended`,
                method: "GET",
            }),
        }),

        addDrugPrescriptionById: builder.mutation({
            query: (id, data) => ({
                url: `/api/prescription/${id}/drug`,
                method: "POST",
                body: { ...data }
            }),
        }),
        
        getPrescriptionDrugById: builder.query({
            query: (id) => ({
                url: `/api/prescription_drug/${id}`,
                method: "GET",
            }),
        }),

        updatePrescriptionDrugById: builder.mutation({
            query: (id, data) => ({
                url: `/api/prescription_drug/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),
        
        deletePrescriptionDrugById: builder.mutation({
            query: (id) => ({
                url: `/api/prescription_drug/${id}`,
                method: "DELETE",
            }),
        }),
        // I don't really understand the other endpoint (Ask Sabah)
        // For now I think doctor only needs to post
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
