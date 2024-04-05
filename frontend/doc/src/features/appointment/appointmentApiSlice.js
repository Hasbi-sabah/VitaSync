import { apiSlice } from "../../app/api/apiSlice";

/**
 * appointmentApiSlice provides API endpoints for appointment related operations.
 */
export const appointmentApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Query to get patient appointment by ID.
         * @param id - The ID of the patient.
         * @param data - Additional data for the request.
         * @returns A promise containing the result of the query.
         */
        getPatientAppointmentById: builder.query({
            query: (id, data) => ({
                url: `/api/patient/${id}/appointment`,
                method: "GET",
                body: { ...data }
            }),
        }),

        /**
         * Query to get HCW appointment by ID.
         * @param data - Array containing HCW ID and additional data.
         * @returns A promise containing the result of the query.
         */
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

        /**
         * Mutation to add patient appointment by ID.
         * @param param - Object containing patient ID and appointment data.
         * @returns A promise containing the result of the mutation.
         */
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

        /**
         * Query to get appointment by ID.
         * @param  id - The ID of the appointment.
         * @returns  A promise containing the result of the query.
         */
        getAppointmentById: builder.query({
            query: (id) => ({
                url: `/api/appointment/${id}`,
                method: "POST",
            }),
        }),

        /**
         * Mutation to update appointment by ID.
         * @param id - The ID of the appointment to be updated.
         * @param data - The updated appointment data.
         * @returns A promise containing the result of the mutation.
         */
        updateAppointmentById: builder.mutation({
            query: (id, data) => ({
                url: `/api/appointment/${id}`,
                method: "PUT",
                body: { ...data }
            }),
        }),

        /**
         * Mutation to delete appointment by ID.
         * @param id - The ID of the appointment to be deleted.
         * @returns A promise containing the result of the mutation.
         */
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
