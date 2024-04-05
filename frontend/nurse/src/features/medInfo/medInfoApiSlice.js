import { apiSlice } from "../../app/api/apiSlice";

/**
 * MedInfoApiSlice provides API endpoints for managing patient medical information.
 */
export const MedInfoApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to fetch medical information of a patient by their ID.
         * @param id - ID of the patient.
         * @returns A promise containing the patient's medical information.
         */
        getPatientMedInfoById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/info`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to add medical information for a patient.
         * @param data - Array containing patient ID and medical information.
         * @returns A promise containing the result of the mutation.
         */
        addPatientMedInfoById: builder.mutation({
            query: (data) => ({
                url: `/api/patient/${data[0]}/info`,
                method: "POST",
                body: { ...data[1] },
            }),
        }),

        /**
         * Mutation to delete medical information by its ID.
         * @param id - ID of the medical information to delete.
         * @returns A promise containing the result of the mutation.
         */
        deleteMedInfoById: builder.mutation({
            query: (id) => ({
                url: `/api/med_info/${id}`,
                method: "DELETE",
            }),
        }),

        /**
         * Query to fetch medical information by its ID.
         * @param id - ID of the medical information.
         * @returns A promise containing the medical information.
         */
        getMedInfoById: builder.query({
            query: (id) => ({
                url: `/api/med_info/${id}`,
                method: "GET",
            }),
        }),
    }),
});

export const {
    useGetPatientMedInfoByIdQuery,
    useAddPatientMedInfoByIdMutation,
    useDeleteMedInfoByIdMutation,
    useGetMedInfoByIdQuery,
} = MedInfoApiSlice;
