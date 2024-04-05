import { apiSlice } from "../../app/api/apiSlice";

/**
 * drugApiSlice provides API endpoints for managing drug-related data.
 */
export const drugApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to search for drugs based on provided IDs.
         * @param data - Array of drug IDs to search for.
         * @returns A promise containing the search results.
         */
        getSearchDrug: builder.query({
            query: (data) => ({
                url: "/api/search_drug",
                method: "POST",
                body: { ids: data },
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),

        /**
         * Query to fetch all drugs.
         * @returns A promise containing the list of drugs.
         */
        getDrug: builder.query({
            query: () => ({
                url: "/api/drug",
                method: "GET",
            }),
        }),

        /**
         * Query to perform drug lookup based on provided data.
         * @param data - Data to perform drug lookup.
         * @returns A promise containing the result of the drug lookup.
         */
        drugLookUp: builder.query({
            query: (data) => ({
                url: '/api/drug_lookup',
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),

        /**
         * Query to fetch a drug by its ID.
         * @param id - ID of the drug to fetch.
         * @returns A promise containing the drug data.
         */
        getDrugById: builder.query({
            query: (id) => ({
                url: `/api/drug/${id}`,
                method: "GET",
            }),
        }),
        
        /**
         * Mutation to add a new drug.
         * @param data - Drug data to be added.
         * @returns A promise containing the result of the mutation.
         */
        addDrug: builder.mutation({
            query: (data) => ({
                url: "/api/drug",
                method: "POST",
                body: { ...data }
            }),
        }),
        
        /**
         * Mutation to update a drug by its ID.
         * @param id - ID of the drug to be updated.
         * @param data - New data for the drug.
         * @returns A promise containing the result of the mutation.
         */
        updateDrugById: builder.mutation({
            query: (id, data) => ({
                url: `/api/drug/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),
        
        /**
         * Mutation to delete a drug by its ID.
         * @param id - ID of the drug to be deleted.
         * @returns A promise containing the result of the mutation.
         */
        deleteDrugById: builder.mutation({
            query: (id) => ({
                url: `/api/drug/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetSearchDrugQuery,
    useGetDrugQuery,
    useGetDrugByIdQuery,
    useAddDrugMutation,
    useUpdateDrugByIdMutation,
    useDeleteDrugByIdMutation,
    useDrugLookUpQuery,
} = drugApiSlice;
