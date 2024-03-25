import { apiSlice } from "../../app/api/apiSlice";

export const recordApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientRecordById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/record`,
                method: "GET",
            }),
        }),

        addPatientRecordById: builder.mutation({
            query: (id, data) => ({
                url: `/api/patient/${id}/record`,
                method: "POST",
                body: { ...data },
            }),
        }),

        getRecordById: builder.query({
            query: (id) => ({
                url: `/api/record/${id}`,
                method: "GET",
            }),
        }),

        updateRecordById: builder.mutation({
            query: (id, data) => ({
                url: `/api/record/${id}`,
                method: "PUT",
                body: { ...data },
            }),
        }),

        deleteRecordById: builder.mutation({
            query: (id) => ({
                url: `/api/record/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetPatientRecordByIdQuery,
    useAddPatientRecordByIdMutation,
    useGetRecordByIdQuery,
    useUpdateRecordByIdMutation,
    useDeleteRecordByIdMutation,
} = recordApiSlice;
