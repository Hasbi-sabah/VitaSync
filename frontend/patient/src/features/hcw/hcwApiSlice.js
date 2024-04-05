import { apiSlice } from "../../app/api/apiSlice";

export const hcwApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to search for a healthcare worker by their ID.
         * @param data - data of the healthcare worker to fetch.
         * @returns A promise containing the healthcare worker data.
         */
        getSearchHcw: builder.query({
            query: (data) => ({
                url: "/api/search_hcw",
                method: "POST",
                body: { ...data },
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),

        /**
         * Query to fetch all healthcare workers.
         * @returns A promise containing the list of healthcare workers.
         */
        getHcw: builder.query({
            query: () => ({
                url: "/api/hcw",
                method: "GET",
            }),
        }),

        /**
         * Query to fetch a healthcare worker by their ID.
         * @param id - ID of the healthcare worker to fetch.
         * @returns A promise containing the healthcare worker data.
         */
        getHcwById: builder.query({
            query: (id) => ({
                url: `/api/hcw/${id}`,
                method: "GET",
            }),
        }),

        /**
         * Mutation to update a healthcare worker by their ID.
         * @param id - ID of the healthcare worker to update.
         * @param data - New data for the healthcare worker.
         * @returns A promise containing the result of the mutation.
         */
        updateHcwById: builder.mutation({
            query: (id, data) => ({
                url: `/api/hcw/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        /**
         * Mutation to add a new healthcare worker.
         * @param data - Data of the healthcare worker to be added.
         * @returns A promise containing the result of the mutation.
         */
        addHcw: builder.mutation({
            query: (data) => ({
                url: "/api/hcw/",
                method: "POST",
                body: { ...data }
            }),
        }),

        /**
         * Mutation to delete a healthcare worker by their ID.
         * @param id - ID of the healthcare worker to delete.
         * @returns A promise containing the result of the mutation.
         */
        deleteHcwById: builder.mutation({
            query: (id) => ({
                url: `/api/hcw/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});


export const {
    useGetSearchHcwQuery,
    useGetHcwQuery,
    useGetHcwByIdQuery,
    useUpdateHcwByIdMutation,
    useAddHcwMutation,
    useDeleteHcwByIdMutation,
} = hcwApiSlice;
