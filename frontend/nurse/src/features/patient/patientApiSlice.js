import { apiSlice } from "../../app/api/apiSlice";

export const patientApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatient: builder.query({
            query: () => ({
                url: "/api/patient",
                method: "GET",
            }),
        }),
        
        getPatientById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}`,
                method: "GET",
            }),
        }),
        
        updatePatientById: builder.mutation({
            query: (id, data) => ({
                url: `/api/patient/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        addPatient: builder.mutation({
            query: (data) => ({
                url: "/api/patient",
                method: "POST",
                body: { ...data },
            }),
        }),

        deletePatientById: builder.mutation({
            query: (id) => ({
                url: `/api/patient/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetPatientQuery,
    useGetPatientByIdQuery,
    useUpdatePatientByIdMutation,
    useAddPatientMutation,
    useDeletePatientByIdMutation,
} = patientApiSlice;
