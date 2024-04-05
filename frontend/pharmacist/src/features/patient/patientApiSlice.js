import { apiSlice } from "../../app/api/apiSlice";

/**
 * patientApiSlice provides API endpoints for managing patient data.
 */
export const patientApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to fetch all patients.
         * @returns A promise containing all patient data.
         */
        getPatient: builder.query({
            query: () => ({
                url: "/api/patient",
                method: "GET",
            }),
        }),
        
        /**
         * Query to fetch a patient by their ID.
         * @param id - ID of the patient.
         * @returns A promise containing the patient data.
         */
        getPatientById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}`,
                method: "GET",
            }),
        }),
        
        /**
         * Mutation to update a patient's data by their ID.
         * @param id - ID of the patient.
         * @param data - Updated patient data.
         * @returns A promise containing the result of the mutation.
         */
        updatePatientById: builder.mutation({
            query: (id, data) => ({
                url: `/api/patient/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        /**
         * Mutation to add a new patient.
         * @param data - Patient data to be added.
         * @returns A promise containing the result of the mutation.
         */
        addPatient: builder.mutation({
            query: (data) => ({
                url: "/api/patient",
                method: "POST",
                body: { ...data },
            }),
        }),

        /**
         * Mutation to delete a patient by their ID.
         * @param id - ID of the patient to delete.
         * @returns A promise containing the result of the mutation.
         */
        deletePatientById: builder.mutation({
            query: (id) => ({
                url: `/api/patient/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetPatientQuery,
    useGetPatientByIdQuery,
    useUpdatePatientByIdMutation,
    useAddPatientMutation,
    useDeletePatientByIdMutation,
} = patientApiSlice;
