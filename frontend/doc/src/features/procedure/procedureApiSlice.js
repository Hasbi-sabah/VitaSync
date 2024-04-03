import { apiSlice } from "../../app/api/apiSlice";

export const procedureApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientProcedureById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/procedure`,
                method: "GET",
            }),
        }),

        addPatientProcedureById: builder.mutation({
            query: ({id, data}) => ({
                url: `/api/patient/${id}/procedure`,
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),

        getProcedureById: builder.query({
            query: (id) => ({
                url: `/api/procedure/${id}`,
                method: "GET",
            }),
        }),

        getProcedurePerformeddById: builder.mutation({
            query: (id) => ({
                url: `/api/procedure/${id}/perform`,
                method: "POST",
            }),
        }),

        updateProcedureById: builder.mutation({
            query: (id, data) => ({
                url: `/api/procedure/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        deleteProcedureById: builder.mutation({
            query: (id) => ({
                url: `/api/procedure/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetPatientProcedureByIdQuery,
    useAddPatientProcedureByIdMutation,
    useGetProcedureByIdQuery,
    useGetProcedurePerformeddByIdMutation,
    useUpdateProcedureByIdMutation,
    useDeleteProcedureByIdMutation,
} = procedureApiSclice;
