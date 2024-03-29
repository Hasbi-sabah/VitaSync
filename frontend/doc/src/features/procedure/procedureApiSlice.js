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
            query: (id, data) => ({
                url: `/api/patient/${id}/procedure`,
                method: "POST",
                body: { ...data }
            }),
        }),

        getProcedureById: builder.query({
            query: (id) => ({
                url: `/api/procedure/${id}`,
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
    useUpdateProcedureByIdMutation,
    useDeleteProcedureByIdMutation,
} = procedureApiSclice;
