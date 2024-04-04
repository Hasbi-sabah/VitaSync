import { apiSlice } from "../../app/api/apiSlice";

export const prescriptionApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/prescription`,
                method: "GET",
            }),
        }),

        getPatientPrescriptionExtendedById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/prescription_extended`,
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

        getPrintPrescriptionById: builder.query({
            query: (id) => ({
                url: `/api/print_prescription/${id}`,
                method: "GET",
                headers: {
                    'Accept': 'application/pdf',
                  },
            }),
            transformResponse: (response) => {
                if (response.ok) {
                    return response.blob(); // Handle the response as a Blob
                } else {
                    throw new Error('Network response was not ok');
                }
            },
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
    useGetPrescriptionByIdQuery,
    useGetPrintPrescriptionByIdQuery,
    useGetPatientPrescriptionExtendedByIdQuery,
    useGetDrugPrescriptionExtendedByIdQuery,
    useUpdatePrescriptionByIdMutation,
    useDeletePrescriptionByIdMutation,
    useGetDrugPrescriptionByIdQuery,
    useAddDrugPrescriptionByIdMutation,
    useGetPrescriptionDrugByIdQuery,
    useUpdatePrescriptionDrugByIdMutation,
    useDeletePrescriptionDrugByIdMutation,
} = prescriptionApiSclice;
