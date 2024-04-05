
/**
 * Imports necessary modules and functions for creating the API slice.
 * @module apiSlice
 */

import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { logOut } from '../../features/auth/authSlice';

/**
 * Retrieves the API URL from the environment variables.
 * @constant
 * @type {string}
 */
const api = process.env.REACT_APP_API_URL;
/**
 * Configures the base query for API requests.
 * @constant
 * @type {Function}
 */
const baseQuery = fetchBaseQuery({
    baseUrl: api,
    credentials: "include",
    prepareHeaders: (headers, { getState }) => {
        const token = getState().auth.token;
        if (token) {
            headers.set("Authorization", `Bearer ${token}`);
        }
        return headers;
    },
});

/**
 * Custom base query function that handles re-authentication.
 * @async
 * @function
 * @param {Object} args - The arguments for the base query.
 * @param {Object} api - The API object.
 * @param {Object} extraOptions - Additional options for the query.
 * @returns {Promise} The result of the base query.
 * @throws {Error} If the request fails with a 401 status.
 */
const baseQueryWithReauth = async (args, api, extraOptions) => {
    try {
        return await baseQuery(args, api, extraOptions);
    } catch (error) {
        if (error.status === 401) {
            api.dispatch(logOut());
        }
        throw error;
    }
};


/**
 * Creates the API slice with the custom base query and endpoints.
 * @constant
 * @type {Object}
 */
export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: baseQueryWithReauth,
    endpoints: () => ({}),
});
