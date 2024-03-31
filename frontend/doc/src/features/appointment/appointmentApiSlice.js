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
            query: (data) => ({
                url: `/api/hcw/${data[0]}/appointment`,
                method: "POST",
                body: JSON.stringify(data[1]),
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),

        addPatientAppointmentById: builder.mutation({
            query: ({id, data}) => ({
                url: `/api/patient/${id}/appointment`,
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                },
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
