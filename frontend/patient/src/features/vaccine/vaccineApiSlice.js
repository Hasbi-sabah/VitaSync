import { apiSlice } from "../../app/api/apiSlice";

export const vaccineApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getVaccineById: builder.query({
            query: (id) => ({
                url: `/api/vaccine/${id}`,
                method: "GET",
            }),
        }),

        addPatientVaccineById: builder.mutation({
            query: (id, data) => ({
                url: `/api/patient/${id}/vaccine`,
                method: "POST",
                body: { ...data},
            }),
        }),

        getPatientVaccineById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/vaccine`,
                method: "GET",
            }),
        }),

        deleteVaccineById: builder.mutation({
            query: (id) => ({
                url: `/api/vaccine/${id}`,
                method: "DELETE",
            }),
        }),

        updateVaccineById: builder.mutation({
            query: (id, data) => ({
                url: `/api/vaccine/${id}`,
                method: "PUT",
                data: { ...data }
            }),
        }),
    }),
});

export const {
    useGetVaccineByIdQuery,
    useAddPatientVaccineByIdMutation,
    useGetPatientVaccineByIdQuery,
    useDeleteVaccineByIdMutation,
    useUpdateVaccineByIdMutation,
} = vaccineApiSlice;
