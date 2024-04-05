/**
 * Imports the apiSlice from the app's API configuration.
 * This slice is used to define the endpoints for authentication-related API calls.
 */
import { apiSlice } from "../../app/api/apiSlice";

/**
 * Defines the authApiSlice by injecting endpoints for authentication.
 * This includes a login mutation endpoint that sends a POST request to the /api/login URL.
 * The credentials are sent in the body of the request.
 * @returns {Object} The authApiSlice object with the defined endpoints.
 */
export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        login: builder.mutation({
            query: credentials => ({
                url: "/api/login",
                method: "POST",
                body: { ...credentials},
            }),
        }),
    }),
});


/**
 * Exports the useLoginMutation hook from the authApiSlice.
 * This hook can be used in components to trigger the login mutation.
 */
export const {
    useLoginMutation
} = authApiSlice;
