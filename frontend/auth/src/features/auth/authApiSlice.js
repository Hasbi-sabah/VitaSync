/**
 * Redux Toolkit slice for handling authentication API calls.
 * This slice includes a mutation for user login.
 */
import { apiSlice } from "../../app/api/apiSlice";

/**
 * Auth API slice.
 * 
 * This slice defines endpoints related to authentication, such as login.
 */
export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Login mutation for user authentication.
         * Sends a POST request to the /api/login endpoint with user credentials.
         * @param {Object} credentials - The user's login credentials.
         * @param {string} credentials.username - The user's username.
         * @param {string} credentials.password - The user's password.
         * @returns {Object} The response from the server, including a token if authentication is successful.
         */
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
 * Exports the login mutation hook for use in components.
 */
export const {
    /**
     * Hook for performing login mutation.
     * 
     * @returns The login mutation hook.
     */
    useLoginMutation
} = authApiSlice;
