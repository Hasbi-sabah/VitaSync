import { apiSlice } from "../../app/api/apiSlice";

export const drugApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getDrug: builder.query({
            query: () => ({
                url: "/api/drug",
                method: "GET",
            }),
        }),

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
        getDrugById: builder.query({
            query: (id) => ({
                url: `/api/drug/${id}`,
                method: "GET",
            }),
        }),
        
        addDrug: builder.mutation({
            query: (data) => ({
                url: "/api/drug",
                method: "POST",
                body: { ...data }
            }),
        }),
        
        updateDrugById: builder.mutation({
            query: (id, data) => ({
                url: `/api/drug/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),
        
        deleteDrugById: builder.mutation({
            query: (id) => ({
                url: `/api/drug/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetDrugQuery,
    useGetDrugByIdQuery,
    useAddDrugMutation,
    useUpdateDrugByIdMutation,
    useDeleteDrugByIdMutation,
    useDrugLookUpQuery,
} = drugApiSlice;
