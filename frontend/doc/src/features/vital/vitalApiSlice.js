 /**
 * Import the apiSlice from the app's API configuration.
 */
import { apiSlice } from "../../app/api/apiSlice";

/**
 * Define the vitalApiSlice by injecting endpoints for various vital-related operations.
 * This includes fetching patient vitals by ID, adding patient vitals, deleting vitals,
 * fetching vitals by ID, and updating vitals by ID.
 * @returns {Object} The vitalApiSlice object with defined endpoints.
 */
export const vitalApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientVitalById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/vital`,
                method: "GET",
            }),
        }),
        addPatientVitalById: builder.mutation({
            query: (data) => ({
                url: `/api/patient/${data[0]}/vital`,
                method: "POST",
                body: { ...data[1] },
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

/**
 * Export hooks generated from the vitalApiSlice for use in components.
 * These hooks allow components to interact with the API endpoints defined above.
 */
export const {
    useGetPatientVitalByIdQuery,
    useAddPatientVitalByIdMutation,
    useDeleteVitalByIdMutation,
    useGetVitalByIdQuery,
    useUpdateVitalByIdMutation,
} = vitalApiSlice;
