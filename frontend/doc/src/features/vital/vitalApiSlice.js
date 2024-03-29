import { apiSlice } from "../../app/api/apiSlice";

export const vitalApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientVitalById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/vital`,
                method: "GET",
            }),
        }),
        addPatientVitalById: builder.mutation({
            query: (id, data) => ({
                url: `/api/patient/${id}/vital`,
                method: "POST",
                body: { ...data },
            }),
        }),
        deleteVitalById: builder.mutation({
            query: (id) => ({
                url: `/api/vital/${id}`,
                method: "DELETE",
            }),
        }),
        getVitalById: builder.query({
            query: (id) => ({
                url: `/api/vital/${id}`,
                method: "GET",
            }),
        }),
        updateVitalById: builder.mutation({
            query: (id, data) => ({
                url: `/api/vital/${id}`,
                method: "PUT",
                body: { ...data },
            }),
        }),
    }),
});

export const {
    useGetPatientVitalByIdQuery,
    useAddPatientVitalByIdMutation,
    useDeleteVitalByIdMutation,
    useGetVitalByIdQuery,
    useUpdateVitalByIdMutation,
} = vitalApiSlice;
