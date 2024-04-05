import { apiSlice } from "../../app/api/apiSlice";

/**
 * prescDrugApiSclice provides API endpoints for managing prescription drugs data.
 */
export const prescDrugApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to fetch prescription drugs by prescription ID.
         * @param id - ID of the prescription.
         * @returns A promise containing the prescription drugs data.
         */
        getPrescriptionDrugsById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}/drug`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to add prescription drugs to a prescription by ID.
         * @param id - ID of the prescription.
         * @param data - Prescription drugs data to be added.
         * @returns A promise containing the result of the mutation.
         */
        addPrescriptionDrugsById: builder.mutation({
            query: ({id, data}) => ({
                url: `/api/prescription/${id}/drug`,
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),
    }),
});

export const {
    useGetPrescriptionDrugsByIdQuery,
    useAddPrescriptionDrugsByIdMutation,
} = prescDrugApiSclice;
