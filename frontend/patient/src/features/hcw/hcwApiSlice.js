import { apiSlice } from "../../app/api/apiSlice";

export const hcwApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
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
    useGetHcwQuery,
    useGetHcwByIdQuery,
    useUpdateHcwByIdMutation,
    useAddHcwMutation,
    useDeleteHcwByIdMutation,
} = hcwApiSlice;
