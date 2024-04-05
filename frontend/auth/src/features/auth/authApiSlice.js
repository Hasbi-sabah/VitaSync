import { apiSlice } from "../../app/api/apiSlice";

/**
 * Auth API slice.
 * 
 * This slice defines endpoints related to authentication, such as login.
 */
export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        /**
         * Endpoint for user login.
         * 
         * @param credentials - The user credentials (e.g., username, password).
         * @returns The API request configuration for login.
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
 * Hooks for authentication API.
 */
export const {
    /**
     * Hook for performing login mutation.
     * 
     * @returns The login mutation hook.
     */
    useLoginMutation
} = authApiSlice;
