import { apiSlice } from "../../app/api/apiSlice";

export const appointmentApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientAppointmentById: builder.query({
            query: (id, data) => ({
                url: `/api/patient/${id}/appointment`,
                method: "GET",
                body: { ...data }
            }),
        }),

        getHCWAppointmentById: builder.query({
            query: (id, data) => ({
                url: `/api/hcw/${id}/appointment`,
                method: "GET",
                params: { ...data }
            }),
        }),

        addPatientAppointmentById: builder.mutation({
            query: (id, data) => ({
                url: `/api/patient/${id}/appointment`,
                method: "POST",
                body: { ...data }
            }),
        }),

        getAppointmentById: builder.query({
            query: (id) => ({
                url: `/api/appointment/${id}`,
                method: "POST",
            }),
        }),

        updateAppointmentById: builder.mutation({
            query: (id, data) => ({
                url: `/api/appointment/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        deleteAppointmentById: builder.mutation({
            query: (id) => ({
                url: `/api/appointment/${id}`,
                method: "DELETE",
            }),
        }),
    }),
});

export const {
    useGetPatientAppointmentByIdQuery,
    useGetHCWAppointmentByIdQuery,
    useAddPatientAppointmentByIdMutation,
    useGetAppointmentByIdQuery,
    useUpdateAppointmentByIdMutation,
    useDeleteAppointmentByIdMutation,
} = appointmentApiSclice;
