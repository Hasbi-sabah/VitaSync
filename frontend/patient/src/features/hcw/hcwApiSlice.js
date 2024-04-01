import { apiSlice } from "../../app/api/apiSlice";

export const hcwApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
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

        getHcw: builder.query({
            query: () => ({
                url: "/api/hcw",
                method: "GET",
            }),
        }),

        getHcwById: builder.query({
            query: (id) => ({
                url: `/api/hcw/${id}`,
                method: "GET",
            }),
        }),

        updateHcwById: builder.mutation({
            query: (id, data) => ({
                url: `/api/hcw/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        addHcw: builder.mutation({
            query: (data) => ({
                url: "/api/hcw/",
                method: "POST",
                body: { ...data }
            }),
        }),

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
